import asyncio

class AgentManager:
    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.agent_id] = agent

    async def dispatch_message(self, message):
        recipient = self.agents.get(message.recipient_id)
        if recipient:
            await recipient.message_queue.put(message)
        else:
            print(f"Agent {message.recipient_id} not found.")

    async def start_all_agents(self):
        for agent in self.agents.values():
            asyncio.create_task(agent.run())

    def stop_all_agents(self):
        for agent in self.agents.values():
            agent.stop()
