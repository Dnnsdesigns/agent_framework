class Task:
    def __init__(self, task_id, description, callback):
        self.task_id = task_id
        self.description = description
        self.callback = callback

    async def execute(self):
        print(f"Executing task: {self.description}")
        await self.callback()
