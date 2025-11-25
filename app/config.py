import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg://postgres-user:OrP0sooy8sFEQ6@188.121.117.72:30464/geoip"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
