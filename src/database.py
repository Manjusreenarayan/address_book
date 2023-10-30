import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Define the function to establish a database connection
def Database(URL): 
    # Set the SQLAlchemy database URL
    SQLALCHEMY_DATABASE_URL = URL
    
    # Initialize metadata
    metadata = MetaData()
    
    # Create an engine with the given URL
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    
    # Create a local session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Define the 'addressbook' table with the necessary columns
    addressbook = sqlalchemy.Table(
        "addressbook",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
        sqlalchemy.Column("name", sqlalchemy.String, index=True),
        sqlalchemy.Column("email", sqlalchemy.String),
        sqlalchemy.Column("phone", sqlalchemy.String),
        sqlalchemy.Column("address1", sqlalchemy.String),
        sqlalchemy.Column("address2", sqlalchemy.String),
        sqlalchemy.Column("city", sqlalchemy.String),
        sqlalchemy.Column("state", sqlalchemy.String),
        sqlalchemy.Column("pincode", sqlalchemy.Integer),
        sqlalchemy.Column("country", sqlalchemy.String),
        sqlalchemy.Column("lat", sqlalchemy.Float),
        sqlalchemy.Column("lng", sqlalchemy.Float)
    )

    # Define a declarative base
    Base = declarative_base()
    
    # Create all defined tables in the engine
    metadata.create_all(bind=engine)
    
    try:
        # Attempt to establish a connection to the database
        connection = engine.connect()
    except SQLAlchemyError as e:
        # Handle any potential connection errors
        print(f"Error connecting to database: {e}")
        return None, None, None
    
    # Return the engine, local session, and addressbook table
    return engine, SessionLocal, addressbook
