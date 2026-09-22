"""
config.py — Central configuration for ShizuMusic.
All secrets must be provided through environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()


# ── Required Telegram configuration ─────────────────────────────────────────

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Telegram user-account session used by the Assistant for voice-chat playback.
STRING_SESSION = os.environ["STRING_SESSION"]

# MongoDB connection string.
MONGO_DB_URL = os.environ["MONGO_DB_URL"]

# Your Telegram numeric user ID.
OWNER_ID = int(os.environ["OWNER_ID"])


# ── Optional bot configuration ───────────────────────────────────────────────

BOT_NAME = os.getenv("BOT_NAME", "Shizu Music")

BOT_LINK = os.getenv(
    "BOT_LINK",
    "https://t.me/ShizuMusicBot",
)

UPDATES_CHANNEL = os.getenv(
    "UPDATES_CHANNEL",
    "https://t.me/PBX_UPDATE",
)

SUPPORT_GROUP = os.getenv(
    "SUPPORT_GROUP",
    "https://t.me/PBXCHATS",
)

LOGGER_ID = int(os.getenv("LOGGER_ID", "0"))

PING_IMG_URL = os.getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/ddzvc0.jpg",
)

SESSION_NAME = os.getenv(
    "SESSION_NAME",
    "ShizuMusic",
)

PORT = int(os.getenv("PORT", "10000"))


# ── Shruti API ───────────────────────────────────────────────────────────────

SHRUTI_API_URL = os.getenv(
    "SHRUTI_API_URL",
    "https://api.shrutibots.site",
)

# Keep the API key in the hosting platform's Environment Variables.
SHRUTI_API_KEY = os.environ["SHRUTI_API_KEY"]

DOWNLOAD_DIR = os.getenv(
    "DOWNLOAD_DIR",
    "downloads",
)

SHRUTI_TOKEN_TIMEOUT = 10
SHRUTI_STREAM_TIMEOUT = 900


# ── Playback limits ──────────────────────────────────────────────────────────

MAX_DURATION_SECONDS = 1800  # 30 minutes
QUEUE_LIMIT = 20
COOLDOWN = 10                 # seconds between /play commands


# ── Start images ─────────────────────────────────────────────────────────────

START_PHOTOS = [
    "https://files.catbox.moe/jgt2vm.png",
]
