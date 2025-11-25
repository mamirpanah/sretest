from flask import Flask, request, jsonify, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import geoip2.database
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from config import Config
from db.models import Base, RequestLog, CountryStats

app = Flask(__name__)

# DB Setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# GeoIP Setup
reader = geoip2.database.Reader("geoip/GeoLite2-Country.mmdb")

# Prometheus counter
COUNTRY_REQUESTS = Counter(
    "country_requests_total",
    "Total number of requests per country",
    ["country"]
)

@app.route("/api/v1/country", methods=["GET"])
def get_country():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "")

    # GeoIP lookup
    try:
        response = reader.country(ip)
        country = response.country.name or "Unknown"
    except:
        country = "Unknown"

    db = SessionLocal()
    try:
        # Insert into RequestLog
        log = RequestLog(ip=ip, country=country, user_agent=user_agent)
        db.add(log)

        # Update country stats
        stat = db.query(CountryStats).filter_by(country=country).first()

        if not stat:
            stat = CountryStats(country=country, request_count=1)
            db.add(stat)
            count = 1
        else:
            stat.request_count += 1
            count = stat.request_count

        db.commit()

    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

    return jsonify({
        "ip": ip,
        "country": country,
        "user_agent": user_agent,
        "message": f"this is the {count} request from your country"
    })


@app.route("/metrics")
def metrics():
    """Expose Prometheus metrics from DB values"""
    db = SessionLocal()
    try:
        stats = db.query(CountryStats).all()

        if not stats:
            # No DB data yet — initialize default metric
            COUNTRY_REQUESTS.labels(country="Unknown")._value.set(0)

        else:
            # Sync metrics with DB values
            for s in stats:
                COUNTRY_REQUESTS.labels(country=s.country)._value.set(s.request_count)

    finally:
        db.close()

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
