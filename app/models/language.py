from models.production import Production
from models.token import Token


class Language:
    ''' Class Language is used to link productions. '''

    def __init__(self, name: str, productions: list[Production] = []) -> None:
        self._name: str = name
        self._productions: list[Production] = productions

    def add_production(self, production: Production) -> None:
        ''' Add production to language. '''
        self._productions.append(production)

    def get_name(self) -> str:
        ''' Get name from language. '''
        return self._name

    def get_productions(self) -> list[Production]:
        ''' Get productions from language. '''
        return self._productions

    def set_productions(self, productions: list[Production]) -> None:
        ''' Set productions to language. '''
        self._productions = productions

    def get_production(self, lexema: str) -> Production:
        ''' Get production from language. '''
        for production in self._productions:
            main_token: Token = production.get_mtoken()
            if main_token.get_lexema() == lexema:
                return production
        return None

    def get_initial_prod(self) -> Production:
        ''' Get initial production from language. '''
        return self._productions[0]

    def is_initial_prod(self, production: Production) -> bool:
        ''' Check if production is initial production. '''
        return production == self.get_initial_prod()

    def is_initial_token(self, token: Token) -> bool:
        ''' Function to check if token is initial token. '''
        return token == self.get_initial_prod().get_mtoken()

    def get_prods_contains(self, token: Token) -> list[Production]:
        ''' Get containers production from language. '''
        container: list[Production] = []
        for production in self._productions:
            if production.include_token(token):
                container.append(production)
        return container

    def set_title(self, title: str) -> None:
        ''' Function to set title to language. '''
        self._name = title

    def __str__(self) -> str:
        prods: str = ''
        for production in self._productions:
            prods += f' \n{production}'
        return f'【 name: {self._name} | productions: {prods}\n】'
