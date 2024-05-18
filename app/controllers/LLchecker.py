import copy
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
        self._initial_productions: list[Production] = []

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
        self.set_initial_productions()

        # ps:str = ""
        # for p in self._initial_productions:
        #     ps += p.__str__() + "\n"
        # print(ps)
        return self._language

    def check_ll0(self, actual: int) -> None:  # arg def

        if actual == 0:
            state: State = State("I-" + str(actual), True, [])
            self.add_new_prods(state, [self._initial_productions[0]])
            if not self._automaton.has_state(state):
                self._automaton.add_state(state)
        else:
            state: State = State("I-" + str(actual), False, [])

        self.check_ll0(actual + 1)

    def add_new_prods(self, state: State, new_prods: list[Production]) -> None:
        """
        Adds new productions to the given state and recursively adds any additional productions that are
        required based on the next non-terminal token in the production.

        Args:
            state (State): The state to which the new productions will be added.
            new_prods (list[Production]): The list of new productions to be added.

        Returns:
            None
        """
        if not new_prods:
            return

        productions: list[Production] = []
        for prod in new_prods:
            tokens = prod.get_first_pattern().get_tokens()
            for i, token in enumerate(tokens):
                if token.get_lexema() == "•" and i + 1 < len(tokens):
                    next_token = tokens[i + 1]
                    if not next_token.is_terminal():
                        for production in self._initial_productions:
                            if (
                                production.eq_mtoken(next_token)
                                and production not in productions
                            ):
                                productions.append(production)

        state.add_productions(new_prods)

        # Filtra producciones ya añadidas para evitar duplicados en las siguientes recursiones
        new_prods = [prod for prod in productions if not state.has_production(prod)]

        if new_prods:
            self.add_new_prods(state, new_prods)

    def set_initial_productions(self) -> None:
        for production in self._language.get_productions():
            cp: Production = copy.deepcopy(production)
            cp.get_first_pattern().get_tokens().insert(0, Token("•", True))
            self._initial_productions.append(cp)

    """
    1. Crear el estado
    2. Agregar las producciones por defecto
    3. Msover el punto
    4. evaluar si hay un punto antes de un no terminal
    5. si hay un punto antes de un no terminal, agregar las producciones de ese no terminal
    6. repetir el proceso hasta que no haya más puntos antes de no terminales
    7. verificar que el estado no exista
    8. agregar el estado al autómata

    """
