import asyncio
from agent_framework.agent import Agent
from agent_framework.agent_manager import AgentManager

async def main():
    # Initialize the Agent Manager
    manager = AgentManager()

    # Create and register agents
    agent1 = Agent(agent_id=1, agent_manager=manager)
    agent2 = Agent(agent_id=2, agent_manager=manager)
    manager.register_agent(agent1)
    manager.register_agent(agent2)

    # Start all agents
    await manager.start_all_agents()

    # Send messages between agents
    await agent1.send_message(recipient_id=2, content="Hello from Agent 1!")
    await agent2.send_message(recipient_id=1, content="Hi Agent 1, this is Agent 2!")

    # Allow some time for message processing
    await asyncio.sleep(5)

    # Stop all agents
    manager.stop_all_agents()

if __name__ == "__main__":
    asyncio.run(main())
