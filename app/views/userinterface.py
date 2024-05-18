import streamlit as st
from PIL import Image

# from controllers.LLchecker import LLchecker
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

                self._LLchecker.check_LR0(0, [])
                self._LLchecker._automaton.fix_names()
                
                for state in self._LLchecker._automaton.get_states():
                    print(state)
                    print("")            
                """
                st.subheader("Lenguaje sin recursion")
                # loader: Reader = Reader()
                # lang_one: Language = loader.str_to_lang(text)

                # self._formatter.set_language(lang_one)

                # lang_without_recursion: Language = self._formatter.remove_left_recursion()
                
                # st.text(lang_without_recursion.to_string())

                # # Input para ingresar texto
                # input_text = st.text_area("Ingresa una palabra para analizar si pertenece al lenguaje")

                # # Botón para subir texto
                # submit_button = st.button("Verificar")
                
                # #lo de abajo debe mostrarse solo cuando se presione el botón de verificar
                # if submit_button:
                    
                    
                #     with col2:
                        
                #         if isinstance(self._formatter.verify_word(input_text, "", self._formatter._language.get_initial_prod().get_mtoken(), False), bool):
                #             st.subheader("\n\n\n\n\nLa palabra pertenece a la gramática.")
                #             st.image("app\data\happycat.gif")                    
                #         else: 
                #             st.subheader("\n\n\n\n\nLa palabra NO pertenece a la gramática.")
                #             st.image("app\data\cat.gif", use_column_width=True)                    """
