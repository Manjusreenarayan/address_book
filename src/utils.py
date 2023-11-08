from sqlalchemy.orm import Session
import src.models as models
from src.schema import AddressBookEntry
import math

# Function to calculate the haversine distance between two points
def utils_haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    earth_radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance

# Function to create an address book entry
def utils_create_addressbook_entry(db: Session, entry: AddressBookEntry):
    try:
        entry_dict = entry.dict()

        db_entry = models.AddressBook(**entry_dict)
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
        return {"status": f"Address {db_entry.id} has been created successfully"}
    except Exception as e:
        db.rollback()
        raise e

# Function to get all address book entries
def utils_get_all_addressbook_entries(db: Session):
    try:
        return db.query(models.AddressBook).all()
    except Exception as e:
        db.rollback()
        raise e

# Function to get an address book entry by ID
def utils_get_addressbook_entry(db: Session, entry_id: str):
    try:
        return db.query(models.AddressBook).filter(models.AddressBook.id == entry_id).first()
    except Exception as e:
        db.rollback()
        raise e

# Function to update an address book entry
def utils_update_addressbook_entry(db: Session, entry_id: str, entry: AddressBookEntry):
    try:
        db_entry = db.query(models.AddressBook).filter(models.AddressBook.id == entry_id).first()
        if db_entry is None:
            return None

        for field, value in entry.dict().items():
            setattr(db_entry, field, value)

        db.commit()
        db.refresh(db_entry)
        return {"status": f"Address {db_entry.id} has been updated successfully"}
    except Exception as e:
        db.rollback()
        raise e

# Function to delete an address book entry
def utils_delete_addressbook_entry(db: Session, entry_id: str):
    try:
        db_entry = db.query(models.AddressBook).filter(models.AddressBook.id == entry_id).first()
        if db_entry:
            db.delete(db_entry)
            db.commit()
            return {"status": f"{entry_id} has been deleted successfully"}
        else:
            return {"status": f"{entry_id} not found"}
    except Exception as e:
        db.rollback()
        raise e
