# Password Generator Web App

A lightweight web application built with Python and Flask that generates cryptographically secure passwords using Python's `secrets` module. The application is containerized with Docker and configured for automated deployment on cloud platforms such as Render.

## Live Demo

- **URL:** `https://password-generator-web-80i6.onrender.com/?`
- *Note:* Hosted on Render's free tier. If the instance is inactive, the initial request may take ~30–50 seconds to spin up (cold start).

---

## Features

- **Cryptographically Secure:** Uses Python's standard `secrets` library to ensure non-deterministic random generation.
- **Dynamic Port Binding:** Automatically reads the `PORT` environment variable injected by cloud hosts, falling back to port `5000` locally.
- **Cloud-Agnostic Container:** Packaged with `python:3.11-slim` to run on any standard OCI/Docker-compliant platform.
- **Generation Counter (local dev):** Counts generated passwords in Redis. If Redis is not available (e.g. on Render), the counter is simply hidden.

---

## Local Setup and Execution

To run this application locally using Docker, you need [Git](https://git-scm.com/) and [Docker Desktop](https://www.docker.com/) installed.

### 1. Clone the Repository
```bash
git clone https://github.com/AtHelge/password-generator-web.git
```
### 2. Move to the right folder
```bash
cd password-generator-web
```

### 3. Build the Docker Image
```bash
docker build -t password-generator-web .
```

### 4. Run application on port 5000
```bash
docker run -p 5000:5000 password-generator-web
```

---

## Development with Docker Compose

For development, the project includes a `docker-compose.yaml` with two services:

- **web** – built from the Dockerfile. The source code is bind-mounted into the container and Flask runs in debug mode, so code and template changes are live without rebuilding.
- **redis** – stores the generation counter. The app connects via the service name `redis` (`REDIS_HOST=redis`).

Start both services:
```bash
docker compose up
```

Then open http://localhost:5000.

The Dockerfile itself is unchanged and is used for production on Render. The Compose file only adapts it for local development.
