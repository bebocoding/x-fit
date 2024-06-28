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
        userPrompt += f"My goal is to {userData.goal}." if userData.goal else ''
        userPrompt += f"\nI am at {userData.level} level." if userData.level else ''
        userPrompt += f"\nI like to workout {userData.trainingEnvironmentPreference}." if userData.trainingEnvironmentPreference else ''
        userPrompt += f"\nI have {userData.illness}." if userData.illness else ''

        print(userPrompt)

        return userPrompt
    
aiCoach = AiCoach()


