from orator import DatabaseManager, Model
import os


V1_API_URL = "https://api.clockify.me/api/v1"
WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID")
HEADERS = {
    "X-Api-Key": os.getenv("CLOCKIFY_API_KEY"),
    "content-type": "application/json",
}

DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

CONFIG = {
    "default": os.getenv("ENVIRONMENT"),
    "production": {
        "driver": "postgres",
        "host": DB_HOSTNAME,
        "database": DB_NAME,
        "user": DB_USERNAME,
        "password": DB_PASSWORD,
        "prefix": "",
    },
    "development": {
        "driver": "postgres",
        "host": "metis-data.c7l51j6b7kxo.us-east-2.rds.amazonaws.com",
        "database": "metis-data",
        "user": "metis",
        "password": "metisstrategy",
        "prefix": "",
    },
}


db = DatabaseManager(CONFIG)
Model.set_connection_resolver(db)
from .client import Client
from .member import Member
from .project import Project
from .time_entry import TimeEntry
from .indicator import Indicator
from .indicator_consolidation import IndicatorConsolidation
