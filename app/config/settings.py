import os

class Config:
    DEBUG = os.getenv("DEBUG", True)
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///smartlogistics.db")

