# Movie Review Django Rest Framework API

This Django project serves as an assignment showcasing my skills in building a Movie Review API using Django Rest Framework and generic class-based views.

## Overview

The Movie Review project is designed to demonstrate proficiency in Django Rest Framework development, specifically leveraging generic class-based views for efficient and maintainable API code.

## Features

- CRUD (Create, Read, Update, Delete) operations for movies and reviews.
- Generic class-based views for handling common patterns.
- Filtering movies by name and release date.
- Filtering reviews by reviewer name.
- Easy-to-use API endpoints for interacting with the application.

## Project Structure

- **movie_review_app:** Django app containing models, serializers, views, and URLs.
  - `models.py`: Defines the Movie and Review models.
  - `serializers.py`: Contains serializers for Movie and Review models.
  - `views.py`: Implements generic class-based views for CRUD operations.
  - `urls.py`: Maps URLs to views.

## How to Run the Project

1. Ensure you have Python and Django installed.
2. Clone the repository.
3. Create and activate a virtual environment.
4. Install project dependencies: `pip install -r requirements.txt`.
5. Apply database migrations: `python manage.py migrate`.
6. Run the development server: `python manage.py runserver`.
7. Access the application at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **Movies:**
  - List/Create: `/api/movies/`
  - Retrieve/Update/Delete: `/api/movies/<int:pk>/`

- **Reviews:**
  - List/Create: `/api/reviews/`
  - Retrieve/Update/Delete: `/api/reviews/<int:pk>/`

## Usage

- Use your preferred API client (e.g., curl, Postman) to interact with the provided endpoints.
- Perform CRUD operations on movies and reviews.
- Apply filters for more specific queries (e.g., `/api/movies/?name=Inception`).

## Dependencies

- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Django Rest Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- Django Filters: [https://django-filter.readthedocs.io/](https://django-filter.readthedocs.io/)


