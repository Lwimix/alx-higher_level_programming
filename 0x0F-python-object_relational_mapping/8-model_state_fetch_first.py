#!/usr/bin/python3
"""This script prints the first State object from the
database hbtn_0e_6_usa using the print_state function.
It uses Object Relational Mapping(ORM) which in this case
is SQLAlchemy. It also imports the State class so as to use
it to manipulate data in the State table
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def print_state(username, password, db_name):
    """ This prints the first state in the database
    hbtn_0e_6_usa
    """
    engine = create_engine(f"""mysql+mysqldb://
    {username}:{password}@localhost/
    {db_name}""", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(select(State.id, State.name))\
        .order_by(State.id).first()
    if not state:
        print("Nothing")
    else:
        print("".join(state))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    print_state(username, password, db_name)
