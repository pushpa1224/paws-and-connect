# Paws-And-Connect

A Django web application for browsing and adopting pets.

## Features

- Browse available pets with search and filter
- Pet detail pages with full information
- Submit adoption requests (login required)
- User dashboard to track adoption request statuses
- Admin panel for managing pets and adoption requests
- REST API with Token Authentication
- Favorite pets functionality
- Pagination on pet listing and API

## Setup Instructions

1. Clone the repository:
```
git clone <repo-url>
cd Paws-And-Connect
```

2. Create and activate virtual environment:
```
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Apply migrations:
```
python manage.py migrate
```

5. Create a superuser for admin access:
```
python manage.py createsuperuser
```

6. Run the development server:
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser.

## Admin Panel

Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## REST API Endpoints

### Authentication
- `POST /api/auth/token/` — Obtain auth token

### Pets
- `GET /api/pets/` — List all pets
- `GET /api/pets/?search=golden` — Search pets
- `GET /api/pets/?animal_type=Dog&gender=Male` — Filter pets
- `GET /api/pets/<id>/` — Retrieve a pet
- `POST /api/pets/` — Create pet (admin only)
- `PUT /api/pets/<id>/` — Update pet (admin only)
- `DELETE /api/pets/<id>/` — Delete pet (admin only)

### Adoptions
- `GET /api/adoptions/` — List your adoption requests
- `POST /api/adoptions/` — Submit an adoption request
- `GET /api/adoptions/<id>/` — Retrieve a request
- `PUT /api/adoptions/<id>/` — Update a request

## Requirements

See `requirements.txt`.
