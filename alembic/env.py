from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.database import Base, DATABASE_URL

# Importar los modelos para registrarlos en SQLAlchemy
from models.usuario import Usuario
from models.rol import Rol
from models.permiso import Permiso
from models.rol_permiso import RolPermiso


config = context.config  # pylint: disable=no-member

# Configurar los registros de Alembic
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Verificar que exista la conexión a PostgreSQL
if not DATABASE_URL:
    raise RuntimeError("No se encontró DATABASE_URL")

# Configurar la URL de conexión
config.set_main_option(
    "sqlalchemy.url",
    DATABASE_URL.replace("%", "%%")
)

# Obtener los metadatos de los modelos
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()