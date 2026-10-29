from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, validate
from models import db, Exercise, Workout, WorkoutExercise


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    reps = fields.Integer(validate=validate.Range(min=1))
    sets = fields.Integer(validate=validate.Range(min=1))
    duration_seconds = fields.Integer(validate=validate.Range(min=1))


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    name = fields.String(
        required=True,
        validate=validate.Length(min=1)
    )

    category = fields.String(
        required=True,
        validate=validate.Length(min=1)
    )

    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True
    )


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        include_relationships = True
        load_instance = True
        sqla_session = db.session

    date = fields.Date(required=True)

    duration_minutes = fields.Integer(
        required=True,
        validate=validate.Range(min=1)
    )

    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True
    )

    exercises = fields.Nested(
        ExerciseSchema,
        many=True
    )


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)