#==========================================================
#Bibliotécas
#==========================================================
import pandas as pd
import numpy as np
import inflection
import streamlit as st
import folium
from folium.plugins import MarkerCluster
from matplotlib import pyplot as plt
from streamlit_folium import folium_static
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title = 'Cidades', page_icon = '🏙️', layout = 'wide')#Deixa o objeto ocupar toda a extensão da tela

#==========================================================
#Funções
#==========================================================
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def create_price_type(price_range):
    if price_range == 1:
        return 'cheap'
    elif price_range == 2:
        return 'normal'
    elif price_range == 3:
        return 'expensive'
    else:
        return 'gourmet'

def converter_booleano(num):
    if num == 0:
        return 'No'
    else:
        return 'Yes'
    
def pais_mais_cidades(df):
    df_aux = (df.loc[:, ['country', 'city']]
                .groupby(['country'])
                .count()
                .sort_values('city', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'city', text_auto = 'city')
    return figura

def pais_mais_restaurantes(df):
    df_aux = (df.loc[:, ['country', 'restaurant_id']]
                .groupby(['country'])
                .count()
                .sort_values('restaurant_id', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'restaurant_id', text_auto = 'restaurant_id')
    return figura

def pais_mais_restaurantes_preco_4(df):
    df_aux = (df.loc[df['price_range'] == 4, ['country', 'price_range']]
                .groupby(['country'])
                .count()
                .sort_values('price_range', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'price_range', text_auto = 'price_range')
    return figura

def pais_mais_tipos_culinaria(df):
    df_aux = (df.loc[:, ['country', 'cuisines']]
                .groupby(['country'])
                .nunique()
                .sort_values('cuisines', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'cuisines', text_auto = 'cuisines')
    return figura

def pais_mais_avaliacoes(df):
    df_aux = (df.loc[:, ['country', 'votes']]
                .groupby(['country'])
                .sum()
                .sort_values('votes', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'votes', text_auto = 'votes')
    return figura

def pais_mais_restaurantes_com_entrega(df):
    df_aux = (df.loc[df['is_delivering_now'] == 'Yes', ['country', 'is_delivering_now']]
                .groupby(['country'])
                .count()
                .sort_values('is_delivering_now', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'is_delivering_now', text_auto = 'is_delivering_now')
    return figura

def pais_mais_restaurantes_com_reserva(df):
    df_aux = (df.loc[df['has_table_booking'] == 'Yes', ['country', 'has_table_booking']]
                .groupby(['country'])
                .count()
                .sort_values('has_table_booking', ascending = False)
                .reset_index())
    figura = px.bar(df_aux, x = 'country', y = 'has_table_booking', text_auto = 'has_table_booking')
    return figura

def pais_mais_restaurantes_com_reserva(df):
    df_aux = (df.loc[:, ['country', 'votes']]
                .groupby(['country'])
                .mean()
                .sort_values('votes', ascending = False)
                .reset_index())
    figura = px.bar(round(df_aux, 2), x = 'country', y = 'votes', text_auto = 'votes')
    return figura

def pais_maior_media_avaliacoes(df):
    df_aux = (df.loc[:, ['country', 'aggregate_rating']]
                .groupby(['country'])
                .mean()
                .sort_values('aggregate_rating', ascending = False)
                .reset_index())
    figura = px.bar(round(df_aux, 2), x = 'country', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def pais_menor_media_avaliacoes(df):
    df_aux = (df.loc[:, ['country', 'aggregate_rating']]
                .groupby(['country'])
                .mean()
                .sort_values('aggregate_rating', ascending = True)
                .reset_index())
    figura = px.bar(round(df_aux, 2), x = 'country', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def media_preco_prato_2(df):
    df_aux = (df.loc[:, ['country', 'average_cost_for_two']]
                .groupby(['country'])
                .mean()
                .sort_values('average_cost_for_two', ascending = False)
                .reset_index())
    figura = px.bar(round(df_aux, 2), x = 'country', y = 'average_cost_for_two', text_auto = 'average_cost_for_two')
    return figura

def cidade_mais_restaurantes(df):
    df_aux = (df.loc[:, ['city', 'country', 'restaurant_id']]
                .groupby(['country','city'])
                .count()
                .sort_values('restaurant_id', ascending = False)
                .reset_index())
    df_aux.columns = ['Países', 'Cidades', 'Qt_Restaurantes']
    figura = px.bar(df_aux.head(10), x = 'Cidades', y = 'Qt_Restaurantes', color = 'Países', template='plotly_white', text_auto = 'Qt_Restaurantes')
    return figura

def cidade_mais_restaurantes_nota_maior_4(df):
    df_aux = (df.loc[df['aggregate_rating'] > 4, ['city', 'country', 'restaurant_id']]
                .groupby(['country','city'])
                .count()
                .sort_values('restaurant_id', ascending = False)
                .reset_index())
    df_aux.columns = ['Países', 'Cidades', 'Qt_Restaurantes']
    figura = px.bar(df_aux.head(10), x = 'Cidades', y = 'Qt_Restaurantes', color = 'Países', template='plotly_white', text_auto = 'Qt_Restaurantes')
    return figura

def cidade_mais_restaurantes_nota_menor_2_5(df):
    df_aux = (df.loc[df['aggregate_rating'] < 2.5, ['city', 'country', 'restaurant_id']]
                .groupby(['country','city'])
                .count()
                .sort_values('restaurant_id', ascending = False)
                .reset_index())
    df_aux.columns = ['Países', 'Cidades', 'Qt_Restaurantes']
    figura = px.bar(df_aux.head(10), x = 'Cidades', y = 'Qt_Restaurantes', color = 'Países', template='plotly_white', text_auto = 'Qt_Restaurantes')
    return figura

def cidade_maior_valor_para_2(df):
    df_aux = (df.loc[:, ['city', 'average_cost_for_two']]
                .groupby(['city'])
                .mean()
                .sort_values('average_cost_for_two', ascending = False)
                .reset_index())
    figura = px.bar(round(df_aux, 2).head(10), x = 'city', y = 'average_cost_for_two', text_auto = 'average_cost_for_two')
    return figura

def cidade_maior_qtde_tipo_culinario(df):
    df_aux = (df.loc[:, ['city', 'country', 'cuisines']]
                .groupby(['country','city'])
                .nunique()
                .sort_values('cuisines', ascending = False)
                .reset_index())
    df_aux.columns = ['Países', 'Cidades', 'Qtde_tipos_culinários']
    figura = px.bar(df_aux.head(10), x = 'Cidades', y = 'Qtde_tipos_culinários', color = 'Países', template='plotly_white', text_auto = 'Qtde_tipos_culinários')
    return figura

def cidade_mais_restaurantes_com_reserva(df):
    df_aux = (df.loc[df['has_table_booking'] == 'Yes', ['city', 'has_table_booking']]
                .groupby(['city'])
                .count()
                .sort_values('has_table_booking', ascending = False)
                .reset_index())
    figura = px.bar(df_aux.head(10), x = 'city', y = 'has_table_booking', text_auto = 'has_table_booking')
    return figura

def cidade_mais_restaurantes_com_entrega(df):
    df_aux = (df.loc[df['is_delivering_now'] == 'Yes', ['city', 'is_delivering_now']]
                .groupby(['city'])
                .count()
                .sort_values('is_delivering_now', ascending = False)
                .reset_index())
    figura = px.bar(df_aux.head(10), x = 'city', y = 'is_delivering_now', text_auto = 'is_delivering_now')
    return figura

def cidade_mais_restaurantes_com_online(df):
    df_aux = (df.loc[df['has_online_delivery'] == 'Yes', ['city', 'has_online_delivery']]
                .groupby(['city'])
                .count()
                .sort_values('has_online_delivery', ascending = False)
                .reset_index())
    figura = px.bar(df_aux.head(10), x = 'city', y = 'has_online_delivery', text_auto = 'has_online_delivery')
    return figura

def restaurante_maior_qtde_avaliacoes(df):
    df_aux = (df.loc[:, ['restaurant_name', 'votes']]
                .groupby(['restaurant_name'])
                .sum()
                .sort_values('votes', ascending = False)
                .reset_index())
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'votes', text_auto = 'votes')
    return figura

def restaurante_maior_media_avaliacoes(df):
    df_aux = (df.loc[:, ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]] 
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_maior_media_avaliacoes_nome(df, nome):
    df = (df.loc[:, ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df = df.loc[nome, 'restaurant_name'] 
    return df

def restaurante_maior_media_avaliacoes_indice(df, indice):
    df = (df.loc[:, ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df = df.loc[indice, 'aggregate_rating'] 
    return df

def restaurante_maior_valor_para_2(df):
    df_aux = (df.loc[:, ['restaurant_name', 'average_cost_for_two']]
                .groupby(['restaurant_name'])
                .max()
                .sort_values('average_cost_for_two', ascending = False)
                .reset_index())
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'average_cost_for_two', text_auto = 'average_cost_for_two')
    return figura

def restaurante_brasileira_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Brazilian', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    tabela = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]].head(10)
    return tabela

def restaurante_brasileira_brasil_maior_avaliacao(df):
    filtro = (df['cuisines'] == 'Brazilian') & (df['country'] == 'Brazil')
    df_aux = (df.loc[filtro, ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby('restaurant_name')
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]                                                                                              
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def comparativo_restaurantes_avaliacoes_online(df):
    df_aux = (round(df.loc[:, ['has_online_delivery', 'votes']]
                      .groupby(['has_online_delivery'])
                      .mean()
                      .sort_values('votes', ascending = False)
                      .reset_index(), 2))
    figura = px.bar(df_aux, x = 'has_online_delivery', y = 'votes', text_auto = 'votes')
    return figura

def comparativo_restaurantes_avaliacoes_reserva_para_2(df):
    df_aux = (round(df.loc[:, ['has_table_booking', 'average_cost_for_two']]
                      .groupby(['has_table_booking'])
                      .mean()
                      .sort_values('average_cost_for_two', ascending = False)
                      .reset_index(), 2))
    figura = px.bar(df_aux, x = 'has_table_booking', y = 'average_cost_for_two', text_auto = 'average_cost_for_two')
    return figura

def comparativo_restaurantes_japoneses_e_bbq(df):
    filtro = ((df['cuisines'] == 'Japanese') & (df['country'] == 'United States of America') | (df['cuisines'] == 'BBQ'))
    df_aux = (round(df.loc[filtro, ['cuisines', 'average_cost_for_two']]                         
                      .groupby(['cuisines'])
                      .mean()
                      .sort_values('average_cost_for_two', ascending = False)
                      .reset_index(), 2))
    figura = px.bar(df_aux, x = 'cuisines', y = 'average_cost_for_two', text_auto = 'average_cost_for_two')
    return figura

def restaurante_italiano_maior_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Italian', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_italiano_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Italian', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_americano_maior_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'American', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_americano_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'American', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating' ]]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_arabe_maior_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Arabian', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_arabe_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Arabian', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_japones_maior_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Japanese', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = round(df_aux.loc[:, ['restaurant_name', 'aggregate_rating']], 2)
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_japones_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Japanese', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]
    figura = px.bar(df_aux.head(10), x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_caseiro_maior_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Home-made', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]
    figura = px.bar(df_aux, x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def restaurante_caseiro_menor_avaliacao(df):
    df_aux = (df.loc[df['cuisines'] == 'Home-made', ['restaurant_name', 'restaurant_id', 'aggregate_rating']]
                .groupby(['restaurant_name'])
                .mean()
                .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [True, True])
                .reset_index())
    df_aux = df_aux.loc[:, ['restaurant_name', 'aggregate_rating']]
    figura = px.bar(df_aux, x = 'restaurant_name', y = 'aggregate_rating', text_auto = 'aggregate_rating')
    return figura

def tipo_culinaria_maior_preco_2(df):
    df_aux = (df.loc[:, ['cuisines', 'average_cost_for_two']]
                .groupby(['cuisines'])
                .mean()
                .sort_values('average_cost_for_two', ascending = False)
                .reset_index())
    df_aux = round(df_aux.loc[:, ['cuisines', 'average_cost_for_two']], 2)
    figura = px.bar(df_aux.head(10), x = 'cuisines', y = 'average_cost_for_two', text_auto = 'average_cost_for_twog')
    return figura

def tipo_culinaria_maior_nota_media(df):
    df_aux = (df.loc[:, ['cuisines', 'aggregate_rating']]
                .groupby(['cuisines'])
                .mean()
                .sort_values('aggregate_rating', ascending = False)
                .reset_index())
    df_aux.columns = ['Tipos_de_culinária', 'Qt_Avaliações']
    figura =  px.bar(round(df_aux, 2), x = 'Tipos_de_culinária', y = 'Qt_Avaliações', text_auto = 'Qt_Avaliações')
    return figura

def tipo_culinaria_menor_nota_media(df):
    df_aux = (df.loc[:, ['cuisines', 'aggregate_rating']]
                .groupby(['cuisines'])
                .mean()
                .sort_values('aggregate_rating', ascending = True)
                .reset_index())
    df_aux.columns = ['Tipos_de_culinária', 'Qt_Avaliações']
    figura =  px.bar(round(df_aux, 2), x = 'Tipos_de_culinária', y = 'Qt_Avaliações', text_auto = 'Qt_Avaliações')
    return figura

def tipo_culinaria_online_e_delivery(df):
    filtro = (df['has_online_delivery'] == 'Yes') & (df['is_delivering_now'] == 'Yes')
    df_aux = (df.loc[filtro, ['cuisines', 'restaurant_id']]
                .groupby(['cuisines'])
                .count()
                .sort_values('restaurant_id', ascending = False)
              .reset_index())
    figura =  px.bar(df_aux.head(10), x = 'cuisines', y = 'restaurant_id', text_auto = 'restaurant_id')
    return figura

def renomear_colunas(dataframe):
    df1 = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def mapa_paises(df):     
    '''Esta função tem a responsabilidade retornar um mapa
        Input: dataframe
        Output: mapa    
    '''
    datamapa = df[['restaurant_name', 'longitude', 'latitude', 'cuisines', 'average_cost_for_two', 'currency', 'aggregate_rating', 'color']].reset_index(drop = True)
    
    # Criando o mapa
    mapa = folium.Map(zoom_start = 15)

    #Criando os clusters
    cluster = MarkerCluster().add_to(mapa)

    icon = 'fa-cutlery'

    #Colocando os pinos
    for index, location_info in datamapa.iterrows():
        folium.Marker([location_info['latitude'],       
                   location_info['longitude']],
                   icon = folium.Icon(color=location_info['color'], icon=icon, prefix='fa'),
                   popup = folium.Popup(f"""<h6> <b> {location_info['restaurant_name']} </b> </h6> <br>
                                        Cozinha: {location_info['cuisines']} <br>
                                        Preço médio para dois: {location_info['average_cost_for_two']} ({location_info['currency']}) <br>
                                        Avaliação: {location_info['aggregate_rating']} / 5.0 <br> """,
                                        max_width= len(f"{location_info['restaurant_name']}")*20)).add_to(cluster)
    folium_static(mapa, width = 924, height = 600)

def editar_df(df):
    df['restaurant_id'] = df['restaurant_id'].astype(str)
    df['cuisines'] = df['cuisines'].astype(str)
    df['city'] = df['city'].astype(str)
    df['restaurant_id'] = df['restaurant_id'].str.strip()
    df['cuisines'] = df['cuisines'].apply(lambda x: x.split(',')[0])
    df['country'] = df['country_code'].apply(lambda x: COUNTRIES[x])
    df['color'] = df['rating_color'].apply(lambda x: COLORS[x])
    df['price_type'] = df['price_range'].apply(create_price_type)
    df['has_table_booking'] = df['has_table_booking'].apply(converter_booleano)
    df['has_online_delivery'] = df['has_online_delivery'].apply(converter_booleano)
    df['is_delivering_now'] = df['is_delivering_now'].apply(converter_booleano)
    df = df.loc[df['cuisines'] != 'nan', :].reset_index()
    return df

#==========================================================
#Extração
#==========================================================

#Importando o dataset
df1 = pd.read_csv('dataset/zomato.csv')

#Fazendo uma cópia do arquivo original
df = df1.copy()

#Renomeando as colunas
df = renomear_colunas(df1)

#Editando os dados
df = editar_df(df)

#==========================================================
#Barra laterial
#==========================================================
    
image = Image.open('logo.png')#Imagem precisa estar na mesma pasta do arquivo .PY
st.sidebar.image(image, width = 60)

st.sidebar.markdown('## Fome Zero')
st.sidebar.markdown('### Filtros')

tipos_de_paises = df['country'].unique()
paises = st.sidebar.multiselect('Escolha os paises que deseja visualizar os restaurantes:', tipos_de_paises,
                        default = ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'])

qtde_restaurante_slider = st.sidebar.slider(
    'Selecione a quantidade de restaurantes que deseja visualizar',
    value = 10,
    min_value = 1,
    max_value = 20)

tipos_de_culinaria = df['cuisines'].unique()
culinaria = st.sidebar.multiselect('Escolha o tipo de culinária:', tipos_de_culinaria,
                        default = ['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American', 'Italian'])

st.sidebar.markdown('''---''')

#Filtro de tipo culinário
linhas_selecionadas_culinaria = df['cuisines'].isin(culinaria)#isin está em
df = df.loc[linhas_selecionadas_culinaria, :]

#Filtro de países
linhas_selecionadas_paises = df['country'].isin(paises)#isin está em
df = df.loc[linhas_selecionadas_paises, :]

#==========================================================
#Central
#==========================================================
with st.container():
    st.markdown('# Visão Tipos culinários')
    st.markdown('## Melhores restaurantes dos principais tipos culinários')

st.markdown('''---''')

with st.container():
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        col1.metric(restaurante_maior_media_avaliacoes_nome(df, nome = 0), restaurante_maior_media_avaliacoes_indice(df, indice = 0))
    with col2:
        col2.metric(restaurante_maior_media_avaliacoes_nome(df, nome = 1), restaurante_maior_media_avaliacoes_indice(df, indice = 1))
    with col3:
        col3.metric(restaurante_maior_media_avaliacoes_nome(df, nome = 2), restaurante_maior_media_avaliacoes_indice(df, indice = 2))
    with col4:
        col4.metric(restaurante_maior_media_avaliacoes_nome(df, nome = 3), restaurante_maior_media_avaliacoes_indice(df, indice = 3))
    with col5:
        col5.metric(restaurante_maior_media_avaliacoes_nome(df, nome = 4), restaurante_maior_media_avaliacoes_indice(df, indice = 4))
        
with st.container():
    st.markdown('## Top 10 restaurantes')
    
    df = (df.loc[:, ['restaurant_name', 'restaurant_id', 'country', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']]
          .sort_values(['aggregate_rating', 'restaurant_id'], ascending = [False, True]))
    st.dataframe(df.head(qtde_restaurante_slider))
    
st.markdown('''---''')

with st.container():
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('##### Melhores tipos de culinárias')
        figura = tipo_culinaria_maior_nota_media(df)
        st.plotly_chart(figura, use_container_width = True)        
    with col2:
        st.markdown('##### Piores tipos de culinárias')
        figura = tipo_culinaria_menor_nota_media(df)
        st.plotly_chart(figura, use_container_width = True)  
