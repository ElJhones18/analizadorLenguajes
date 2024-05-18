from models.language.production import Production


class State:
    """
    Represents a state in an automaton.

    Attributes:
        _name (str): The name of the state.
        _productions (list[Production]): The list of productions associated with the state.
        _is_initial (bool): Indicates whether the state is an initial state.
    """

    def __init__(
        self, name: str, is_initial: bool, productions: list[Production] = []
    ) -> None:
        self._name: str = name
        self._productions: list[Production] = productions
        self._is_initial: bool = is_initial

    def add_production(self, production: Production) -> None:
        """Adds a production to the state."""
        self._productions.append(production)
        
    def has_production(self, production: Production) -> bool:     
        """Checks if the state has a production."""
        return production in self._productions
        
    def add_productions(self, productions: list[Production]) -> None:
        """Adds a list of productions to the state."""
        self._productions.extend(productions)

    def get_name(self) -> str:
        """Returns the name of the state."""
        return self._name

    def get_is_initial(self) -> bool:
        """Returns True if the state is an initial state, False otherwise."""
        return self._is_initial

    def get_productions(self) -> list[Production]:
        """Returns the list of productions associated with the state."""
        return self._productions

    def set_name(self, name: str) -> None:
        """Sets the name of the state."""
        self._name = name

    def set_is_initial(self, is_initial: bool) -> None:
        """Sets whether the state is an initial state."""
        self._is_initial = is_initial

    def set_productions(self, productions: list[Production]) -> None:
        """Sets the list of productions associated with the state."""
        self._productions = productions

    def __str__(self) -> str:
        """Returns a string representation of the State object."""
        productions: str = ""
        for production in self._productions:
            productions += f"{production}\n"
        return f"State: {self._name},\n Initial: {self._is_initial},\n Productions: \n{productions}"
    
    def __eq__(self, other: object) -> bool:
        """Checks if the state is equal to another state."""
        if isinstance(other, State):
            times: int = 0
            if len(self._productions) == len(other.get_productions()):
                for prod in self._productions:
                    for prod2 in other.get_productions():
                        if prod.__eq__(prod2):
                            times += 1
            # print("holiwis" + str(self._is_initial == other._is_initial and times == len(self._productions)))
            return times == len(self._productions)
        return False
