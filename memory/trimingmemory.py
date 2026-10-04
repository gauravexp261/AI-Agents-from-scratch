from memory.memory import Memory

class TrimmingMemory(Memory):
    """A memory module that trims conversation history to a maximum length."""
    
    def __init__(self, max_length:int = 10):
        super().__init__()
        self.max_length = max_length
        
    def add(self, role:str, content:str, tool_call:dict | None =None, **kwargs) -> None:
        """Add a message to memory and trim if necessary."""
        super().add(role, content, tool_call, **kwargs)
        if len(self.messages) > self.max_length:
            self.messages = self.messages[-self.max_length:]