
# MoU Generator Backend

This is the backend service for the MoU (Memorandum of Understanding) Generator, built using FastAPI. This service provides several endpoints for generating and managing MoUs, along with some special functionalities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [GET /generate](#get-generate)
  - [POST /create](#post-create)
  - [GET /status/{id}](#get-statusid)
  - [PUT /update/{id}](#put-updateid)
  - [DELETE /delete/{id}](#delete-deleteid)
- [Special Works](#special-works)
- [Contributing](#contributing)
- [License](#license)

## Features
- Generate MoUs dynamically.
- Create, update, and delete MoUs.
- Check the status of MoU generation.
- Includes special functionalities for specific tasks.

## Installation
To get started with the MoU Generator backend, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/mou-generator-backend.git
    cd mou-generator-backend
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

## Usage
Once the application is running, you can interact with the API using tools like curl, Postman, or directly via the browser at `http://127.0.0.1:8000/docs` to access the automatically generated API documentation.

## API Endpoints

### GET /generate
Generate a new MoU.

**Request:**
```http
GET /generate
```

**Response:**
- `200 OK` on success
- `500 Internal Server Error` on failure

### POST /create
Create a new MoU with specified details.

**Request:**
```http
POST /create
Content-Type: application/json

{
    "title": "Sample MoU",
    "parties": ["Party A", "Party B"],
    "content": "Details of the MoU..."
}
```

**Response:**
- `201 Created` with the MoU ID
- `400 Bad Request` for invalid input

### GET /status/{id}
Check the status of a specific MoU generation process.

**Request:**
```http
GET /status/{id}
```

**Response:**
- `200 OK` with status details
- `404 Not Found` if the MoU ID does not exist

### PUT /update/{id}
Update an existing MoU.

**Request:**
```http
PUT /update/{id}
Content-Type: application/json

{
    "title": "Updated MoU Title",
    "parties": ["Party A", "Party B"],
    "content": "Updated details of the MoU..."
}
```

**Response:**
- `200 OK` on successful update
- `404 Not Found` if the MoU ID does not exist

### DELETE /delete/{id}
Delete an existing MoU.

**Request:**
```http
DELETE /delete/{id}
```

**Response:**
- `204 No Content` on successful deletion
- `404 Not Found` if the MoU ID does not exist

## Special Works
The backend includes special functionalities that go beyond basic CRUD operations. These may include:
- Custom MoU templates.
- Integration with external services for e-signatures.
- Automated reminders for MoU renewals.
- Analytics and reporting on MoU usage.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing coding style and includes appropriate tests.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to your branch.
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
