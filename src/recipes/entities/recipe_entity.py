from sqlalchemy import Column, Text

from . import base


class Recipe(base.Base):
    __tablename__ = "recipe"
    title: Column[Text] = Column(Text, nullable=False)
    description: Column[Text] = Column(Text, nullable=False)
