from models.automaton.state import State


class Transition:
    def __init__(self, source: State, target: State, label: str):
        """
        Initializes a new Transition object.

        Args:
            source (State): The source state of the transition.
            target (State): The target state of the transition.
            label (str): The label associated with the transition.
        """
        self.source: State = source
        self.target: State = target
        self.label: str = label

    def get_source(self) -> State:
        """
        Returns the source state of the transition.
        """
        return self.source

    def get_target(self) -> State:
        """
        Returns the target state of the transition.
        """
        return self.target

    def get_label(self) -> str:
        """
        Returns the label associated with the transition.
        """
        return self.label

    def set_source(self, source: State) -> None:
        """
        Sets the source state of the transition.
        """
        self.source = source

    def set_target(self, target: State) -> None:
        """
        Sets the target state of the transition.
        """
        self.target = target

    def set_label(self, label: str) -> None:
        """
        Sets the label associated with the transition.
        """
        self.label = label
