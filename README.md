# Agent Framework

This is a simple Python agent framework that supports basic message passing, concurrency, and task management. The framework is modular, scalable, and can be extended to include more advanced features like decentralized communication, state persistence, and more.

## Features

- **Multithreaded/Async Agents:** Agents run concurrently, allowing parallel operations.
- **Message Passing:** Agents can communicate with each other through message queues.
- **Task Scheduling:** Supports basic task execution with room for advanced scheduling.
- **State Persistence:** Agent states can be persisted using SQLite.

## Getting Started

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/agent-framework.git
    cd agent-framework
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the example:
    ```bash
    python examples/basic_example.py
    ```

## Usage

The core components of the framework are:

- **Agent:** The basic unit that performs tasks and communicates with other agents.
- **AgentManager:** Manages agent registration and message dispatching.
- **Message:** A message object used for communication between agents.
- **Task:** A simple task class that can be extended for more complex scheduling.

### Example

Check out the `examples/` directory for a basic implementation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
