from sqlalchemy import Column, Text, Integer, Boolean

from . import base

table_name = "recipe"


class Recipe(base.Base):
    __tablename__ = table_name
    title: Column[Text] = Column(Text, nullable=False)
    description: Column[Text] = Column(Text, nullable=False)
    user_id: Column[Integer] = Column(Integer, nullable=False)
    calories: Column[Integer] = Column(Integer, nullable=True)
    spice_level: Column[Integer] = Column(Integer, nullable=True)
    is_deleted: Column[Boolean] = Column(Boolean, nullable=False)
