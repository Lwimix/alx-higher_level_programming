#!/usr/bin/python3
"""This script lists all City objects from the
database hbtn_0e_14_usa using the print_cities function.
It uses Object Relational Mapping(ORM) which in this case
is SQLAlchemy. It also imports the City class so as to use
it to manipulate data in the cities table
"""
import sys
from model_state import Base
from model_city import City
from sqlalchemy import (create_engine)
from spqlalchemy.orm import sessionmaker


def print_cities(username, password, db_name):
    """ This prints all the cities in the database
    hbtn_0e_14_usa
    """
    engine = create_engine(f"""mysql+mysqldb://
    {username}:{password}@localhost/
    {db_name}""", pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(select(State.name, City.id, City.name)) \
        .join(State, State.id == City.state_id) \
        .order_by(City.id)
    for city in cities:
        print("{}".format(city))
    session.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    print_states(username, password, db_name)
