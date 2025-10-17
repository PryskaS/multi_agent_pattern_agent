from .tool import Tool

def simulated_web_search(query: str) -> str:
    """Simulates a web search for a given query."""
    print(f"--- SIMULATING WEB SEARCH for: '{query}' ---")
    if "AI agents" in query:
        return """
        Recent developments in AI agents show a trend towards autonomous systems
        that can perform multi-step tasks. Frameworks like CrewAI and LangChain
        are popular for orchestrating multi-agent collaboration, enabling specialized
        agents (e.g., researchers, writers) to work together to solve complex problems.
        """
    return "No specific information found for this query."

search_tool = Tool(
    name="web_search",
    description="Searches the web for the most up-to-date information on a given topic.",
    function=simulated_web_search
)