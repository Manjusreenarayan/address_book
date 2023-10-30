from typing import List
from pydantic import BaseModel, Field

# Define the AddressBookEntry Pydantic model
class AddressBookEntry(BaseModel):
    name: str = Field(..., example="Manjusree")  # Name of the address book entry
    email: str = Field(..., example="manjusree@gmail.com")  # Email associated with the entry
    phone: str = Field(..., example="9987654321")  # Phone number associated with the entry
    address1: str = Field(..., example="123 Main St")  # First line of the address
    address2: str = Field(None, example="Apt 4B")  # Second line of the address (optional)
    city: str = Field(..., example="Bengaluru")  # City name
    state: str = Field(..., example="KA")  # State name
    pincode: int = Field(..., example=12345, ge=000000, le=999999)  # Pincode of the address
    country: str = Field(..., example="INDIA")  # Country name
    lat: float = Field(..., example=37.7749)  # Latitude coordinate of the address
    lng: float = Field(..., example=-122.4194)  # Longitude coordinate of the address

# Define the AddressBookEntries Pydantic model
class AddressBookEntries(BaseModel):
    address_book_list: List[AddressBookEntry] = Field(..., example=[AddressBookEntry])  # List of AddressBookEntry objects

# Define the AddressBookEntryCreate Pydantic model
class AddressBookEntryCreate(AddressBookEntry):
    pass

# Define the AddressBookEntryUpdate Pydantic model
class AddressBookEntryUpdate(AddressBookEntry):
    pass

# Define the AddressBookDeletion Pydantic model
class AddressBookDeletion(BaseModel):
    status: str = Field(..., example="entry_id has been deleted successfully")  # Status message for the deletion
