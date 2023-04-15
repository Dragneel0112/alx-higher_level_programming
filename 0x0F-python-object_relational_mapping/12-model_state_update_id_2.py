#!/usr/bin/python3
"""
Updates database where State object id=2 to New Mexico
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
    st = session.query(State).filter_by(id=2).first()
    st.name = "New Mexico"
    session.commit()
    session.close()
