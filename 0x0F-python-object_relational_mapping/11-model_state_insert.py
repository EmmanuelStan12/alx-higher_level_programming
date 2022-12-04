#!/usr/bin/python3
"""
This file lists all states via SQLAlchemy
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.ext.declarative import declarative_base

    user = argv[1]
    password = argv[2]
    db = argv[3]
    query = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, db))

    Session = sessionmaker(bind=engine)
    session = Session()
    l_state = State(name='Louisiana')
    session.add(l_state)
    session.commit()
    print("{}".format(l_state.id))
    session.close()
