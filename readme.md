# todo_app_fastapi

A simple FastAPI-based TODO application that provides a minimal REST API for managing tasks. This project utilizes FastAPI and SQLite3 for data storage, implementing standard REST methods: GET, POST, PUT, and DELETE.

## Features
- Create, read, update, and delete TODO items.
- RESTful API with JSON responses.
- SQLite3 database for persistent storage.

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn
- SQLite3 (included with Python)

## Installation
1. Clone the repository or download the project files.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install the required packages:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application
To start the FastAPI application, run:
```bash
uvicorn app.main:app --reload
```
Access the API documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints
- **GET /todos**: Retrieve a list of all TODO items.
- **POST /todos**: Create a new TODO item.
- **GET /todos/{id}**: Retrieve a specific TODO item by ID.
- **PUT /todos/{id}**: Update an existing TODO item.
- **DELETE /todos/{id}**: Delete a TODO item.

## Data Model
- `id`: int (auto-incremented)
- `title`: str
- `description`: Optional[str]
- `completed`: bool (default: false)
- `created_at`: datetime

## Configuration
- Configure the SQLite3 database connection in the application settings.
- Use environment variables for sensitive information.

## Testing
- Write tests using pytest and FastAPI's TestClient to ensure API functionality.

## Contributing
Contributions are welcome! Please ensure to follow the project's coding standards and add tests for new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.