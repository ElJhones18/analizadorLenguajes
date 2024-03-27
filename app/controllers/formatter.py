from models.language import Language

from models.pattern import Pattern
from models.production import Production
from models.token import Token


class Formatter:
    ''' Class Formatter is used to format languages. '''

    def __init__(self, language: Language | None = None) -> None:
        self._language: Language | None = language

    def remove_left_recursion(self) -> Language:
        ''' Function to remove left recursion. '''

        productions: list[Production] =\
            self._language.get_productions()

        for main_prod in productions:

            sec_prods_list: list[Production] = []

            main_token: Token = main_prod.get_mtoken()
            sec_token: Token = f"{main_token.get_lexema()}'"

            empty_token: Token = Token('λ', True)
            empty_pattern: Pattern = Pattern([empty_token])

            sec_prod: Production = Production(
                sec_token, [empty_pattern]
            )
            patterns: list[Pattern] = main_prod.get_patterns()

            for patt in patterns:
                first_token: Token | None = patt.get_first()

                if first_token is None:
                    continue

                if main_prod.eq_mtoken(first_token):

                    new_patt: Pattern =\
                        main_prod.discard_pattern(patt)

                    new_patt.remove_token(first_token)
                    new_patt.add_token(sec_token)

                    sec_prod.add_pattern(new_patt)
                    # patt.remove_token(first_token)
                    # patt.add_token(sec_token)

                    # main_prod.remove_pattern(patt)
                else:
                    patt.add_token(sec_token)
            sec_prods_list.append(sec_prod)

        for sec_prod in sec_prods_list:
            self._language.add_production(sec_prod)

        print(self._language)

        return self._language

    def set_language(self, language: Language) -> None:
        ''' Function to set language. '''
        self._language = language
