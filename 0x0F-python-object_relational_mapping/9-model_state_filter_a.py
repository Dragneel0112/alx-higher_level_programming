#!/usr/bin/python3
"""
Lists all State objects from a database with the letter a
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    st = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for s in st:
        print("{}: {}".format(s.id, s.name))
    session.close()
