from aiCoach import aiCoach
import models
import schemas




from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    userData = models.UserData("lose weight", "beginner", "indoor", "diabetes")
    plan = aiCoach.generatePlan(userData)
    return {"plan": plan}

@app.post("/plan")
async def plan(userData: schemas.UserData):
    userData = models.UserData(goal=userData.Goal, level=userData.Level, 
                               illness=userData.Illness, trainingEnvironmentPreference=userData.trainingEnvironmentPreference)
    plan = aiCoach.generatePlan(userData)
    return {"plan": plan}