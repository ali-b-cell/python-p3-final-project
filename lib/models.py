from sqlalchemy import Column, Integer, String, Float
from lib.database import Base

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    orders = relationship("Order". back populates "customer")
    
class Flower(Base):
    __tablename__ = 'flowers' 

    id = Column(Integer, primary_key=True)  
    name = Column(String)
    price = Column(Float) 
    stock_quantity = Column(Integer)
    order_items = relationship("OrderItem", back_populates="flower")

    def __repr__(self):
         return f"<Flower(name={self.name}, color={self.color},
         price={self.price})>"

class Order(Base):
      __tablename__ = 'orders'

      id = Column(Integer, primary_key=True)
      customer_id = Column(Integer, ForeignKey('customer.id'))
      date = Column(Date)
      total_price = Column(Date)
      customer = relationship("customer", back_populates="orders")
      items = relationship("OrderItem", back_populates="Orders")

class OrderItem(Base):
     __tablename__ = 'order_items'

     id = Column(Integer, primary_key=True)
     order_id = Column(Integer, ForeignKey('orders.id'))
     flower_id = Column(Integer, ForeignKey('flowers.id'))
     quantity = Column(Integer)

     order = relationship("order", back_populates="order_items")
      
