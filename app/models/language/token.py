class Token:
    """Class Variable is used to determine grammars."""

    def __init__(self, lexema: str, is_terminal: bool) -> None:
        self._lexema = lexema  # A
        self._is_terminal = is_terminal  # False

    def get_lexema(self) -> str:
        """Get lexema."""
        return self._lexema

    def set_lexema(self, lexema: str) -> None:
        """Set lexema."""
        self._lexema = lexema

    def get_lexema2(self) -> str:
        """Get lexema."""
        if self.get_lexema() == "λ":
            return ""
        else:
            return self._lexema

    def is_terminal(self) -> bool:
        """Get is_terminal."""
        return self._is_terminal

    def __str__(self) -> str:
        return f"{self._lexema} ; {self._is_terminal}"

    def __eq__(self, value: object) -> bool:
        return (
            self._lexema == value.get_lexema()
        )  # and self._is_terminal == value.is_terminal()
