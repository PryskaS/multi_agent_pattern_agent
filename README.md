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
... (You can include the Mermaid diagram from the Portuguese version here) ...

## 🏁 Getting Started
... (The "Getting Started" and "API Endpoint" sections can be adapted from the previous READMEs as the process is identical) ...
---