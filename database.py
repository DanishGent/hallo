from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine



Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()


class Person(Base):


    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Person(name="peter", age=18))
        session.add_all(new_items)
        session.commit()




engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()