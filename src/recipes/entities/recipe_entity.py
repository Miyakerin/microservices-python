from sqlalchemy import Column, Text

from . import base

table_name = "recipe"


class Recipe(base.Base):
    __tablename__ = table_name
    title: Column[Text] = Column(Text, nullable=False)
    description: Column[Text] = Column(Text, nullable=False)
