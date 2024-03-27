from models.token import Token
from models.pattern import Pattern


class Production:
    ''' Class Production is used to link patterns. '''

    def __init__(self, main_token: Token, patterns: list[Pattern] = []) -> None:
        self._main_token: Token = main_token
        self._patterns: list[Pattern] = patterns

    def add_pattern(self, pattern: Pattern) -> None:
        ''' Add pattern to production. '''
        self._patterns.append(pattern)

    def add_patterns(self, patterns: list[Pattern]) -> None:
        ''' Add patterns to production. '''
        self._patterns.extend(patterns)

    def get_mtoken(self) -> Token:
        ''' Get token from production. '''
        return self._main_token

    def get_patterns(self) -> list[Pattern]:
        ''' Get patterns from production. '''
        return self._patterns

    def set_patterns(self, patterns: list[Pattern]) -> None:
        ''' Set patterns to production. '''
        self._patterns = patterns

    def include_token(self, token: Token) -> bool:
        ''' Check if production includes token. '''
        for pattern in self._patterns:
            for iter_token in pattern.get_tokens():
                eq_lexemas: bool = iter_token.get_lexema() == token.get_lexema()
                are_terminals: bool = iter_token.is_terminal() == token.is_terminal()
                if eq_lexemas and are_terminals:
                    return True
        return False

    def eq_mtoken(self, token: Token) -> bool:
        ''' Function to check if two tokens are equal. '''
        eq_lexemas: bool = token.get_lexema()\
            == self._main_token.get_lexema()
        are_terminals: bool = token.is_terminal()\
            == self._main_token.is_terminal()
        return eq_lexemas and are_terminals

    def __str__(self) -> str:
        patts: str = ''
        for pattern in self._patterns:
            patts += f'\n{pattern}'
        return (
            f'『mtoken {self._main_token} | patterns ⟨{patts}⟩』'
        )
