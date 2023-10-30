# Import necessary libraries and modules
from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from . import database, utils, models
from .config import Config
from .schema import AddressBookEntry, AddressBookEntryCreate, AddressBookEntryUpdate, AddressBookDeletion
import logging, logging.config
from fastapi import FastAPI
import os
from datetime import datetime
from faker import Faker
import random
import yaml

# SQLite database connection
connection, SessionLocal, addressbook = database.Database(Config.DATABASE_URL)

# Initialize FastAPI app
app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add logger to all API endpoints
logger = logging.getLogger(__name__)

# Get the absolute path to the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Construct the absolute path to logs_conf.yaml
config_path = os.path.join(current_directory, "log_conf.yaml")

# Load the configuration file
with open(config_path, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)



# Endpoint for creating an address book entry
@app.post("/addressbook/")
def create_addressbook_entry(entry: AddressBookEntryCreate, db: Session = Depends(get_db)):
    logger.info("Creating address book entry")
    db_entry = utils.create_addressbook_entry(db, entry)
    return db_entry

@app.post("/addressbookrandom/")
def create_random_addresses(count: int = Query(..., title="Number of Addresses"), db: Session = Depends(get_db)):
    if count < 1:
        raise HTTPException(status_code=400, detail="Count must be greater than 0")
    random_addresses = []
    for _ in range(count):
        fake = Faker()
        address_entity = AddressBookEntryCreate(
            name=fake.first_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address1=fake.street_address(),
            address2=fake.secondary_address(),
            city=fake.city(),
            state=fake.state_abbr(),
            pincode=random.randint(10000, 99999),
            country=fake.country(),
            lat=fake.latitude(),
            lng=fake.longitude()
        )
        random_addresses.append(address_entity)
    result = [utils.create_addressbook_entry(db, random_address ) for random_address in random_addresses]
    return {"status":f"{count} number of random addresses created in addressbook"}


# Endpoint for retrieving all address book entries
@app.get("/addressbook/")
def get_addressbook_entries(db: Session = Depends(get_db)):
    try:
        logger.info("Retrieving all address book entries")
        entry = utils.get_all_addressbook_entries(db)
        if entry is None or entry == []:
            return {"error": "No Data found"}
        return {"address_book_list": entry}
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Endpoint for retrieving a specific address book entry by ID
@app.get("/addressbook/{entry_id}", response_model=AddressBookEntry)
def get_addressbook_entry(entry_id: str, db: Session = Depends(get_db)):
    logger.info(f"Retrieving address book entry with id: {entry_id}")
    entry = utils.get_addressbook_entry(db, entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry

# Endpoint for updating a specific address book entry by ID
@app.put("/addressbook/{entry_id}")
def update_addressbook_entry(entry_id: str, entry: AddressBookEntryUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating address book entry with id: {entry_id}")
    db_entry = utils.update_addressbook_entry(db, entry_id, entry)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

# Endpoint for deleting a specific address book entry by ID
@app.delete("/addressbook/{entry_id}", response_model=AddressBookDeletion)
def delete_addressbook_entry(entry_id: str, db: Session = Depends(get_db)):
    logger.info(f"Deleting address book entry with id: {entry_id}")
    db_entry = utils.delete_addressbook_entry(db, entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

# Endpoint for finding the nearest locations based on target coordinates and distance
@app.get("/find_nearest_locations/")
async def find_nearest_locations(
    target_latitude: float = Query(..., title="Target Latitude"),
    target_longitude: float = Query(..., title="Target Longitude"),
    distance: float = Query(..., title="Search Distance in Kilometers"), 
    db: Session = Depends(get_db)
):
    logger.info("Finding nearest locations")
    # Calculate distances and query the database for nearest locations
    locations = utils.get_all_addressbook_entries(db)
    locations_within_distance = []

    for location in locations:
        dist = utils.haversine(target_latitude, target_longitude, location.lat, location.lng)
        if dist <= distance:
            locations_within_distance.append({"nearest_locations": location, "distance": dist})

    # Sort the locations by distance
    locations_within_distance.sort(key=lambda x: x["distance"])

    # Close the database session
    db.close()

    return {"nearest_locations_within_distance": locations_within_distance}
