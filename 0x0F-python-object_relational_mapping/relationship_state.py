#!/usr/bin/python3
"""contains the class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """contains the class definition of a State
    Args: base: te base class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
            "City",
            cascade="all, delete-orphan",
            backref=backref("state", cascade="all"),
            single_parent=True)
