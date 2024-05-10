# Copyright (c) 2022 - 2024 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("APP_ID", "10471716"))
    API_HASH = os.environ.get("API_HASH","f8a1b21a13af154596e2ff5bed164860")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6933485941:AAGwZMeIbR6kA52usoVOh5nDHL4YgFC38H4")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002048766471"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://appuz:chrijismiappuz@cluster0.yngvhc2.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6883997969"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    MAX_MESSAGE_LENGTH = 4096
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
