import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image


def main():

    @st.cache_data
    def load_data(file):
        xls = pd.ExcelFile(file)
        dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}
        return dfs

    # with st.sidebar:
    #     st.title("Dashboard - Espumante")
    #     uploaded_file = st. file_uploader("Coloque o seu arquivo 'sites.xlsx' aqui")
    # if uploaded_file is None:
    #     st.title(f"Adicione o arquivo Excel 'sites.xlsx' na sidebar")
    # else:
    dfs = load_data('sites.xlsx')
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("espumante.png", width=70)
    with col2:
        st.image("tacas.png", width=70)

    # Título da página
    st.title('Dashboard - Espumante')

    # Botão para exibir as palavras utilizadas na pesquisa
    state = st.button('Clique aqui para ver as palavras utilizadas na pesquisa')
    if state:
        if st.button('Clique aqui para ocultar'):
            state = False
        else:
            st.write("""
            espumantes, champagne,  adega,  prosecco, casamento,  casamentos, uvas, uva,  vinícula, diversão, bebida, festas, festa,  jantar, jantares, gastronomia,  degustação, queijo, chocolate,  chocolates, vinho,  vinhos, enoturismo, vinhedo,  taças,  taça, restaurante,  restaurantes, brinde, drink,  sabor , culinária,  massas, bruschettas,  frança, itália, espanha,  anonovo,  reveillon,  frescor,  sofisticação, cítricas, cítrico,  refrescante,  comidas , aperitivos, sobremesas, frutado,  chardonnay ,  flores, joias,  presentes,  presente, cestas, peixe,  peixes, marisco,  mariscos, acidez, cerimonialista, decoração,  fotografia, música, bartenders, bar,  bares,  confeitaria,  doce, doces,  arranjos, frisante, rótulos , salton, chandon,  freixenet,  garibaldi , aurora, miolo,  noiva,  noivas, safra, brunch, vinho espumante,  happy hour, espumante nature, espumante extrabrut,  espumante brut, espumante sec,  espumante seco, espumante demisec,  espumante doce, sabor frutado,  frutos do mar,  vinho frisante, ano novo, cave geisse,  casa perini,  casa valduga, vinícola aurora
            """)

    # Seleção do site
    site_selecionado = st.selectbox('Selecione o site', list(dfs.keys()))

    # Cabeçalho
    st.header(f'Palavras que mais aparecem no site: **{site_selecionado}**')

    st.write("")

    # Dados do site selecionado
    data = dfs[site_selecionado]

    st.write(f"Nuvem de Palavras do Site: **{site_selecionado}**")

    # # Nuvem de palavras do site
    word_freq = dict(zip(data['palavra'], data['qtde']))

    # Gerar a Word Cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    
    # Plotar a Word Cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot(plt)

    st.write("")
    st.write("")

    col1, col2 = st.columns([1, 2])

    with col1:
        # Dataframe com as palavras do site
        st.write(f"Palavras do site: **{site_selecionado}**")
        st.dataframe(data)

    with col2:
        # Gráfico interativo com Plotly Express
        st.write("Gráfico de Frequência das Palavras:")
        fig = px.bar(data, x='palavra', y='qtde', title=f'Frequência de Palavras no site {site_selecionado}', 
                    labels={'palavra': 'Palavra', 'qtde': 'Quantidade'},
                    template='plotly_white')
        fig.update_layout(xaxis_tickangle=-45)

        st.plotly_chart(fig, use_container_width=True)
if __name__  == '__main__':
    main()