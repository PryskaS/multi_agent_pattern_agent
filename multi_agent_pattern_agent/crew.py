from .agent import Agent
from .task import Task

class Crew:
    """
    Manages a team of agents and orchestrates the execution of tasks.
    """
    def __init__(self, agents: list[Agent], tasks: list[Task]):
        self.agents = agents
        self.tasks = tasks

    def run(self) -> str:
        """
        Executes the tasks sequentially, passing the output of one task
        as the context for the next.
        """
        task_output = "" # Start with an empty context

        # This is a simple sequential pipeline.
        # The output of task_i becomes the input for task_{i+1}.
        for task in self.tasks:
            agent = self._get_agent_for_task(task)
            if not agent:
                return f"Error: No agent found for the role: {task.role}"
            
            # Inject the output of the previous task as context
            context_with_output = task.description + f"\n\nPREVIOUS_TASK_OUTPUT:\n{task_output}"
            
            task_output = agent.run(context=context_with_output)
            print(f"--- Task Output ---\n{task_output}\n--------------------")

        return task_output

    def _get_agent_for_task(self, task: Task) -> Agent | None:
        """Finds the correct agent in the crew to perform a given task."""
        for agent in self.agents:
            if agent.role == task.role:
                return agent
        return None