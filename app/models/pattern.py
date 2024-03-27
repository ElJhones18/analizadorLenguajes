from models.token import Token


class Pattern:
    ''' Class Pattern is used to group token. '''

    def __init__(self, tokens: list[Token] = []) -> None:
        self._tokens: list[Token] = tokens

    def add_token(self, token: Token) -> None:
        ''' Add token to pattern. '''
        self._tokens.append(token)

    def get_tokens(self) -> list[Token]:
        ''' Get tokens from pattern. '''
        return self._tokens

    def get_token(self, lexema: str) -> Token | None:
        ''' Get token from pattern. '''
        for token in self._tokens:
            if token.get_lexema() == lexema:
                return token
        return None

    def next_token(self, token: Token) -> Token | None:
        ''' Get next token from pattern. '''
        idx: int | None = self.get_token_index(token)
        if idx is None:
            return None
        if idx + 1 >= len(self._tokens):
            return None
        return self._tokens[idx + 1]

    def get_token_index(self, token: Token) -> int | None:
        ''' Locate token from pattern. '''
        for idx, iter_token in enumerate(self._tokens):
            eq_lexemas: bool = iter_token.get_lexema() == token.get_lexema()
            are_terminals: bool = iter_token.is_terminal() == token.is_terminal()
            if eq_lexemas and are_terminals:
                return idx
        return None

    def includes_token(self, token: Token) -> bool:
        ''' Function to check if a pattern includes one token. '''
        for iter_token in self._tokens:
            eq_lexemas: bool = iter_token.get_lexema() == token.get_lexema()
            are_terminals: bool = iter_token.is_terminal() == token.is_terminal()
            if eq_lexemas and are_terminals:
                return True
        return False

    def get_first(self) -> Token:
        ''' Get first token from pattern. '''
        return self._tokens[0]

    def eq_token(self, token_a: Token, token_b: Token) -> bool:
        ''' Function to check if two tokens are equal. '''
        eq_lexemas: bool = token_a.get_lexema()\
            == token_b.get_lexema()
        are_terminals: bool = token_a.is_terminal()\
            == token_b.is_terminal()
        return eq_lexemas and are_terminals

    def __str__(self) -> str:
        tks: str = ''
        for token in self._tokens:
            tks += f'\n{token}'
        return f'[pattern: {tks}\n]'
