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

    def check_LR0(self, actual: int, default_prods: list[Production]) -> None:
        """
        Checks if the language is LR(0).

        Args:
            actual (int): The index of the current state.
            default_prods (list[Production]): The list of default productions for the current state.

        Returns:
            None
        """
        # print("------------------------------------")
        if not default_prods and actual != 0:
            return

        posible_transitions: list[Token] = []

        if actual == 0:
            # print("NUEVA EJECUCION")
            state: State = State("I-" + str(actual), True, [])
            self.add_new_prods(state, [self._initial_productions[0]])

            if not self._automaton.has_state(state):
                self._automaton.add_state(state)
                posible_transitions = self.check_posible_transitions(state)
            else:
                # print("YA EXISTE EL ESTADO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return
        else:
            state: State = State("I-" + str(actual), False, [])
            defs: list[Production] = self.move_dot(default_prods)
            self.add_new_prods(state, defs)

            if not self._automaton.has_state(state):
                self._automaton.add_state(state)
                posible_transitions = self.check_posible_transitions(state)
            else:
                # print("YA EXISTE EL ESTADO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return

        if not self._automaton.has_state(state):
            actual, _ = self._automaton.has_state(state)
        else:
            actual += 1

        if posible_transitions:
            for pt in posible_transitions:
                defs = self.find_default_prods(pt, state.get_productions())
                self.check_LR0(actual, defs)

    def move_dot(self, prods: list[Production]) -> None:
        """
        Moves the dot symbol ('•') in the given list of productions one position to the right.

        Args:
            prods (list[Production]): The list of productions to modify.

        Returns:
            None
        """
        cp = copy.deepcopy(prods)
        for prod in cp:
            tokens = prod.get_first_pattern().get_tokens()
            for i, token in enumerate(tokens):
                if token.get_lexema() == "•" and i + 1 < len(tokens):
                    tokens[i] = tokens[i + 1]
                    tokens[i + 1] = Token("•", True)
                    break
        return cp

    def find_default_prods(
        self, token: Token, prods: list[Production]
    ) -> list[Production]:
        """
        Finds the default productions for a given token.
        Being default productions, the ones that can move with the dot

        Args:
            token (Token): The token to search for.
            prods (list[Production]): The list of productions to search in.

        Returns:
            list[Production]: The list of default productions found.
        """
        default_prods: list[Production] = []
        for prod in prods:
            tokens = prod.get_first_pattern().get_tokens()
            for i, t in enumerate(tokens):
                if t.get_lexema() == "•" and i + 1 < len(tokens):
                    if tokens[i + 1].get_lexema() == token.get_lexema():
                        default_prods.append(prod)
        return default_prods

    def check_posible_transitions(self, state: State) -> list[Token]:
        """
        Returns a list of possible transitions from the given state.

        Args:
            state (State): The state to check for possible transitions.

        Returns:
            list[Token]: A list of tokens representing the possible transitions.
        """
        posibles: list[Token] = []
        for prod in state.get_productions():
            tokens = prod.get_first_pattern().get_tokens()
            for i, token in enumerate(tokens):
                if token.get_lexema() == "•" and i + 1 < len(tokens):
                    if tokens[i + 1] not in posibles:
                        posibles.append(tokens[i + 1])

        return posibles

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
                        # for production in self._initial_productions:
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
        """
        Sets the initial productions for the LL checker.

        This method creates a deep copy of each production in the language's productions list,
        adds a special token "•" at the beginning of the first pattern's tokens list,
        and appends the modified production to the initial productions list.

        Returns:
            None
        """
        self._initial_productions = []
        for production in self._language.get_productions():
            cp: Production = copy.deepcopy(production)
            cp.get_first_pattern().get_tokens().insert(0, Token("•", True))
            self._initial_productions.append(cp)
