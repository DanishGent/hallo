from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine



Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()


class Person(Base):

    __tablename__ = "products"
    product_number = Column(Integer, primary_key=True)
    brand = Column(String)
    price = Column(Integer)


    def __repr__(self):
        return f"Person({self.product_number=}    {self.brand=}    {self.price=})"


def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Person(brand="pipss", price=6))
        session.add_all(new_items)
        session.commit()


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

create_test_data()