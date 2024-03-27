import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Interfaz Bacancita con Streamlit")

# Subtitulo
st.subheader("Sube un archivo de texto o ingresa texto en el input")

# Drag and Drop para subir archivos de texto
uploaded_file = st.file_uploader("Arrastra y suelta un archivo de texto (.txt)", type=["txt"])

# Input para ingresar texto
input_text = st.text_area("O ingresa tu texto aquí")

# Botón para subir texto
submit_button = st.button("Subir Texto")

# Sección para mostrar la imagen
st.subheader("Imagen a pantalla completa")
# Cargando la imagen
image = Image.open("app\data\gatoaudifonos.jpg")  # Cambia "example_image.jpg" por la ruta de tu imagen
st.image(image, use_column_width=True)

