#!/usr/bin/python3
"""
This file lists all states via SQLAlchemy
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship

    user = argv[1]
    password = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    State.cities = relationship('City', order_by=City.id,
                                back_populates='state')
    result = session.query(State, City).\
        filter(City.state_id == State.id).all()
    for row in result:
        print("{}: ({}) {}".format(row[0].name, row[0].id, row[1].name))
    session.close()
