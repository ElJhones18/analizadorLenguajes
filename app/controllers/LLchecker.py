from models.automaton.state import State
from models.automaton.automaton import Automaton
from models.language.language import Language
from models.language.pattern import Pattern
from models.language.production import Production
from models.language.token import Token


class LLchecker:
    def __init__(self) -> None:
        self._language: Language = None
        self._automaton: Automaton = Automaton([], [], None)

    def get_language(self) -> Language:
        return self._language

    def set_language(self, language: Language) -> None:
        self._language = language

    def extend_grammar(self) -> Language:
        """Function to extend grammar."""
        initial_production: Production = self._language.get_initial_prod().get_mtoken()
        self._language.add_extended_production(
            Production(Token("S", False), [Pattern([initial_production])])
        )
        # print(self._language.to_string())
        return self._language

    def check_ll0(self, actual: int) -> None:

        if actual == 0:
            self.create_first_state()
        else:
            state: State = State("I-" + str(actual), False, [])

        return

    def create_first_state(self) -> None:
        print("helloxd")
        state: State = State("I-0", False, [])
        productions: list[Production]
        s_prod: Production = self._language.get_initial_prod()
        s_prod.get_patterns()[0].get_tokens().insert(0, Token("•", True))
        state.add_production(s_prod)
        print("hellosasa" + state.__str__())

        # for production in state.get_productions():
        for i, token in enumerate(s_prod.get_patterns()[0].get_tokens()):
            if i == 0 and token.get_lexema() == "•":
                next_token: Token = s_prod.get_patterns()[0].get_tokens()[i + 1]
                if not next_token.is_terminal():
                    for production in self._language.get_productions():
                        if (
                            production.get_mtoken().get_lexema()
                            == next_token.get_lexema()
                        ):
                            production: Production = production
                            production.get_patterns()[0].get_tokens().insert(
                                0, Token("•", True)
                            )
                            state.add_production(production)

        print("hello" + state.__str__())
        self._automaton.add_state(state)
        self._automaton.set_initial_state(state)
        return
