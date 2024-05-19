from models.automaton.state import State
from models.automaton.transition import Transition
from typing import Tuple


class Automaton:
    """
    Represents an automaton.

    Attributes:
        states (list[State]): The list of states in the automaton.
        transitions (list[Transition]): The list of transitions in the automaton.
        start (State): The start state of the automaton.
    """

    def __init__(
        self, states: list[State], transitions: list[Transition], start: State
    ):
        self._states: list[State] = states
        self._transitions: list[Transition] = transitions
        self._start: State = start

    def fix_names(self):
        """
        Fix the names of the states in the automaton.
        """
        for i, state in enumerate(self._states):
            state.set_name("I-" + str(i))

    def add_state(self, state: State):
        """
        Add a state to the automaton.
        """
        self._states.append(state)

    def set_initial_state(self, state: State):
        """
        Set the initial state of the automaton.
        """
        self._start = state

    def get_states(self) -> list[State]:
        """
        Get the list of states in the automaton.
        """
        return self._states

    def get_transitions(self) -> list[Transition]:
        """
        Get the list of transitions in the automaton.
        """
        return self._transitions

    def get_start(self) -> State:
        """
        Get the start state of the automaton.
        """
        return self._start

    def set_states(self, states: list[State]):
        """
        Set the list of states in the automaton.
        """
        self._states = states

    def set_transitions(self, transitions: list[Transition]):
        """
        Set the list of transitions in the automaton.
        """
        self._transitions = transitions

    def add_transition(self, transition: Transition):
        """
        Add a transition to the automaton.
        """
        self._transitions.append(transition)

    def has_state(self, state: State) -> Tuple[int, bool]:
        """
        Check if a state is already in the list of states in the automaton.
        """
        for index, existing_state in enumerate(self._states):
            # if existing_state == state:
            if existing_state.__eq__(state):
                return index, True
        return False
