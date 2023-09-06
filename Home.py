#==========================================================
#Bibliotécas
#==========================================================
import streamlit as st
from PIL import Image

st.set_page_config(page_title = 'Página principal', page_icon = '🌟', layout = 'wide')

#image_path = 'C:/Users/Leonardo/curso_cientista_de_dados/Repos/Python_zero_ao_ds/arquivos_python/'
image = Image.open('logo.png')#Imagem precisa estar na mesma pasta do arquivo .PY
st.sidebar.image(image, width = 60)

st.sidebar.markdown('## Fome Zero')
st.sidebar.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito!')
st.sidebar.markdown('''---''')

st.write('# Fome Zero Dashboard')

st.markdown(
    '''
    Fome Zero Dashboard foi construído para acompanhar as métricas de avaliação, tipo de culinária e demais informações dos restaurantes em várias partes do mundo!.
    ### Este dashboard foi estruturado 4 partes:
    - Geral;
    - Países;
    - Cidades;
    - Tipos de culinárias.

    Duvidas?, contactar:
    - www.linkedin.com/in/leonardonassibfonseca
    ''')