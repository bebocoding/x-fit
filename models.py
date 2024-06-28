class UserData:
    def __init__(self, goal: str = None, level: str = None, trainingEnvironmentPreference: str = None, illness: str = None):
        self.goal = goal
        self.level = level
        self.trainingEnvironmentPreference = trainingEnvironmentPreference
        self.illness = illness