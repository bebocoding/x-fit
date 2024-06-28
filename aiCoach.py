from config import systemMessage

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from tools import tools
from models import *



class AiCoach:
    def __init__(self, systemMessage=systemMessage, tools=tools):
        self.llm_with_tools = ChatGroq(model="llama3-70b-8192", api_key="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", temperature=1).bind_tools(tools=tools, tool_choice="trainingFromJson")
        self.systemMessage = systemMessage

    def generatePlan(self, userData):
        userPrompt = self.generateUserPrompt(userData)
        
        messages = [
            SystemMessage(content=systemMessage),
            HumanMessage(content=userPrompt),
        ]

        aiResponse = self.llm_with_tools.invoke(messages)
        plan = aiResponse.tool_calls[0]['args']
        return plan



    def generateUserPrompt(self, userData:UserData):

        userPrompt = ''
        userPrompt += f"I am a {userData.gender}." if userData.gender else ''
        userPrompt += f"\nMy age is {userData.age}." if userData.age else ''
        userPrompt += f"\nMy height {userData.height} meters." if userData.height else ''
        userPrompt += f"\nMy weight is {userData.weight} kg." if userData.weight else ''
        userPrompt += f"\nMy goal is to {', '.join(userData.goal)}." if userData.goal else ''
        userPrompt += f"\nI am at {userData.bodyFatPercentage}% fat percentage." if userData.bodyFatPercentage else ''
        userPrompt += f"\nMy muscle mass is {userData.muscleMass} kg." if userData.muscleMass else ''
        userPrompt += f"\nI prefer to have a {userData.workoutDurationPreference} min workout." if userData.workoutDurationPreference else ''
        userPrompt += f"\nI prefer to train {userData.workoutFrequencyPreference}." if userData.workoutFrequencyPreference else ''
        userPrompt += f"\nI prefer {', '.join(userData.preferredExerciseTypes)} exercise types." if userData.preferredExerciseTypes else ''
        userPrompt += f"\nI am at {userData.experience} level." if userData.experience else ''
        userPrompt += f"\nI like to workout {', '.join(userData.trainingEnvironmentPreference)}." if userData.trainingEnvironmentPreference else ''
        userPrompt += f"\nI have {', '.join(userData.healthIssues)}." if userData.healthIssues else ''


        return userPrompt
    
aiCoach = AiCoach()


