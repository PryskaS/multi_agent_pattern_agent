# Multi-Agent Crew Service 🤖🤝📝

[![Code Quality and Tests](https://github.com/PRYSKAS/multi_agent_pattern_agent/actions/workflows/ci.yml/badge.svg)](https://github.com/PRYSKAS/multi_agent_pattern_agent/actions)

An AI microservice that implements the **Multi-Agent Collaboration** pattern. This system orchestrates a crew of specialized AI agents, each with a distinct role and set of tools, to collaboratively solve complex problems, such as writing a comprehensive blog post from a single topic.

This project represents the synthesis of multiple agentic design patterns (Tool Use, Reflection) into a distributed system architecture.

## 🧠 Core Concept: The Agentic Organization

Instead of a single, monolithic "do-it-all" agent, this architecture is built on the principle of specialization, creating a digital team:

1.  **Specialized Agents:** Each `Agent` is configured with a persona (role, goal, backstory) and tools specific to its function (e.g., a Researcher with access to search tools).
2.  **Defined Tasks:** Each `Task` defines a clear objective to be executed by an agent with the corresponding role.
3.  **Orchestration (The `Crew`):** The `Crew` class acts as a project manager. It executes tasks in a defined sequence, passing the output of one agent as the context for the next, ensuring a cohesive and collaborative workflow.

This model transforms problem-solving from a monolithic task into a pipeline of specialists, mirroring how high-performance human teams operate.

## 🚀 Engineering & AI System Design Highlights

This project demonstrates the ability to design and build complex, distributed AI systems.

* **Microservice Architecture for AI:** The system is designed with a clear separation of concerns (`Agent`, `Task`, `Crew`), making it modular, testable, and easily extensible.
* **Inter-Agent Data Pipeline:** The `Crew` manages a data pipeline where the output of one agent becomes the input for the next, enabling the incremental construction of a complex solution.
* **Synthesis of Patterns:** The project combines multiple patterns: the **Researcher** acts as a `ToolAgent`, while the **Critic** applies principles from the `ReflectionAgent`.
* **Infrastructure as a Pattern:** The entire engineering foundation (`FastAPI`, `Docker`, `Pytest`, `GitHub Actions`) was reused, proving the effectiveness of our "agent factory" and allowing for a singular focus on the AI logic.

## 🏗️ The Crew's Workflow

This project implements the key phases of an MLOps pipeline for custom model creation:

```mermaid
graph TD
    subgraph "Início do Processo"
        A[User Input: Blog Topic] --> B(FastAPI Endpoint /generate);
    end

    subgraph "Crew Orchestration"
        B --> C{Orchestrator Agent (Crew)};
        C -- Assigns Task --> D[Agent: Research Manager];
        D -- Uses Tool --> E[Tool: Internet Search];
        E --> D;
        D -- Output --> F[Agent: Content Creator];
        F -- Output --> G[Agent: SEO Expert];
        G -- Output --> H[Agent: Critic/Editor];
        H -- Feedback/Refines --> F;
        H -- Final Output --> I[Final Blog Post];
    end

    subgraph "Fim do Processo"
        I --> B;
        B --> J[User Output: JSON Response];
    end
```

## 🏁 Getting Started

### Prerequisites

* Git
* Python 3.9+
* Docker Desktop (running)
* An OpenAI API Key (required for LLM calls and tool usage)
* A Serper API Key (for internet search tool, required for the Researcher Agent)

### 1. Setup Environment and API Keys

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PRYSKAS/multi_agent_pattern_agent.git](https://github.com/PRYSKAS/multi_agent_pattern_agent.git)
    cd multi_agent_pattern_agent
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure environment variables:**
    * Create a `.env` file from the example: `copy .env.example .env` (on Windows) or `cp .env.example .env` (on Unix/macOS).
    * Add your `OPENAI_API_KEY` and `SERPER_API_KEY` to the new `.env` file. These are crucial for the agents to function.

### 2. Running the Multi-Agent Service

1.  **Run locally using Uvicorn (for development):**
    ```bash
    uvicorn serving.main:app --reload --port 8001
    ```
    Access the API documentation and interact with the service at `http://127.0.0.1:8001/docs`.

2.  **Run using Docker (Recommended for stable execution):**
    * **Build the Docker image:**
        ```bash
        docker build -t multi-agent-crew-service .
        ```
    * **Run the container:**
        ```bash
        docker run -d -p 8001:8001 --env-file .env --name multi-agent-crew multi-agent-crew-service
        ```
    Access the API at `http://127.0.0.1:8001/docs`.

---

## 📡 API Endpoint

### `POST /generate`

Initiates the multi-agent crew to generate content based on a given topic.

**Request Body:**

```json
{
  "topic": "The future of AI in content creation"
}

### Success Response (200 OK):

{
  "blog_post": "..." // The complete blog post generated by the crew
}
---