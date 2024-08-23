import pytest
import asyncio
from agent_framework.agent import Agent
from agent_framework.agent_manager import AgentManager

@pytest.mark.asyncio
async def test_agent_message_passing():
    manager = AgentManager()
    agent1 = Agent(agent_id=1, agent_manager=manager)
    agent2 = Agent(agent_id=2, agent_manager=manager)

    manager.register_agent(agent1)
    manager.register_agent(agent2)

    await agent1.send_message(recipient_id=2, content="Test Message")
    await asyncio.sleep(1)  # Wait for message processing

    assert not agent2.message_queue.empty()

@pytest.mark.asyncio
async def test_agent_lifecycle():
    manager = AgentManager()
    agent = Agent(agent_id=1, agent_manager=manager)

    manager.register_agent(agent)
    await agent.run()

    assert agent.is_active
    agent.stop()
    assert not agent.is_active
