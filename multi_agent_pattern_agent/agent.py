import os
from openai import OpenAI
from typing import Optional, List
from .tool import Tool

class Agent:
    """
    Represents a specialized AI agent in a collaborative crew.
    """
    def __init__(
        self,
        role: str,
        goal: str,
        backstory: str,
        tools: Optional[List[Tool]] = None,
        model: str = "gpt-4o", # Using a more advanced model for better collaboration
    ):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = {tool.name: tool for tool in tools} if tools else {}
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def run(self, context: str) -> str:
        """
        Executes the agent's main task based on the given context.
        This is a simple implementation; more complex agents might use the ReAct pattern here.
        """
        system_prompt = f"""
        You are an expert AI agent.
        Your Role: {self.role}
        Your Goal: {self.goal}
        Your Backstory: {self.backstory}

        You must focus solely on your goal and role. Do not perform tasks that are outside your scope.
        """
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context},
        ]

        print(f"--- Executing Agent: {self.role} ---")
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during agent execution: {e}"