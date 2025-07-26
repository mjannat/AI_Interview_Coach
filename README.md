# AI Interview Coach – Odoo 17 Dockerized Setup

This project provides a ready-to-use Docker Compose setup for running Odoo 17 with a PostgreSQL 15 backend and your custom AI Interview Coach module.

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Quick Start

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd AI_Interview_Coach
   ```

2. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```
   POSTGRES_USER=odoo
   POSTGRES_PASSWORD=1234
   ODOO_ENV=production
   ```

3. **Check your `odoo.conf`:**
   Make sure it contains:
   ```
   [options]
   admin_passwd = 1234
   db_host = db
   db_port = 5432
   db_user = odoo
   db_password = 1234
   addons_path = /mnt/extra-addons/ai_interview_coach
   ```

4. **Build and start the containers:**
   ```sh
   docker compose -f aic-docker-compose.yml up -d --build
   ```

5. **Access Odoo:**
   Open [http://localhost:8069](http://localhost:8069) in your browser.

---

## Common Issues

- **Database connection errors:**  
  Ensure `db_host = db` in `odoo.conf` and that your `.env` and Compose file use the same credentials.

- **Password authentication failed:**  
  If you change the database password, run:
  ```sh
  docker compose -f aic-docker-compose.yml down -v
  docker compose -f aic-docker-compose.yml up -d
  ```
  to reset the database volume.

- **Network not found:**  
  If you see a network error, create it with:
  ```sh
  docker network create mime-connect-docker-net
  ```

---

## Useful Commands

- View logs:
  ```sh
  docker logs odoo17_web
  docker logs odoo_postgres_17_db
  ```
- Stop and remove containers:
  ```sh
  docker compose -f aic-docker-compose.yml down
  ```
- Remove containers and volumes:
  ```sh
  docker compose -f aic-docker-compose.yml down -v
  ```

---

## Project Structure

```
.
├── ai_interview_coach/        # Your custom Odoo module
├── odoo.conf                 # Odoo configuration file
├── Dockerfile                # Custom Odoo Dockerfile
├── aic-docker-compose.yml    # Docker Compose file
├── .env                      # Environment variables
└── README.md                 # This file
```

