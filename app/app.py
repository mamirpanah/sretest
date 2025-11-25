from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import geoip2.database
from config import Config
from db.models import Base, RequestLog

app = Flask(__name__)

# DB Setup
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# GeoIP Setup
reader = geoip2.database.Reader("geoip/GeoLite2-Country.mmdb")

@app.route("/api/country", methods=["GET"])
def get_country():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    user_agent = request.headers.get("User-Agent", "")

    try:
        response = reader.country(ip)
        country = response.country.name or "Unknown"
    except:
        country = "Unknown"

    # Store in DB
    db = SessionLocal()
    log = RequestLog(ip_address=ip, country=country, user_agent=user_agent)
    db.add(log)
    db.commit()
    db.refresh(log)
    db.close()

    return jsonify({
        "ip": ip,
        "country": country,
        "user_agent": user_agent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
