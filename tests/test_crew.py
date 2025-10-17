from unittest.mock import MagicMock
from multi_agent_pattern_agent.agent import Agent
from multi_agent_pattern_agent.crew import Crew
from multi_agent_pattern_agent.task import Task

def test_crew_runs_tasks_sequentially_and_passes_context(mocker):
    """
    Tests that the Crew orchestrates agents in the correct order and
    that the output of one task becomes the input for the next.
    """
    # Arrange
    # 1. Define the sequence of outputs we expect from each agent
    researcher_output = "Fact 1: AI agents are cool. Fact 2: CrewAI is a framework."
    writer_output = "Blog Post Draft: AI agents are very cool. You can use frameworks like CrewAI."
    critic_output = "Critique: The post is good, but could be more detailed."

    # 2. Mock the Agent's run method
    # We are not testing the agents themselves, only the Crew's orchestration.
    # We use side_effect to make the mocked method return different values on each call.
    mock_agent_run = mocker.patch(
        'multi_agent_pattern_agent.agent.Agent.run',
        side_effect=[researcher_output, writer_output, critic_output]
    )

    # 3. Create mock agents and tasks
    # The actual content of the agents doesn't matter, only their roles.
    agents = [
        Agent(role="Researcher", goal="...", backstory="..."),
        Agent(role="Writer", goal="...", backstory="..."),
        Agent(role="Critic", goal="...", backstory="...")
    ]
    tasks = [
        Task(role="Researcher", description="Research the topic"),
        Task(role="Writer", description="Write the blog post"),
        Task(role="Critic", description="Critique the post")
    ]

    crew = Crew(agents=agents, tasks=tasks)

    # Act
    final_result = crew.run()

    # Assert
    # 1. The final result should be the output of the LAST agent in the chain.
    assert final_result == critic_output

    # 2. The Agent.run method should have been called once for each task.
    assert mock_agent_run.call_count == 3

    # 3. (Advanced) Check that the context was passed correctly.
    # The second call to agent.run should have contained the output of the first agent.
    second_call_args = mock_agent_run.call_args_list[1]
    context_for_writer = second_call_args.kwargs['context']
    assert researcher_output in context_for_writer