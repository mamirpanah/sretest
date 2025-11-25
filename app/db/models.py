from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True)
    ip = Column(String, nullable=False)
    user_agent = Column(String, nullable=False)
    country = Column(String, nullable=False)

class CountryStats(Base):
    __tablename__ = "country_stats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, unique=True, nullable=False)
    request_count = Column(Integer, nullable=False, default=0)