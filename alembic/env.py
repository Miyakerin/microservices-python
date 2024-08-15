import os
import re

from logging.config import fileConfig

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
url_tokens = {
    "RECIPES_DB_USER": os.getenv("RECIPES_DB_USER", ""),
    "RECIPES_DB_PASSWORD": os.getenv("RECIPES_DB_PASSWORD", ""),
    "RECIPES_DB_HOST": os.getenv("RECIPES_DB_HOST", ""),
    "RECIPES_DB_PORT_CONTAINER": os.getenv("RECIPES_DB_PORT_CONTAINER", ""),
    "RECIPES_DB_DB": os.getenv("RECIPES_DB_DB", ""),
}

url = config.get_main_option("sqlalchemy.url")

url = re.sub(r"\${(.+?)}", lambda m: url_tokens[m.group(1)], url)


def run_migrations_offline() -> None:
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:

    connectable = create_engine(url)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
