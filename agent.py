"""
Course: 02AML204 - Introduction to Artificial Intelligence
Activity: SLE-1 AI Agent Implementation
PRN: 25UAM045
Name: Aniket Mane

Description:
A simple PEAS-based Reflex Vacuum Cleaner Agent operating in a two-room environment (Room A and Room B).
"""

class Environment:
    def __init__(self):
        # Environment state: 'Clean' or 'Dirty'
        self.locations = {'A': 'Dirty', 'B': 'Dirty'}
        self.agent_location = 'A'

    def get_percept(self):
        # Returns current location and condition
        return self.agent_location, self.locations[self.agent_location]

    def execute_action(self, action):
        # Applies agent's chosen action to the environment
        if action == 'Suck':
            self.locations[self.agent_location] = 'Clean'
            print(f"[ACTION] Sucked dirt in Room {self.agent_location}.")
        elif action == 'Right':
            self.agent_location = 'B'
            print("[ACTION] Moved Right to Room B.")
        elif action == 'Left':
            self.agent_location = 'A'
            print("[ACTION] Moved Left to Room A.")
        elif action == 'NoOp':
            print("[ACTION] No operation. Both rooms are clean.")

    def are_all_clean(self):
        return all(status == 'Clean' for status in self.locations.values())


class ReflexVacuumAgent:
    def decide_action(self, location, status):
        # Simple condition-action rule set
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'
        return 'NoOp'


def run_simulation():
    print("=== PEAS Vacuum Cleaner Agent Simulation ===")
    env = Environment()
    agent = ReflexVacuumAgent()
    
    step = 1
    max_steps = 6

    while step <= max_steps:
        loc, status = env.get_percept()
        print(f"\nStep {step}: Agent in Room '{loc}' | Status: '{status}'")
        
        if env.are_all_clean() and status == 'Clean':
            env.execute_action('NoOp')
            print("\nEnvironment is fully cleaned! Goal accomplished.")
            break
            
        action = agent.decide_action(loc, status)
        env.execute_action(action)
        step += 1

if __name__ == "__main__":
    run_simulation()
