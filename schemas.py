from typing import List, Optional
from pydantic import BaseModel, conlist

class UserData(BaseModel):
    gender: Optional[str] = None
    age: Optional[int] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    goal: Optional[List[str]] = None
    experience: Optional[str] = None
    bodyFatPercentage: Optional[float] = None
    muscleMass: Optional[float] = None
    workoutDurationPreference: Optional[str] = None
    workoutFrequencyPreference: Optional[str] = None
    preferredExerciseTypes: Optional[List[str]] = None
    trainingEnvironmentPreference: Optional[List[str]] = None
    healthIssues: Optional[List[str]] = None

