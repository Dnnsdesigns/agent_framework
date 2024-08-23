import asyncio
from agent_framework.message import Message

class Agent:
    def __init__(self, agent_id, agent_manager):
        self.agent_id = agent_id
        self.manager = agent_manager
        self.message_queue = asyncio.Queue()
        self.is_active = True

    async def send_message(self, recipient_id, content):
        message = Message(sender_id=self.agent_id, recipient_id=recipient_id, content=content)
        await self.manager.dispatch_message(message)

    async def receive_message(self):
        while self.is_active:
            message = await self.message_queue.get()
            await self.process_message(message)

    async def process_message(self, message):
        print(f"Agent {self.agent_id} received message from Agent {message.sender_id}: {message.content}")

    async def run(self):
        print(f"Agent {self.agent_id} started.")
        await self.receive_message()

    def stop(self):
        self.is_active = False
        print(f"Agent {self.agent_id} stopped.")
