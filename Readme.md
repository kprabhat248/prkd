# FastAPI Student CRUD API with Ollama Integration

This project is a simple REST API built with Python and FastAPI that performs CRUD (Create, Read, Update, Delete) operations on a list of students. It also integrates with a local Ollama instance to generate AI-based summaries for student profiles.

## Features

-   **CRUD Operations:** Full support for creating, reading, updating, and deleting students.
-   **In-Memory Storage:** Uses a simple Python dictionary for data storage (no database required).
-   **AI Integration:** Generates student summaries using the Llama3 model via Ollama.
-   **Containerized:** Fully containerized with Docker and Docker Compose for easy setup and deployment.
-   **Structured Code:** Follows a clean, refactored project structure for maintainability.

## Prerequisites

1.  **Docker and Docker Compose:** [Install Docker](https://docs.docker.com/get-docker/).
2.  **Ollama:** [Install Ollama](https://ollama.com/download).
3.  **Llama3 Model:** After installing Ollama, pull the Llama3 model:
    ```bash
    ollama pull llama3
    ```

## How to Run

1.  **Start the Ollama Application:** Make sure the Ollama application is running on your host machine.

2.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd <your-repo-directory>
    ```

3.  **Build and Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4.  **The API is ready!** The server will be running at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

## Testing Endpoints with cURL

**Create a Student:**
```bash
curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"name": "Alice", "age": 22, "email": "alice@example.com"}'