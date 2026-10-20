from sqlalchemy import create_engine, Column, INTEGER, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///CarData_Relation.db', echo=False)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    id = Column(INTEGER, primary_key= True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(Float)
    quantity = Column(INTEGER)

    customer_id = Column(INTEGER, ForeignKey('customerinfo.id'))

    customers = relationship('Customer', back_populates='owner')


class Customer(Base):
    __tablename__ = 'customerinfo'

    id = Column(INTEGER, primary_key=True)
    name  = Column(String)
    address = Column(String)
    mobile_number = Column(String)

    owner = relationship('Car', back_populates='customers')

Base.metadata.create_all(engine)
#############################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

#############################################
customer1 = Customer(name='Ali Akbari', address ='Ahwaz', mobile_number='0123')
customer2 = Customer(name='Nima Akbari', address ='Tehran', mobile_number='2333')

sessionLocal.add_all([customer1, customer2])
sessionLocal.commit()


car1 = Car(brand ='Benz', model='G1 class', price = 2000, quantity =15, customer_id =1 )
car2 = Car(brand ='BMW', model='AMG2', price = 1500, quantity =10, customer_id =1)
sessionLocal.add_all([car1, car2])
sessionLocal.commit()

customer1 = sessionLocal.query(Customer).filter_by(id = 1).first()

# print(customer1.owner)
for car in customer1.owner:
    print(car.brand)
    print(car.model)
    print('--'*30)
