from dataclasses import dataclass

@dataclass
class Task:
    """Represents a specific task to be performed by an agent."""
    role: str
    description: str