from models.language import Language

from models.pattern import Pattern
from models.production import Production
from models.token import Token


class Formatter:
    ''' Class Formatter is used to format languages. '''

    def __init__(self, language: Language | None = None) -> None:
        self._language: Language | None = language

    def set_language(self, language: Language) -> None:
        ''' Function to set language. '''
        self._language = language
    
    def remove_left_recursion(self) -> Language:
        ''' Function to remove left recursion. '''
        productions: list[Production] =\
            self._language.get_productions()

        for production in productions:
            if production.is_recursive():
                main_token: Token = production.get_mtoken()
                sec_token: Token = Token(main_token.get_lexema() + "'", False)

                alphas: list[Pattern] = []
                betas: list[Pattern] = []

                for pattern in production.get_patterns():
                    first_token: Token | None = pattern.get_first()

                    if first_token is None:
                        continue

                    if production.eq_mtoken(first_token):
                        pattern.remove_token(first_token)
                        alphas.append(pattern)
                    else:
                        betas.append(pattern)

                # print("alphas: ")
                # for alpha in alphas:
                #     print(alpha.__str__())
                # print("betas: ")
                # for beta in betas:
                #     print(beta.__str__())

                production.remove_patterns()
                
                for beta in betas:
                    beta.add_token(sec_token)

                production.add_patterns(betas)

                for alpha in alphas:
                    alpha.add_token(sec_token)

                sec_production: Production = Production(sec_token, alphas)
                self._language.add_production(sec_production)

        print('ola' + self._language.to_string())
        print('-----------------------------------------------------------------')
        return self._language
