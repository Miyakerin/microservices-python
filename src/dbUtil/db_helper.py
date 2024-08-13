from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class DatabaseHelper:
    def __init__(self, db_setting):
        self.connection_string = (
            f"postgresql+asyncpg://{db_setting.user}:{db_setting.password}"
            f"@{db_setting.host}:{db_setting.port_host}/{db_setting.db}"
        )
        self.engine = create_async_engine(self.connection_string, echo=db_setting.echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=False
        )
