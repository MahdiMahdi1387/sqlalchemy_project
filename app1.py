from sqlalchemy import create_engine, Column, INTEGER, FLOAT, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///CarData.db', echo=False)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

Base.metadata.create_all(engine)

class Customer(Base):
    __tablename__ = 'customerinfo'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    number = Column(String, nullable=False)
    address = Column(String, nullable=False)

Base.metadata.create_all(engine)
########################################

Session = sessionmaker(bind=engine)
session_local = Session()
########################################

# car1 = Car(brand='Benz', model='G class', price=2000, quantity=5)
# car2 = Car(brand='BMW', model='AMG', price=1500, quantity=10)

# session_local.add_all([car1, car2])
# session_local.commit()
########################################
# cars_obj = session_local.query(Car).all() # list of car objects

# for item in cars_obj:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--' * 30)

# #######################################

# # all of the vars bellow are object...
# car = session_local.query(Car).filter_by(id=1)  # selects by where id = 1
# car_all = session_local.query(Car).all()  # returns all
# car_first = session_local.query(Car).first()  # returns first record

# print(car)
# print(car_all)
# print(car_first)
# print('=' * 30)
# #######################################
# car_price1500 = session_local.query(Car).filter_by(price=1500).all()  # selects by where price = 1500

# for item in car_price1500:
#     print(f'Brand: {item.brand}')
#     print(f'Model: {item.model}')
#     print(f'Quantity: {item.quantity}')
#     print(f'Price: {item.price}')
#######################################
# car = session_local.query(Car).filter(Car.price > 1500).all()

# for item in car:
#     print(f'Brand: {item.brand}')
#     print(f'Model: {item.model}')
#     print(f'Quantity: {item.quantity}')
#     print(f'Price: {item.price}')
#     print('-' * 30)
#######################################
# car_temp = session_local.query(Car).filter(Car.model.like('%AMG%')).all()

# for item in car_temp:
#     print(f'Brand: {item.brand}')
#     print(f'Model: {item.model}')
#     print(f'Quantity: {item.quantity}')
#     print(f'Price: {item.price}')
#     print('-' * 30)
#######################################
car_temp = session_local.query(Car).filter(Car.model.like('%AMG%')).first()

car_temp.brand = 'AUDI'
session_local.commit()

# if car_temp is not None:
#     session_local.delete(car_temp)
#     session_local.commit()
