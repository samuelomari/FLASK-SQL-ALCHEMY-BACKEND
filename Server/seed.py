from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    pushups = Exercise(name="Push Ups", category="Strength", equipment_needed=False)
    squats = Exercise(name="Squats", category="Strength", equipment_needed=False)
    running = Exercise(name="Running", category="Cardio", equipment_needed=False)

    db.session.add_all([pushups, squats, running])
    db.session.commit()

    workout1 = Workout(
        date=date(2026, 7, 24),
        duration_minutes=45,
        notes="Morning workout"
    )

    workout2 = Workout(
        date=date(2026, 7, 25),
        duration_minutes=30,
        notes="Evening cardio"
    )

    db.session.add_all([workout1, workout2])
    db.session.commit()

    we1 = WorkoutExercise(
        workout=workout1,
        exercise=pushups,
        reps=15,
        sets=3,
        duration_seconds=0
    )

    we2 = WorkoutExercise(
        workout=workout1,
        exercise=squats,
        reps=20,
        sets=3,
        duration_seconds=0
    )

    we3 = WorkoutExercise(
        workout=workout2,
        exercise=running,
        reps=0,
        sets=1,
        duration_seconds=1800
    )

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Database seeded successfully!")