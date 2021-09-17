import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Todoroki Music")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/9df06211ca97d34bc930c.jpg")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/b475b03020311ad0c3080.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/9df06211ca97d34bc930c.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/9df06211ca97d34bc930c.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/9df06211ca97d34bc930c.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "todorokiXrobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TodorokiAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "todorokisupportgrup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "todorokiproject")
OWNER_NAME = getenv("OWNER_NAME", "tdrki_1") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "tdrki_1")
PMPERMIT = getenv("PMPERMIT", "ENABLE")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
