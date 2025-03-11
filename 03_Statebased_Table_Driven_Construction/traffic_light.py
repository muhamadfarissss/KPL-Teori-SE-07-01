from enum import Enum
import time
#automata =>state
class trafficLightState(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

state_transitions = {
    trafficLightState.RED: trafficLightState.GREEN,
    trafficLightState.GREEN: trafficLightState.YELLOW,
    trafficLightState.YELLOW: trafficLightState.RED
}

current_state = trafficLightState.YELLOW
next_state = state_transitions[current_state]
print(next_state) #trafficLightState.RED

state_duration = {
    trafficLightState.RED: 60,
    trafficLightState.GREEN: 60,
    trafficLightState.YELLOW: 5
}
current_state = trafficLightState.RED
while True:
    print(current_state)
    time.sleep = state_duration[current_state]
    current_state = state_transitions[current_state]