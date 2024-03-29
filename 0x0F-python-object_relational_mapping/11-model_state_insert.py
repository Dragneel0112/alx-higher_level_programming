#!/usr/bin/python3
"""
Adds State Louisiana to database
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    st = session.query(State).filter_by(name='Louisiana').first()
    print(str(st.id))
    session.commit()
    session.close()
