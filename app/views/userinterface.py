import streamlit as st
from PIL import Image

# from controllers.LLchecker import LLchecker
from views.render_automaton import Render_automaton
from controllers.LLchecker import LLchecker
from controllers.reader import Reader
from models.language.language import Language


class UserInterface:
    """Class Ui is used to renderize the program."""

    def __init__(self) -> None:
        self._LLchecker: LLchecker = LLchecker()

    def render(self) -> None:
        """Function to renderize the program."""
        # Título de la aplicación
        st.set_page_config(layout="wide")
        st.title("Analizador de Lenguajes")

        st.subheader("Sube un archivo de texto con tu lenguaje")

        # Drag and Drop para subir archivos de texto
        uploaded_file = st.file_uploader(
            "Arrastra y suelta el archivo de texto (.txt)", type=["txt"]
        )
        col1, col2 = st.columns(2)

        with col1:
            # Subtitulo

            # Si subió un archivo
            if uploaded_file:
                # Sección para mostrar el texto del archivo
                st.subheader("Lenguaje subido")
                # Se lee el archivo
                # text = uploaded_file.getvalue().decode("utf-8")
                text = uploaded_file.read().decode("UTF8")
                # Se muestra el texto
                st.text(text)

                loader: Reader = Reader()
                lang_one: Language = loader.str_to_lang(text)
                self._LLchecker.set_language(lang_one)
                extended_grammar: Language = self._LLchecker.extend_grammar()

                st.subheader("Lenguaje extendido")
                st.text(extended_grammar.to_string())

                self._LLchecker.build_automaton(0, [], None, None)
                self._LLchecker._automaton.fix_names()

                with col2:

                    st.subheader(self._LLchecker.check_LR0_SLR0())
                    
                    renderer: Render_automaton = Render_automaton(self._LLchecker._automaton)
                    renderer.render()
                    
                    st.image("app/data/automaton/automaton.gv.svg", use_column_width=True)