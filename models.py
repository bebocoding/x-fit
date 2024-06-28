class UserData:
    def __init__(self, 
                 gender: str = None,
                 age: int = None,
                 weight: float = None,
                 height: float = None,
                 goal: list = None,
                 experience: str = None,
                 bodyFatPercentage: float = None,
                 muscleMass: float = None,
                 workoutDurationPreference: str = None,
                 workoutFrequencyPreference: str = None,
                 preferredExerciseTypes: list = None,
                 trainingEnvironmentPreference: list = None,
                 healthIssues: list = None):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.experience = experience
        self.bodyFatPercentage = bodyFatPercentage
        self.muscleMass = muscleMass
        self.workoutDurationPreference = workoutDurationPreference
        self.workoutFrequencyPreference = workoutFrequencyPreference
        self.preferredExerciseTypes = preferredExerciseTypes
        self.trainingEnvironmentPreference = trainingEnvironmentPreference
        self.healthIssues = healthIssues