import streamlit as st
from PIL import Image

from controllers.formatter import Formatter
from controllers.reader import Reader
from models.language import Language


class UserInterface:
    ''' Class Ui is used to renderize the program. '''

    def __init__(self) -> None:
        self._formatter: Formatter = Formatter()

    def render(self) -> None:
        ''' Function to renderize the program. '''
        # Título de la aplicación
        st.title("Interfaz Bacancita con Streamlit")

        # Subtitulo
        st.subheader("Sube un archivo de texto o ingresa texto en el input")

        # Drag and Drop para subir archivos de texto
        uploaded_file = st.file_uploader(
            "Arrastra y suelta un archivo de texto (.txt)", type=["txt"])

        # Input para ingresar texto
        input_text = st.text_area("O ingresa tu texto aquí")

        # Botón para subir texto
        submit_button = st.button("Subir Texto")

        # Cuando clickee el botón:
        if submit_button:
            # Si subió un archivo
            # if uploaded_file is not None:
            #     # Sección para mostrar el texto del archivo
            #     st.subheader("Texto del archivo subido")
            #     # Se lee el archivo
            #     text = uploaded_file.getvalue().decode("utf-8")
            #     # Se muestra el texto
            #     st.write(text)

            # # Si ingresó texto en el input
            # if input_text:
            #     # Sección para mostrar el texto ingresado
            #     st.subheader("Texto ingresado")
            #     # Se muestra el texto
            #     st.write(input_text)
            file_route: str = 'app/data/lang1.txt'

            loader: Reader = Reader()
            lang_one: Language = loader.txt_to_lang(file_route)

            self._formatter.set_language(lang_one)

            self._formatter.remove_left_recursion()

        # Sección para mostrar la imagen
        st.subheader("Imagen a pantalla completa")
        # Cargando la imagen
        # Cambia "example_image.jpg" por la ruta de tu imagen
        # image = Image.open("app\data\gatoaudifonos.jpg")
        image = Image.open("app\\data\\gatoaudifonos.jpg")
        st.image(image, use_column_width=True)
