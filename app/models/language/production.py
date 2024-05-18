from .token import Token
from .pattern import Pattern


class Production:
    """Class Production is used to link patterns."""

    def __init__(self, main_token: Token, patterns: list[Pattern] = []) -> None:
        self._main_token: Token = main_token
        self._patterns: list[Pattern] = patterns

    def get_first_pattern(self) -> Pattern:
        """Get first pattern from production."""
        return self._patterns[0]

    def add_pattern(self, pattern: Pattern) -> None:
        """Add pattern to production."""
        self._patterns.append(pattern)

    def add_patterns(self, patterns: list[Pattern]) -> None:
        """Add patterns to production."""
        self._patterns.extend(patterns)

    def get_mtoken(self) -> Token:
        """Get token from production."""
        return self._main_token

    def get_patterns(self) -> list[Pattern]:
        """Get patterns from production."""
        return self._patterns

    def set_patterns(self, patterns: list[Pattern]) -> None:
        """Set patterns to production."""
        self._patterns = patterns

    def include_token(self, token: Token) -> bool:
        """Check if production includes token."""
        for pattern in self._patterns:
            for iter_token in pattern.get_tokens():
                eq_lexemas: bool = iter_token.get_lexema() == token.get_lexema()
                are_terminals: bool = iter_token.is_terminal() == token.is_terminal()
                if eq_lexemas and are_terminals:
                    return True
        return False

    def remove_pattern(self, pattern: Pattern) -> None:
        """Remove pattern from production."""
        self._patterns.remove(pattern)

    def remove_patterns(self) -> None:
        """Remove pattern from production."""
        self._patterns = []

    def discard_pattern(self, pattern: Pattern) -> Pattern | None:
        """Discard pattern from production."""
        for idx, iter_pattern in enumerate(self._patterns):
            if iter_pattern == pattern:
                return self._patterns.pop(idx)

    def eq_mtoken(self, token: Token) -> bool:
        """Function to check if two tokens are equal."""
        eq_lexemas: bool = token.get_lexema() == self._main_token.get_lexema()
        are_terminals: bool = token.is_terminal() == self._main_token.is_terminal()
        return eq_lexemas #and are_terminals

    def is_recursive(self) -> bool:
        """Function to check if production is recursive."""
        for pattern in self._patterns:
            if self._main_token.get_lexema() == pattern.get_first().get_lexema():
                return True
        return False

    def __str__(self) -> str:
        patts: str = ""
        for pattern in self._patterns:
            patts += f"\n{pattern}"
        return f"『mtoken {self._main_token} | patterns ⟨{patts}⟩』"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Production):

            if len(self._patterns) == len(other.get_patterns()):
                for i, pattern in enumerate(self._patterns):
                    if not pattern.__eq__(other.get_patterns()[i]):
                        return False
                return self.eq_mtoken(other.get_mtoken())

            # return self.eq_mtoken(other.get_mtoken()) and
        return False
