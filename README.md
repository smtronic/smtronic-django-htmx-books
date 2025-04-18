# 📚 Django HTMX Books — Dockerized Project

A simple Django app for managing books using **HTMX**, **Memcached**, and multilingual localization. The project is ready for deployment using **Docker**, **Docker Compose**, **Gunicorn**, and **NGINX**.

---

## 📦 Contents

- [🚀 Quick Start (Development)](#-quick-start-development)
- [🌍 Production Setup](#-production-setup)
- [🛠 Management Commands](#-management-commands)
- [📚 About the App](#-about-the-app)
- [📂 Project Structure](#-project-structure)
- [📌 Notes](#-notes)
- [📄 Environment Variables](#-environment-variables)
- [🔧 HTMX in Use](#-htmx-in-use)
- [🌐 Localization](#-localization)
- [🚀 Deployment](#-deployment)

---

## 🚀 Quick Start (Development)

Make sure you have **Docker** and **Docker Compose** installed.

1. **Clone the repository**:

   ```bash
   git clone git@github.com:smtronic/django-htmx-books.git
   cd django-htmx-books
   ```

2. **Copy environment variable files**:

   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your values if needed.

3. **Build and run the containers**:

   ```bash
   docker compose up -d --build
   ```

4. **Apply migrations**:

   ```bash
   docker compose exec web python manage.py migrate --noinput
   ```

5. **Access the app**:

   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🌍 Production Setup

1. **Copy and configure `.env.prod`**:

   ```bash
   cp .env.prod.example .env.prod
   ```

2. **Run production containers**:

   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
   ```

3. **Apply migrations**:

   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml exec web python manage.py migrate --noinput
   ```

4. **Collect static files**:

   ```bash
   docker compose --env-file .env.prod -f docker-compose.prod.yml exec web python manage.py collectstatic --noinput
   ```

---

## 🛠 Management Commands

| Command                                                    | Description                                                 |
| ---------------------------------------------------------- | ----------------------------------------------------------- |
| `docker compose down -v`                                   | Stop and remove containers and volumes (⚠️ deletes DB data) |
| `docker compose logs`                                      | View application logs                                       |
| `docker compose exec web python manage.py createsuperuser` | Create a superuser for admin access                         |

---

## 📚 About the App

- Implements **CRUD** for books using **HTMX**.
- Caching is handled via **Memcached** for book lists and sorting.
- Supports localization: **English (en)** and **Russian (ru)**.
- Partial rendering with HTMX: list, create form, detail, update, delete.
- Production uses **Gunicorn** + **NGINX**.

---

## 📂 Project Structure

```plaintext
.
├── docker-compose.yml               # Dev Docker Compose
├── docker-compose.prod.yml          # Production Docker Compose
├── nginx/
│   ├── Dockerfile
│   └── htmx_book.conf               # NGINX config
├── app/
│   ├── Dockerfile
│   ├── Dockerfile.prod
│   ├── manage.py
│   ├── entrypoint.prod.sh
│   ├── books/                       # Book app
│   ├── django_htmx/                 # Main Django project
│   ├── templates/                   # Base and partial templates
│   ├── static/                      # Static files
│   ├── locale/                      # Translations
│   └── requirements.txt
```

---

## 📌 Notes

- The app uses [`.env`](.env) files for environment variables.
- Languages are managed using `LOCALE_PATHS`.
- Cache is configured via `django.core.cache.cache` and manually invalidated.
- Dev mode uses **debug_toolbar** and **rosetta**.
- Production uses **Gunicorn** served by **NGINX**.

---

## 📄 Environment Variables

This project uses two environment files:

| File                     | Used for    | Description                             |
| ------------------------ | ----------- | --------------------------------------- |
| [`.env`](.env)           | Development | Local dev configuration                 |
| [`.env.prod`](.env.prod) | Production  | Real secrets, production cache settings |

These files must **not** be committed to Git. Instead, provide examples:

```bash
cp .env.example .env
cp .env.prod.example .env.prod
```

Update them with your own values.

---

## 🔧 HTMX in Use

HTMX is used to dynamically update parts of the page (no full reload):

- Book list is refreshed after add/delete.
- Book rows can be edited in place.
- Sorting works asynchronously.

---

## 🌐 Localization

Supported languages:

- **English (en)**
- **Russian (ru)**

To add a new language:

```bash
django-admin makemessages -l <language_code>
django-admin compilemessages
```

---

## 🚀 Deployment

This project can be deployed to any VPS or PaaS (e.g., Render, DigitalOcean).

### Steps:

1. Configure your [`.env.prod`](.env.prod) with real values.
2. Use [`docker-compose.prod.yml`](docker-compose.prod.yml) to run the app.
3. Optionally set up **SSL**, domains, and external DB storage.

---

If you have any questions or suggestions, feel free to open an issue or PR!
# New change
