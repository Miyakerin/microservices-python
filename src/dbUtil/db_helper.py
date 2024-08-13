from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)


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

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.get_scoped_session() as session:
            yield session
            await session.remove()
