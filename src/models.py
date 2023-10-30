# Import necessary libraries and modules
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()


# Define the AddressBook model
class AddressBook(Base):
    # Set the table name
    __tablename__ = "addressbook"

    # Define the columns
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the table
    name = Column(String, index=True)  # Name of the address entry
    email = Column(String)  # Email associated with the address
    phone = Column(String)  # Phone number associated with the address
    address1 = Column(String)  # First line of the address
    address2 = Column(String)  # Second line of the address
    city = Column(String)  # City name
    state = Column(String)  # State name
    pincode = Column(Integer)  # Pincode of the address
    country = Column(String)  # Country name
    lat = Column(Float)  # Latitude coordinate of the address
    lng = Column(Float)  # Longitude coordinate of the address

