# Blog API with FastAPI and PostgreSQL

This is a simple blog API implemented with FastAPI and PostgreSQL. The API supports creating, reading, updating, and deleting blog posts. Additionally, it supports pagination and search functionality.

## Features

- **CRUD Operations**: Create, Read, Update, and Delete blog posts.
- **Pagination**: Paginate the list of blog posts.
- **Search**: Search blog posts by title or content.
- **Docker**: The project is containerized using Docker and Docker Compose.

## Endpoints

- `GET /posts`: Returns a list of all blog posts with optional pagination.
- `GET /posts/{id}`: Returns a single blog post by ID.
- `POST /posts`: Creates a new blog post.
- `PUT /posts/{id}`: Updates an existing blog post by ID.
- `DELETE /posts/{id}`: Deletes a blog post by ID.
- `GET /posts/search`: Searches for blog posts by title or content.

## Requirements

- Docker
- Docker Compose

## Setup and Running
1. Initialize containers for project via CLI from root directory (/test):
   docker-compose up --build
2. Take notice that connection data for Postgres is env-encoded in .env and are default data.

Once the containers are up and running, you can access the API at http://localhost:8000.
You can use Postman to interact with the API. Here are some example requests:

Get all posts
Method: GET
URL: http://localhost:8000/posts
Query Params:
skip (optional): The starting index for pagination (default is 0).
limit (optional): The number of posts to return (default is 10).

Get a post by ID
Method: GET
URL: http://localhost:8000/posts/{id} (replace {id} with the actual post ID)

Create a new post
Method: POST
URL: http://localhost:8000/posts
Body: JSON

Update a post by ID
Method: PUT
URL: http://localhost:8000/posts/{id} (replace {id} with the actual post ID)
Body: JSON

Delete a post by ID
Method: DELETE
URL: http://localhost:8000/posts/{id} (replace {id} with the actual post ID)

Search posts
Method: GET
URL: http://localhost:8000/posts/search
Query Params:
query: The search query string.
skip (optional): The starting index for pagination (default is 0).
limit (optional): The number of posts to return (default is 10).

### Clone the Repository

```sh
git clone https://github.com/yourusername/blog-api.git
cd blog-api
