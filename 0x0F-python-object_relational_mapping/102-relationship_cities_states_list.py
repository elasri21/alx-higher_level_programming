#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(args[1], args[3], args[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ct, st in session.query(City, State)\
            .join(State, State.id == City.state_id).order_by(City.id):
        print("{}: {} -> {}".format(ct.id, ct.name, st.name))
