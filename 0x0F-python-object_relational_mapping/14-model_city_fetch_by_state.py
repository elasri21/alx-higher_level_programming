#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        args[1], args[2], args[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    all_cities = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for ct, st in all_cities:
        print("{}: ({}) {}".format(st.name, ct.id, ct.name))
    session.commit()
    session.close()
