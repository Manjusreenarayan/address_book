# Address Book Application

This is an address book application built using FastAPI. The application allows users to create, update, delete, and retrieve addresses. The addresses are stored in an SQLite database and include coordinates for each address.

## Installation

To run the address book application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a Virtual Environment using - "python -m venv .venv" in terminal
4. Activate the Virtual Environment using - ".venv\Scripts\activate" in terminal
5. Install the required dependencies using the following command:
   pip install -r requirements.txt
6. change the .env.example file name to .env

## Usage
To start the FastAPI server, use the following command:
uvicorn src.main:app --reload

The FastAPI server will start running at `http://127.0.0.1:8000`.

## API Documentation

The Swagger documentation for the API can be accessed at `http://127.0.0.1:8000/docs`.

## API Endpoints

The following API endpoints are available:

- `POST /addressbookrandom/`: Create a few random address entries.
- `POST /addressbook/`: Create a new address entry.
- `GET /addressbook/`: Retrieve all addresses from the address book.
- `GET /addressbook/{entry_id}`: Retrieve a specific address by ID.
- `PUT /addressbook/{entry_id}`: Update an existing address entry.
- `DELETE /addressbook/{entry_id}`: Delete an address entry.
- `GET /find_nearest_locations/`: Retrieves addresses within a specified distance from provided location coordinates.

## Validation

The addresses undergo validation to ensure the required fields are present and that the coordinates are properly formatted.

## Retrieval of Addresses within a Given Distance

The application allows users to retrieve addresses that are within a specified distance and location coordinates. The relevant API endpoint is:

- `GET /find_nearest_locations/`: Retrieve addresses within a given distance and location coordinates.

## Logging
Once you start the Fast API Server on your local Machine and start using the API's , you can find the logs stored on the app.log file under the logs Directory of this project

## Author

Manjusree Narayan
