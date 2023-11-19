#!/usr/bin/python3
"""Start linking class to table in database
This module imports the Base and State class
which enable access to the State table in
the sys.argv[3] database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(f"""mariadb+mariadb://{sys.argv[1]}:
                           {sys.argv[2]}@localhost/
                           {sys.argv[3]}""", pool_pre_ping=True)
    Base.metadata.create_all(engine)
