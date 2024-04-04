class Token:
    ''' Class Variable is used to determine grammars. '''

    def __init__(self, lexema: str, is_terminal: bool) -> None:
        self._lexema = lexema  # A
        self._is_terminal = is_terminal  # False

    def get_lexema(self) -> str:
        ''' Get lexema. '''
        return self._lexema
    
    def get_lexema2(self) -> str:
        ''' Get lexema. '''
        if self.get_lexema() == "λ":
            return ""
        else:
            return self._lexema

    def is_terminal(self) -> bool:
        ''' Get is_terminal. '''
        return self._is_terminal

    def __str__(self) -> str:
        return f'{self._lexema} ; {self._is_terminal}'
