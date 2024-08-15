from sqlalchemy import Column, Text

from . import base

table_name = "ingredient"


class Recipe(base.Base):
    __tablename__ = table_name
    name: Column[Text] = Column(Text, nullable=False)
