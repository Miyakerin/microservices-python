from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseHelper:
    def __init__(self, db_setting):
        self.connection_string = (
            f"postgresql+psycopg2://{db_setting.user}:{db_setting.password}"
            f"@{db_setting.host}/{db_setting.db}"
        )
        self.engine = create_engine(self.connection_string, echo=db_setting.echo)
        self.session_factory = sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False, expire_on_commit=False
        )
