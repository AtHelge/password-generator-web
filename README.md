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