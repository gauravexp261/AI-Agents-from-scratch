from memory.memory import Memory

class SummarizationMemory(Memory):
    """A memory module that summarizes conversation history after assistant responses."""
    
    def __init__(self, llm):
        super().__init__()
        self.llm = llm

    def add(self, role:str, content:str, tool_call:dict | None =None, **kwargs) -> None:
        """Add a message to memory and summarize if necessary."""
        super().add(role, content, tool_call, **kwargs)
        if role == 'assistant':
            summary = ""
            conversation = ""
            for message in self.messages:
                if message['role'] == "system":
                    summary = message['content']   
                else:
                    conversation += f"{message['role']}: {message['content']}\n"
            prompt = f"""You maintain a persistent summary of a conversation. 
            Your job is to create an UPDATED summary. 
            IMPORTANT RULES: 
            1. Preserve all important information from the existing summary. 
            2. Add important information from the new conversation. 
            3. NEVER remove an existing fact unless the new conversation explicitly corrects or contradicts it. 
            4. Keep the summary concise. 
            5. Do not copy the entire conversation. 
            6. Output ONLY the updated summary.
                    Summary: {summary}

                    Conversation:
                    {conversation}
                    UPDATED SUMMARY:"""
            response = self.llm.generate([{"role": "user", "content": prompt}])
            self.messages = [{"role": "system", "content": response.content}]

  