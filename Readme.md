# Flask SQLAlchemy Workout Application Backend

This project is a small Flask REST API for managing workouts, exercises, and the relationship between them.

## Features
- CRUD endpoints for workouts
- CRUD endpoints for exercises
- Linking exercises to workouts through a join table
- Marshmallow-based serialization and validation
- SQLAlchemy models with constraints and validations

## Installation
1. Install dependencies with Pipenv:
   `pipenv install`
2. Activate the environment:
   `pipenv shell`
3. Run the database migrations:
   `flask db upgrade`
4. Seed the database with starter data:
   `python server/seed.py`

## Run the server
From the project root, start the API with:

`python server/app.py`

The API will run on port 5555.

## Main Endpoints
- GET /workouts
- GET /workouts/<id>
- POST /workouts
- DELETE /workouts/<id>
- GET /exercises
- GET /exercises/<id>
- POST /exercises
- DELETE /exercises/<id>
- POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises