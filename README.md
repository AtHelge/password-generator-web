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

## Local Development (Docker)

### 1. Build the Docker Image
```bash
docker build -t password-generator-web .
```

### 2. Run application on port 5000
```bash
docker run -p 5000:5000 password-generator-web
```