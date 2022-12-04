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
    result = session.query(State).order_by(State.id).all()
    for entry in result:
        print("{}: {}".format(entry.id, entry.name))
        for city in entry.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
