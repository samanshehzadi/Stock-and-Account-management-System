from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize database
engine = create_engine('sqlite:///database/restaurant_management.db')
Base = declarative_base()

# Define Tables
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    vendor_id = Column(Integer, ForeignKey('vendors.vendor_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

class Vendor(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String, nullable=False)
    total_paid = Column(Float, default=0.0)
    remaining_credit = Column(Float, default=0.0)

class Kitchen(Base):
    __tablename__ = 'kitchen'
    kitchen_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    quantity_used = Column(Integer, nullable=False)
    used_cost = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

class Sale(Base):
    __tablename__ = 'sales'
    sale_id = Column(Integer, primary_key=True)
    order_id = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    sale_price = Column(Float, nullable=False)
    payment_status = Column(String, nullable=False)
    date = Column(Date, nullable=False)

class DailyBalance(Base):
    __tablename__ = 'daily_balances'
    balance_id = Column(Integer, primary_key=True)
    opening_balance = Column(Float, default=0.0)
    closing_balance = Column(Float, nullable=False)
    used_balance = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Print success message
print("Database and tables created successfully!")

# Session maker
Session = sessionmaker(bind=engine)
session = Session()