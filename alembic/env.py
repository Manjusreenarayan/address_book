from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# This is the Alembic Config object, which provides access to the configuration values in your alembic.ini file.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your model's MetaData object here
from src.models import Base
target_metadata = Base.metadata

# Other necessary imports and configurations can go here
# ...

# This function should return the target metadata.
# This is used when generating migrations using the `--autogenerate` option.
def run_migrations_offline():
    context.configure(url=config.get_main_option("sqlalchemy.url"), target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

# This function should return the target metadata.
# This is used when generating migrations using the `--autogenerate` option.
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context:
    run_migrations_online()
else:
    run_migrations_offline()
