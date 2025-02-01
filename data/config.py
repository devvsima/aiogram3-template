from pathlib import Path
from environs import Env

DIR = Path(__file__).absolute().parent.parent

env = Env()
env.read_env()

# ---< Telegram bot >---
TG_TOKEN: str = env.str("TOKEN", default=None)
ADMINS: list = env.list("ADMINS", default=None, subcast=int)
SKIP_UPDATES: bool = env.bool("SKIP_UPDATES", default=False)

# ---< Database >---
MONGO_HOST: str = env.str("MONGO_HOST", default="localhost")
MONGO_PORT: int = env.int("MONGO_PORT", default=27017)
MONGO_USER: str = env.str("MONGO_USER", default=None)
MONGO_PASS: str = env.str("MONGO_PASS", default=None)
MONGO_NAME: str = env.str("MONGO_NAME", default="template")

MONGO_URL = env.str("MONGO_URL", default="mongodb://{MONGO_HOST}:{MONGO_PORT}/")

if all([MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT]):
    MONGO_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/"

# ---< Redis >---
REDIS_HOST: str = env.str("REDIS_HOST", default=None)
REDIS_PORT: int = env.int("REDIS_PORT", default=6379)
REDIS_DB: int = env.int("REDIS_DB", default=5)

REDIS_URL: str = env.str("RD_URI", default=None)

if all([REDIS_DB, REDIS_HOST, REDIS_PORT]):
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# ---< Other >---
I18N_DOMAIN = "bot"

IMAGES_DIR = rf"{DIR}/images"
LOCALES_DIR = f"{DIR}/data/locales"
