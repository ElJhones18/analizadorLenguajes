from models.automaton.automaton import Automaton
import graphviz


class Render_automaton:
    def __init__(self, automaton: Automaton):
        self.automaton: Automaton = automaton

    def render(self):

        dot = graphviz.Digraph(comment="Automaton")
        dot.attr(bgcolor="#0e1117")
        self.change_dots()
        for state in self.automaton.get_states():
            label: str = ""
            is_acceptance: bool = False
            for production in state.get_productions():
                label += production.toString() + "\n"
                if production.is_acceptance():
                    is_acceptance = True
            label = state.get_name() + "\n\n" + label
            if is_acceptance:
                dot.node(
                    state.get_name(),
                    label,
                    shape="box",
                    fontname="Arial",
                    margin="0.2",
                    color="green",
                    fontcolor="white",
                )
            else:
                dot.node(
                    state.get_name(),
                    label,
                    shape="box",
                    fontname="Arial",
                    margin="0.2",
                    color="white",
                    fontcolor="white",
                )

        for transition in self.automaton.get_transitions():
            dot.edge(
                transition.get_source().get_name(),
                transition.get_target().get_name(),
                label=transition.get_label(),
                fontcolor="white",
                color="white",
            )

        dot.render(
            "app/data/automaton/automaton.gv",
            # view=True
        )

        dot.format = "svg"
        dot.render("app/data/automaton/automaton.gv")

        # print(dot.source)

    def set_automaton(self, automaton: Automaton):
        self.automaton = automaton

    def change_dots(self):
        for state in self.automaton.get_states():
            for production in state.get_productions():
                for pattern in production.get_patterns():
                    for token in pattern.get_tokens():
                        if token.get_lexema() == "•":
                            token.set_lexema(".")
