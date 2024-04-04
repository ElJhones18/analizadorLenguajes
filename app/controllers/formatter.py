from models.language import Language

from models.pattern import Pattern
from models.production import Production
from models.token import Token


class Formatter:
    """Class Formatter is used to format languages."""

    def __init__(self, language: Language | None = None) -> None:
        self._language: Language | None = language

    def set_language(self, language: Language) -> None:
        """Function to set language."""
        self._language = language

    def remove_left_recursion(self) -> Language:
        """Function to remove left recursion."""
        productions: list[Production] = self._language.get_productions()

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
                alphas.append(Pattern([Token("λ", True)]))
                sec_production: Production = Production(sec_token, alphas)
                self._language.add_production(sec_production)

        # print("ola" + self._language.to_string())
        # print("-----------------------------------------------------------------")
        return self._language

    # def verify_word(
    #     self, word, g_word, symbol, optional
    # ):
    #     start_gword = len(g_word)
    #     t_word = ""
    #     if not symbol.is_terminal():
    #         if  len(self._language.get_production(symbol.get_lexema2()).get_patterns()) > 1:
    #             optional = True
    #         for pattern in self._language.get_production(symbol.get_lexema2()).get_patterns():
    #             for i in pattern.get_tokens():
    #                 t_word = self.verify_word(word, g_word, i, optional)
    #                 if len(t_word) != 0 :
    #                     g_word = t_word
    #                 else:
    #                     break
    #             if len(g_word) > start_gword:
    #                 break
    #         if symbol.get_lexema2() == self._language.get_initial_prod().get_mtoken().get_lexema2():
    #             if len(t_word) == len(word):
    #                 return True
    #             else:
    #                 return False
    #         else:
    #             return t_word
    #     else:
    #         g_word += symbol.get_lexema2()
    #         if word.startswith(g_word):
    #             return g_word
    #         else:
    #             return ""
            
            
    def verify_word(
        self, word: str, g_word: str, symbol: Token, optional: bool
    ):
        start_gword: int = len(g_word)
        t_word: str = ""
        if not symbol.is_terminal():
            if  len(self._language.get_production(symbol.get_lexema2()).get_patterns()) > 1:
                optional = True
            for pattern in self._language.get_production(symbol.get_lexema2()).get_patterns():
                for i in pattern.get_tokens():
                    t_word = self.verify_word(word, g_word, i, optional)
                    if len(t_word) != 0:
                        g_word = t_word
                    else:
                        break
                if len(g_word) > start_gword:
                    break
            if symbol.get_lexema2() == self._language.get_initial_prod().get_mtoken().get_lexema2():
                if len(t_word) == len(word):
                    print("true")
                    return True
                else:
                    print("false")
                    # return False
                    return t_word
            else:
                return t_word
        else:
            g_word += symbol.get_lexema2()
            if word.startswith(g_word):
                return g_word
            else:
                return ""
