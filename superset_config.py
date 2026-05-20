import os

# MySQL compatibility: make pymysql work as MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

# PostgreSQL
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://superset:superset@localhost:5432/superset"
)

# Redis cache
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_URL": os.environ.get("CACHE_REDIS_URL", "redis://localhost:6379/1"),
}

# Rate limiter storage backend
RATELIMIT_STORAGE_URL = os.environ.get("CACHE_REDIS_URL", "redis://localhost:6379/2")

# Celery
class CeleryConfig:
    broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
    result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
    worker_prefetch_multiplier = 1
    task_acks_late = False
    beat_schedule = {}

CELERY_CONFIG = CeleryConfig

# Secret key
SECRET_KEY = os.environ.get(
    "SUPERSET_SECRET_KEY",
    "your-secret-key-here-change-in-production-123456789"
)

# Feature flags
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
}

WTF_CSRF_ENABLED = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = "Lax"

# MCP Configuration
ENABLE_MCP = True
MCP_DEV_USERNAME = "khai.dt"

# LLM Configuration for MCP (vLLM compat)
LLM_PROVIDER = "openai"
LLM_ENDPOINT = "http://10.11.12.3:8000/v1"
LLM_MODEL = "qwen30b-awq"
LLM_API_KEY = "dummy"
LLM_TIMEOUT = 60
