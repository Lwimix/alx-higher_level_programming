#!/usr/bin/python3
"""This script lists all State objects from the
database hbtn_0e_6_usa using the print_states function.
It uses Object Relational Mapping(ORM) which in this case
is SQLAlchemy. It also imports the State class so as to use
it to manipulate data in the State table
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    def print_states(username, password, db_name):
        """ This prints all the states in the database
        hbtn_0e_6_usa
        """
        engine = create_engine(f"""mysql+mysqldb://
        {username}:{password}@localhost/
        {db_name}""", pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(select(State.id, State.name))\
            .order_by(State.id).all()
        for state in states:
            print("".join(state))
        session.close()
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    print_states(username, password, db_name)
