from llm import LLM
from trajectory import Trajectory
import memory

class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self,llm:LLM):
        self.llm = llm
        self.memory = memory  # Chapter 4: Add Memory
        self.tools = None  # Chapter 5: Add Tools
        self.planner = None  # Chapter 6: Add Planning
        self.trajectory = Trajectory()

    def run(self, messages: list[dict]) -> str:
        """Run the agent on a task."""
        self.trajectory.initialize(query=messages[-1]["content"])
        return self._step(messages)

    def _step(self,  messages: list[dict]) -> str:
        """Perform a single step."""
        # Placeholder - will be implemented in later chapters
        response = self.llm.generate(messages)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""
        # Placeholder - will be implemented in later chapters
        return f"Executed action: {action}"
    
 
# gemma3:12b 
# gemma4:lates


messages = [
    {"role": "system", "content": "You are helpful assistant"},
    {"role": "user", "content": "What is 2+2 and how many stars are rhere"},
]

if __name__ == "__main__":
    agent = TinyAgent(llm=LLM(model="gemma4:latest",temperature= 0))
    response = agent.run(messages)
    print("ANSWER:")
    print(response)
    print("==================")
    print("==================")
    print("\nTRAJECTORY:")
    print(agent.trajectory.runs)