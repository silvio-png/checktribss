import streamlit as st

# 1. Configuração inicial da página
st.set_page_config(
    page_title="Unique '56 | The Panel",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Injeção de CSS customizado
estilo_customizado = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background-color: #121c26;
    color: #e0e0e0;
}

.mobile-container {
    max-width: 450px;
    margin: 0 auto;
    padding: 20px 10px;
    font-family: 'Arial', sans-serif;
}

.titulo-dourado {
    color: #dcb360;
    font-size: 1.4rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 30px;
    line-height: 1.4;
}

.texto-base {
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 20px;
    color: #c9d1d9;
    text-align: justify;
}

.texto-destaque {
    color: #dcb360;
    font-weight: 600;
}

.botao-dourado {
    display: block;
    width: 100%;
    background-color: #dcb360;
    color: #121c26 !important;
    text-align: center;
    padding: 16px;
    border-radius: 8px;
    font-weight: bold;
    text-decoration: none;
    font-size: 1.1rem;
    margin-top: 40px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    transition: background-color 0.3s;
}

.botao-dourado:hover {
    background-color: #f0c36b;
}
</style>
"""
st.markdown(estilo_customizado, unsafe_allow_html=True)

# 3. Construção do Conteúdo da Página (Sem espaços no início das linhas)
html_conteudo = """
<div class="mobile-container">
<div class="titulo-dourado">
Revendedor de Combustíveis:<br>
Você sabe exatamente quantos reais você perdeu 'variação de temperatura' ou erro de conciliação de estoque *hoje*?
</div>
<div class="texto-base">
Provavelmente não. E seus concorrentes também não sabem. Desenvolvi uma plataforma de inteligência de dados, Unique'56, exclusiva que se integra e complementa o seu sistema de gestão atual. 
Ela funciona como uma camada extra de auditoria, <span class="texto-destaque">identificando e estancando vazamentos financeiros silenciosos</span> que as operações comuns não detectam.
</div>
<div class="texto-base">
Por questões de confidencialidade estratégica, não exibo a mecânica publicamente. Agende uma apresentação privada.
</div>
<a href="https://wa.me/5519981795831?text=Ol%C3%A1%2C%20tenho%20interesse%20em%20agendar%20uma%20apresenta%C3%A7%C3%A3o%20confidencial%20da%20Unique%2756." class="botao-dourado" target="_blank">
Agendar Apresentação<br>Confidencial via WhatsApp
</a>
</div>
"""
st.markdown(html_conteudo, unsafe_allow_html=True)