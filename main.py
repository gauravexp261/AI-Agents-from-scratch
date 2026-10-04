from llm import LLM
from trajectory import Trajectory
from memory.memory import Memory
from memory.trimingmemory import TrimmingMemory
from memory.summarizationmemory import SummarizationMemory

class TinyAgent:
    """A minimal, modular, and educational agent framework."""

    def __init__(self,llm,memory):
        self.llm = llm
        self.memory = memory  # Chapter 4: Add Memory
        self.tools = None  # Chapter 5: Add Tools
        self.planner = None  # Chapter 6: Add Planning
        self.trajectory = Trajectory()

    def run(self, task:str) -> str:
        """Run the agent on a task."""
        self.memory.add("user", task)
        self.trajectory.initialize(task)
        return self._step()

    def _step(self) -> str:
        """Perform a single step."""
        # Placeholder - will be implemented in later chapters
        response = self.llm.generate(self.memory.get_messages())
        self.memory.add("assistant", response.content)
        self.trajectory.add(response)
        return response.content

    def _execute_action(self, action: str) -> str:
        """Execute a tool action."""
        # Placeholder - will be implemented in later chapters
        return f"Executed action: {action}"
    
 
# gemma3:12b 
# gemma4:lates




if __name__ == "__main__":
    memory = SummarizationMemory(LLM(model="gemma4:latest"))
    agent_with_memory = TinyAgent(LLM(model="gemma4:latest"), memory=memory)
    response_1 = agent_with_memory.run("Hi! my name is gaurav")
    response_2 = agent_with_memory.run("how is it going")
    response_3 = agent_with_memory.run("what is 4-40")
    response_4 = agent_with_memory.run("what is my name")
    print(agent_with_memory.memory.get_messages())
    print()
    print()
    print(agent_with_memory.trajectory.runs)