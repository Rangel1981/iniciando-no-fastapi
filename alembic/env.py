import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config
from sqlalchemy import pool

from alembic import context

# 1. Importe o BaseModel
from workout.contrib.models import BaseModel

# 2. IMPORTANTE: Importe todos os seus modelos aqui. 
# Sem esses imports, o 'target_metadata' ficará vazio!
from workout.atleta.models import AtletaModel
from workout.categorias.models import CategoriaModel
from workout.centro_treinamento.models import CentroTreinamentoModel

# Interpretador do arquivo de configuração do Alembic (alembic.ini)
config = context.config

# Configura o logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define o alvo dos metadados para o autogenerate
target_metadata = BaseModel.metadata

def run_migrations_offline() -> None:
    """Executa migrações no modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    """Configura o contexto da migração para o modo online."""
    # Corrigido de 'arget_metadata' para 'target_metadata'
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    """Cria o engine assíncrono e roda a migração em modo síncrono."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    
    async with connectable.connect() as connection:
        # run_sync executa uma função síncrona em um ambiente assíncrono
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    """Executa migrações no modo 'online'."""
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()