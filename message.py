from datetime import datetime

class Message:
    def __init__(self, sender_id, recipient_id, content, message_type='info', priority=1):
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.timestamp = datetime.now()
        self.message_type = message_type
        self.priority = priority

    def __str__(self):
        return f"[{self.timestamp}] {self.sender_id} -> {self.recipient_id}: {self.content} (Type: {self.message_type}, Priority: {self.priority})"
