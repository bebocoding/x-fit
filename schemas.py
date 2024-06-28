from fastapi import FastAPI
from pydantic import BaseModel


class UserData(BaseModel):
    Level: str | None = None
    Goal: str | None = None
    trainingEnvironmentPreference: str | None = None
    Illness: str | None = None