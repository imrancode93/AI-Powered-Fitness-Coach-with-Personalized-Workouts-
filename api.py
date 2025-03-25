from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_user, add_user, save_workout
from workout_generator import generate_workout
from logger import log_message

app = FastAPI()

# ----------- Pydantic Schema -----------
class UserRequest(BaseModel):
    name: str
    age: int
    fitness_level: str
    goal: str
    equipment: str

# ----------- Root -----------
@app.get("/")
def root():
    return {"message": "Welcome to the AI Fitness Coach API!"}

# ----------- Register User -----------
@app.post("/user")
def register_user(user: UserRequest):
    if get_user(user.name):
        raise HTTPException(status_code=400, detail="User already exists")
    
    add_user(
        name=user.name,
        age=user.age,
        fitness_level=user.fitness_level,
        goal=user.goal,
        equipment=user.equipment
    )
    return {"message": f"User '{user.name}' registered successfully!"}

# ----------- Generate Workout -----------
@app.get("/workout/{username}")
def get_user_workout(username: str):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    workout = generate_workout(
        fitness_level=user.fitness_level,
        goal=user.goal,
        duration="30",
        equipment=user.equipment
    )

    save_workout(user_id=user.id, workout_plan=workout)

    return {
        "username": user.name,
        "goal": user.goal,
        "fitness_level": user.fitness_level,
        "equipment": user.equipment,
        "workout_plan": workout
    }

log_message("✅ FastAPI server ready.")
