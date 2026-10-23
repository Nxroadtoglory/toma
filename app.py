<<<<<<< HEAD
import os
from google import genai
from PIL import Image
import streamlit as st

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA E DESIGN CUSTOMIZADO (CSS)
# ==============================================================================
st.set_page_config(
    page_title="Assistente de Design | Criativo", page_icon="", layout="wide"
)

# Injetando CSS customizado para dar um visual profissional de design
st.markdown("""
    <style>
    /* Estilização geral dos botões principais */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.95;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    /* Arredondamento e suavização de inputs e textareas */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    
    /* Caixa de upload com visual mais limpo */
    .stFileUploader>div {
        border-radius: 8px;
        border: 2px dashed #cbd5e1;
    }
    
    /* Ajuste de títulos */
    h1, h2, h3 {
        letter-spacing: -0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# CONFIGURAÇÃO DA API KEY
# ==============================================================================
# O SDK busca automaticamente a variável 'GEMINI_API_KEY'
# Se preferir testar localmente colando a chave, descomente a linha abaixo:
# os.environ["GEMINI_API_KEY"] = "SUA_API_KEY_AQUI"

client = genai.Client()
MODELO = "gemini-3.8-flash"
# ==============================================================================

st.title(" Assistente Virtual para Design")
st.markdown(
    "Sua central de suporte inteligente para análises visuais, brainstormings"
    " e validação de conceitos."
)

# Menu lateral
menu = st.sidebar.selectbox(
    "Escolha a Ferramenta",
    ["Análise e Critique de Imagem", "Brainstorming & Conceitos"],
)

if menu == "Análise e Critique de Imagem":
  st.header(" Critique Visual de Layout")
  imagem_subida = st.file_uploader(
      "Envie a imagem do projeto (PNG, JPG)", type=["png", "jpg", "jpeg"]
  )
  pergunta = st.text_area(
      "O que você gostaria que o assistente avaliasse?",
      placeholder="Ex: Analise a hierarquia visual, a legibilidade da tipografia"
      " e o contraste.",
  )

  if st.button("Analisar Design"):
    if not imagem_subida:
      st.warning("Por favor, envie uma imagem antes de continuar.")
    elif not pergunta:
      st.warning("Por favor, digite o que você quer analisar na imagem.")
    else:
      with st.spinner("Analisando os detalhes visuais com IA..."):
        try:
          img = Image.open(imagem_subida)
          prompt_sistema = (
              "Você é um Diretor de Arte sênior e especialista em UI/UX e"
              " Design Gráfico. Faça uma análise construtiva, técnica e focada"
              " em usabilidade, hierarquia visual e estética da imagem enviada."
          )

          response = client.models.generate_content(
              model=MODELO, contents=[img, prompt_sistema, pergunta]
          )

          st.markdown("###  Parecer do Especialista:")
          st.markdown(response.text)
        except Exception as e:
          st.error(f"Erro ao processar a imagem: {e}")

elif menu == "Brainstorming & Conceitos":
  st.header(" Gerador de Ideias & Brainstorm")
  briefing = st.text_area(
      "Qual é o briefing ou o tema do projeto?",
      placeholder="Ex: Preciso de ideias para o rebranding de uma cafeteria"
      " sustentável para o público jovem.",
  )

  if st.button("Gerar Insights"):
    if not briefing:
      st.warning("Por favor, informe o briefing ou tema para o brainstorm.")
    else:
      with st.spinner("Conectando referências e gerando ideias..."):
        try:
          prompt_completo = (
              f"Atue como um estrategista de marca e designer criativo. Para o"
              f" seguinte briefing: '{briefing}', forneça:\n"
              "1. Três conceitos criativos e visuais diferentes.\n"
              "2. Sugestão de paleta de cores (com códigos HEX exatos).\n"
              "3. Direção tipográfica recomendada.\n"
              "4. Ideias de aplicação rápida no mundo real (mockups,"
              " embalagens, posts, etc.)."
          )

          response = client.models.generate_content(
              model=MODELO, contents=prompt_completo
          )

          st.markdown("###  Resultados do Brainstorm:")
          st.markdown(response.text)
        except Exception as e:
=======
import os
from google import genai
from PIL import Image
import streamlit as st

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA E DESIGN CUSTOMIZADO (CSS)
# ==============================================================================
st.set_page_config(
    page_title="Assistente de Design | Criativo", page_icon="", layout="wide"
)

# Injetando CSS customizado para dar um visual profissional de design
st.markdown("""
    <style>
    /* Estilização geral dos botões principais */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.95;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    /* Arredondamento e suavização de inputs e textareas */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    
    /* Caixa de upload com visual mais limpo */
    .stFileUploader>div {
        border-radius: 8px;
        border: 2px dashed #cbd5e1;
    }
    
    /* Ajuste de títulos */
    h1, h2, h3 {
        letter-spacing: -0.5px;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# CONFIGURAÇÃO DA API KEY
# ==============================================================================
# O SDK busca automaticamente a variável 'GEMINI_API_KEY'
# Se preferir testar localmente colando a chave, descomente a linha abaixo:
# os.environ["GEMINI_API_KEY"] = "SUA_API_KEY_AQUI"

client = genai.Client()
MODELO = "gemini-3.8-flash"
# ==============================================================================

st.title(" Assistente Virtual para Design")
st.markdown(
    "Sua central de suporte inteligente para análises visuais, brainstormings"
    " e validação de conceitos."
)

# Menu lateral
menu = st.sidebar.selectbox(
    "Escolha a Ferramenta",
    ["Análise e Critique de Imagem", "Brainstorming & Conceitos"],
)

if menu == "Análise e Critique de Imagem":
  st.header(" Critique Visual de Layout")
  imagem_subida = st.file_uploader(
      "Envie a imagem do projeto (PNG, JPG)", type=["png", "jpg", "jpeg"]
  )
  pergunta = st.text_area(
      "O que você gostaria que o assistente avaliasse?",
      placeholder="Ex: Analise a hierarquia visual, a legibilidade da tipografia"
      " e o contraste.",
  )

  if st.button("Analisar Design"):
    if not imagem_subida:
      st.warning("Por favor, envie uma imagem antes de continuar.")
    elif not pergunta:
      st.warning("Por favor, digite o que você quer analisar na imagem.")
    else:
      with st.spinner("Analisando os detalhes visuais com IA..."):
        try:
          img = Image.open(imagem_subida)
          prompt_sistema = (
              "Você é um Diretor de Arte sênior e especialista em UI/UX e"
              " Design Gráfico. Faça uma análise construtiva, técnica e focada"
              " em usabilidade, hierarquia visual e estética da imagem enviada."
          )

          response = client.models.generate_content(
              model=MODELO, contents=[img, prompt_sistema, pergunta]
          )

          st.markdown("###  Parecer do Especialista:")
          st.markdown(response.text)
        except Exception as e:
          st.error(f"Erro ao processar a imagem: {e}")

elif menu == "Brainstorming & Conceitos":
  st.header(" Gerador de Ideias & Brainstorm")
  briefing = st.text_area(
      "Qual é o briefing ou o tema do projeto?",
      placeholder="Ex: Preciso de ideias para o rebranding de uma cafeteria"
      " sustentável para o público jovem.",
  )

  if st.button("Gerar Insights"):
    if not briefing:
      st.warning("Por favor, informe o briefing ou tema para o brainstorm.")
    else:
      with st.spinner("Conectando referências e gerando ideias..."):
        try:
          prompt_completo = (
              f"Atue como um estrategista de marca e designer criativo. Para o"
              f" seguinte briefing: '{briefing}', forneça:\n"
              "1. Três conceitos criativos e visuais diferentes.\n"
              "2. Sugestão de paleta de cores (com códigos HEX exatos).\n"
              "3. Direção tipográfica recomendada.\n"
              "4. Ideias de aplicação rápida no mundo real (mockups,"
              " embalagens, posts, etc.)."
          )

          response = client.models.generate_content(
              model=MODELO, contents=prompt_completo
          )

          st.markdown("###  Resultados do Brainstorm:")
          st.markdown(response.text)
        except Exception as e:
>>>>>>> 9f2938299010ab3f9a9062187cd0197aa06891ce
          st.error(f"Erro ao gerar ideias: {e}")