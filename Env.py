"""
Add Environment variables here

Reference: https://pypi.org/project/envguardian/
"""

from envguardian import Env

env_schema = {
    "SECRET_KEY": Env.string(),
    "DEBUG": Env.boolean(),
    "DATABASE_NAME": Env.string(),
    "DATABASE_USER": Env.string(),
    "DATABASE_HOST": Env.string(),
    "DATABASE_PASSWORD": Env.string(),
    "DATABASE_PORT": Env.integer(),
}

