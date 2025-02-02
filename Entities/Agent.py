from typing import List
import random
import string
from faker import Faker

# Agent Class
class Agent:
    def __init__(self, agent_id: int, name: str, assigned_properties: List[int]):
        self.agent_id = agent_id
        self.name = name
        self.assigned_properties = assigned_properties

    def __str__(self):
        return f"Agent ID: {self.agent_id}\n" \
               f"Name: {self.name}\n" \
               f"Assigned Properties: {', '.join(map(str, self.assigned_properties))}"
    
    def create_random_agents(num_agents: int):
        agents = []
        fake = Faker()
        
        for agent_id in range(1, num_agents + 1):
            # Generate a random name (5 characters long, uppercase letters)
            name = fake.name()
            
            # Assign 10 properties based on agent_id (1-10 for agent 1, 11-20 for agent 2, etc.)
            assigned_properties = list(range((agent_id - 1) * 10 + 1, agent_id * 10 + 1))
            
            # Create and append the new agent
            agents.append(Agent(agent_id, name, assigned_properties))

        return agents


