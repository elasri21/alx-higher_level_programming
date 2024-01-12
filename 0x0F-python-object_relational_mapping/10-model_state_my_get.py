#!/usr/bin/python3
"""prints the State object with the name passed as
argument from the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(args[1], args[2], args[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).filter(State.name == args[4]).\
        order_by(State.id).all()
    if st:
        print("{}".format(st[0].id))
    else:
        print("Not found")
    session.close()
