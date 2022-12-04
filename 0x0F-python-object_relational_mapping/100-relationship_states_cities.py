#!/usr/bin/python3
"""
This file lists all states via SQLAlchemy
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.ext.declarative import declarative_base

    user = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, db))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    n_state = State(name='California')
    n_city = City(name='San Francisco')

    n_state.cities.append(n_city)
    session.add(n_state)
    session.commit()
    session.close()
