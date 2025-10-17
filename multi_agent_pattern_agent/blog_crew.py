from dotenv import load_dotenv

from .agent import Agent
from .crew import Crew
from .task import Task
from .tools import search_tool

load_dotenv()

def create_blog_writing_crew(topic: str) -> Crew:
    """
    Creates and configures the blog writing crew with agents and tasks.
    """
    # === 1. Define the Agents (The Team) ===

    researcher = Agent(
        role="Senior Research Analyst",
        goal=f"Uncover compelling and factual information on the topic: {topic}",
        backstory="You are a world-class research analyst, known for your ability to dig deep and find the most relevant and up-to-date information on any subject. You are a master of web search.",
        tools=[search_tool] # The Researcher is the only one with a tool
    )

    writer = Agent(
        role="Professional Content Writer",
        goal=f"Write an engaging, well-structured, and insightful blog post on the topic: {topic}",
        backstory="You are a renowned content writer, famous for your clear, concise, and captivating writing style. You can transform complex research into easy-to-understand narratives."
    )

    critic = Agent(
        role="Expert Writing Critic",
        goal="Provide constructive feedback on a blog post, identifying areas for improvement.",
        backstory="You are a sharp-eyed editor and critic with a keen sense of what makes content great. You provide clear, actionable feedback to elevate a piece of writing from good to excellent."
    )


    # === 2. Define the Tasks (The Workflow) ===

    research_task = Task(
        role="Senior Research Analyst",
        description=f"Conduct comprehensive research on {topic}. Find at least 3 key facts or recent developments. The final output should be a bullet-point list of your findings."
    )

    writing_task = Task(
        role="Professional Content Writer",
        description="Based on the research provided, write a blog post of about 3-4 paragraphs. The post should be engaging and well-structured."
    )

    critique_task = Task(
        role="Expert Writing Critic",
        description="Review the blog post draft. Provide a bullet-point list of suggestions for improvement, focusing on clarity, engagement, and accuracy. If the post is perfect, say so."
    )


    # === 3. Assemble the Crew ===

    blog_crew = Crew(
        agents=[researcher, writer, critic],
        tasks=[research_task, writing_task, critique_task]
    )

    return blog_crew


# --- Main execution block to test the crew ---
if __name__ == "__main__":
    topic_to_research = "The future of AI agents"
    crew = create_blog_writing_crew(topic_to_research)
    
    print(f"=== Starting Blog Writing Crew for topic: '{topic_to_research}' ===")
    final_result = crew.run()
    
    print("\n\n=== Crew Run Complete ===")
    print("Final Result:")
    print(final_result)