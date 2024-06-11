# Book_Catalog_project

## Description

Book Catalog Project is a web application for managing a catalog of books. Users can add, edit, delete, and view books in the catalog. The application also supports user authentication and filtering of books by genre, author, and publication date.

## Features

- User registration and authentication
- Add, edit, and delete books
- Filter books by genre, author, and publication date
- Email notifications

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Nurgazy22/Book_Catalog_project.git
    cd Book_Catalog_project
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure the database:

    Update the `.env` file with your database settings. Example:

    ```plaintext
    DATABASE_URL=postgres://nurgazy:1@localhost:5432/books_db
    ```

5. Apply migrations:

    ```sh
    python manage.py migrate
    ```

6. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

7. Start the server:

    ```sh
    python manage.py runserver
    ```

## Usage

1. Open your browser and go to `http://127.0.0.1:8000/admin` to log in to the admin panel using your superuser credentials.
2. To interact with the API, use the following endpoints:
    - Get a list of books: `GET /api/books/`
    - Filter books by genre, author, and publication date: `GET /api/books/?genre=<genre_id>&author=<author_id>&publication_date=<yyyy-mm-dd>`
    - Add a book: `POST /api/books/`
    - Update a book: `PUT /api/books/<id>/`
    - Partially update a book: `PATCH /api/books/<id>/`
    - Delete a book: `DELETE /api/books/<id>/`

Examples of requests using `curl`:

- **Add a book**:

    ```sh
    curl -X POST http://127.0.0.1:8000/api/books/ \
    -H "Authorization: Token your_token" \
    -H "Content-Type: application/json" \
    -d '{ 
        "title": "New Book", 
        "genre": 1, 
        "author": 1, 
        "publication_date": "2024-06-07", 
        "description": "A great book!" 
    }'
    ```

- **Update a book**:

    ```sh
    curl -X PUT http://127.0.0.1:8000/api/books/1/ \
    -H "Authorization: Token your_token" \
    -H "Content-Type: application/json" \
    -d '{ 
        "title": "Updated Book Title", 
        "genre": 1, 
        "author": 1, 
        "publication_date": "2024-06-07", 
        "description": "Updated description of the book" 
    }'
    ```

- **Partially update a book**:

    ```sh
    curl -X PATCH http://127.0.0.1:8000/api/books/1/ \
    -H "Authorization: Token your_token" \
    -H "Content-Type: application/json" \
    -d '{ 
        "description": "Partially updated description" 
    }'
    ```

- **Delete a book**:

    ```sh
    curl -X DELETE http://127.0.0.1:8000/api/books/1/ \
    -H "Authorization: Token your_token"
    ```

## Contributing

If you would like to contribute to this project, please fork the repository, create a feature branch (`git checkout -b my-feature-branch`), commit your changes, and open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
