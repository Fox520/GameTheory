DISCOUNT = 0.5
import copy

class State:
    def __init__(self, reward, name, transitions=None):
        self.reward = reward
        self.utility_value = 0.0
        self.transitions = transitions
        self.previous_utility_value = None
        self.name = name


def quick_add(transitions):
    total = 0
    for t in transitions:
        total += t[0] * t[1].utility_value
    return total


def get_max(transitions):
    away: tuple = transitions[0]
    others: list = transitions[1:]

    aval = away[0] * away[1].utility_value
    oval = quick_add(others)
    return max(aval, oval)


S1 = State(3, "S1")
S2 = State(-1, "S2")
S1.transitions = [(1.0, S2), (0.5, S1), (0.5, S2)]
S2.transitions = [(1.0, S1), (1.0, S2)]
states = [S1, S2]

def value_iteration():
    for state in states:
        while state.previous_utility_value != state.utility_value:
            
            # state = copy.deepcopy(s)
            # print(state.name)
            # if state.previous_utility_value == None:
            #     state.previous_utility_value = state.utility_value
            # Update utility value/ Bellman update
            state.previous_utility_value = state.utility_value
            state.utility_value = state.reward + DISCOUNT * get_max(state.transitions)

            # Check if optimal
        # if state.utility_value == state.previous_utility_value:
        #     print(state.name, state.utility_value, "is optimal")
        #     break
        # print(state.utility_value, state.previous_utility_value)
        
value_iteration()
print(states[0].utility_value, states[1].utility_value)
