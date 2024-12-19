from typing import Optional
import os
from tortoise import Tortoise

POSTGRES_HOST = os.getenv("DB_HOST", "localhost")
POSTGRES_PORT = os.getenv("DB_PORT", "5432")
POSTGRES_DB = os.getenv("DB_NAME", "quiz_info")
POSTGRES_USER = os.getenv("DB_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("DB_PASSWORD", "1234")

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def init_db() -> None:
    try:
        await Tortoise.init(
            db_url=TORTOISE_ORM["connections"]["default"],
            modules={"models": TORTOISE_ORM["apps"]["models"]["models"]}
        )
        await Tortoise.generate_schemas()
        print("Ma'lumotlar bazasi muvaffaqiyatli ulanishi!")
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        print(f"Connection URL: {TORTOISE_ORM['connections']['default']}")
        raise

async def close_db() -> None:
    try:
        await Tortoise.close_connections()
    except Exception as e:
        print(f"Error closing database connection: {str(e)}")
