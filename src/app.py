import json
import requests
import streamlit as st

# =====================================
# CONFIGURAÇÃO
# =====================================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "minimax-m3:cloud"

# =====================================
# CARREGAR BASE DE CONHECIMENTO
# =====================================

with open("../data/metas_financeiras.json", "r", encoding="utf-8") as f:
    produtos_renda_fixa = json.load(f)

with open("../data/produtos_renda_fixa.json", "r", encoding="utf-8") as f:
    produtos_renda_fixa = json.load(f)

with open("../data/conceitos_financeiros.json", "r", encoding="utf-8") as f:
    conceitos_financeiros = json.load(f)

with open("../data/regras_reserva_emergencia.json", "r", encoding="utf-8") as f:
    regras_reserva = json.load(f)

print("Base de conhecimento carregada com sucesso!")

# =====================================
# SYSTEM PROMPT
# =====================================

SYSTEM_PROMPT = """
Você é o SmartFinance AI, um agente financeiro inteligente especializado em educação financeira, construção de reserva de emergência e planejamento de metas financeiras.

OBJETIVO

Ajudar usuários a organizar suas finanças pessoais, construir reservas de emergência e alcançar metas financeiras de forma segura, responsável e planejada.

REGRAS

- Utilize apenas as informações fornecidas pelo usuário e pela base de conhecimento.
- Nunca invente taxas, rentabilidades ou dados financeiros.
- Quando faltarem informações, solicite apenas os dados necessários.
- Nunca prometa ganhos financeiros.
- Nunca afirme que um investimento é garantidamente melhor que outro.
- Explique conceitos financeiros de forma simples e acessível.
- Priorize a reserva de emergência antes de outras metas.
- Diferencie fatos, cálculos e estimativas.
- Recomende orientação profissional quando apropriado.
- Responda de forma clara, objetiva e educativa.

COMPORTAMENTO PROATIVO

Identifique:

- Ausência de reserva de emergência;
- Gastos excessivos;
- Metas incompatíveis com a renda;
- Prazos irreais;
- Oportunidades de economia;
- Possíveis riscos financeiros.

SEGURANÇA

- Não invente informações.
- Não faça previsões de mercado.
- Não forneça aconselhamento financeiro profissional.
- Admita limitações quando necessário.

MEMÓRIA

Você possui uma memória estruturada.

Sempre consulte essa memória antes de fazer perguntas.

Nunca solicite novamente informações já registradas.

Se faltar alguma informação importante, solicite apenas o dado faltante.

Utilize o histórico da conversa e a memória para personalizar as respostas.
"""

# =====================================
# MEMÓRIA CONVERSACIONAL
# =====================================

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# =====================================
# MEMÓRIA ESTRUTURADA
# =====================================

if "perfil_financeiro" not in st.session_state:

    st.session_state.perfil_financeiro = {

        "renda_mensal": None,
        "despesas_mensais": None,
        "reserva_atual": None,
        "objetivo_financeiro": None,
        "valor_objetivo": None,
        "prazo_objetivo": None,
        "tipo_trabalho": None
    }

# =====================================
# FORMATAR MEMÓRIA
# =====================================

def memoria_formatada():

    memoria = st.session_state.perfil_financeiro

    return f"""
DADOS FINANCEIROS CONHECIDOS

Renda Mensal: {memoria['renda_mensal']}
Despesas Mensais: {memoria['despesas_mensais']}
Reserva Atual: {memoria['reserva_atual']}
Objetivo Financeiro: {memoria['objetivo_financeiro']}
Valor do Objetivo: {memoria['valor_objetivo']}
Prazo do Objetivo: {memoria['prazo_objetivo']}
Tipo de Trabalho: {memoria['tipo_trabalho']}
"""

# =====================================
# MONTAR CONTEXTO
# =====================================

def montar_contexto():

    memoria = memoria_formatada()

    contexto = f"""
SMARTFINANCE AI

{memoria}

=====================================
BASE DE CONHECIMENTO
=====================================

PRODUTOS DE RENDA FIXA

{json.dumps(produtos_renda_fixa, indent=2, ensure_ascii=False)}

CONCEITOS FINANCEIROS

{json.dumps(conceitos_financeiros, indent=2, ensure_ascii=False)}

REGRAS DE RESERVA DE EMERGÊNCIA

{json.dumps(regras_reserva, indent=2, ensure_ascii=False)}
"""

    return contexto

# =====================================
# HISTÓRICO
# =====================================

def montar_historico():

    historico = ""

    for msg in st.session_state.mensagens:

        papel = (
            "USUÁRIO"
            if msg["role"] == "user"
            else "ASSISTENTE"
        )

        historico += f"{papel}: {msg['content']}\n\n"

    return historico

# =====================================
# ATUALIZAR MEMÓRIA
# =====================================

def atualizar_memoria(renda, despesas, reserva):

    memoria = st.session_state.perfil_financeiro

    if renda > 0:
        memoria["renda_mensal"] = renda

    if despesas > 0:
        memoria["despesas_mensais"] = despesas

    if reserva >= 0:
        memoria["reserva_atual"] = reserva

# =====================================
# CONSULTAR MODELO
# =====================================

def perguntar(msg):

    contexto = montar_contexto()

    historico = montar_historico()

    memoria = memoria_formatada()

    prompt = f"""
{SYSTEM_PROMPT}

=====================================
MEMÓRIA ESTRUTURADA
=====================================

{memoria}

=====================================
BASE DE CONHECIMENTO
=====================================

{contexto}

=====================================
HISTÓRICO DA CONVERSA
=====================================

{historico}

=====================================
PERGUNTA ATUAL
=====================================

{msg}

=====================================
INSTRUÇÕES FINAIS
=====================================

Utilize a memória estruturada.

Não solicite novamente informações já registradas.

Caso falte alguma informação:

- Solicite apenas o dado faltante.
- Não faça suposições.

Se o usuário perguntar sobre investimentos:

- Explique riscos.
- Não prometa rentabilidade.
- Não faça previsões.

Se a reserva de emergência for insuficiente:

- Priorize sua construção.

Sempre explique cálculos quando aplicável.

Responda de forma educativa, clara e objetiva.
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    resposta.raise_for_status()

    return resposta.json()["response"]

# =====================================
# INTERFACE
# =====================================

st.set_page_config(
    page_title="SmartFinance AI",
    page_icon="💰",
    layout="centered"
)

st.title("💰 SmartFinance AI")

st.markdown("""
Assistente Financeiro Inteligente para:

✅ Construção de Reserva de Emergência

✅ Planejamento de Metas Financeiras

✅ Educação Financeira
""")

# =====================================
# LIMPAR CONVERSA
# =====================================

if st.button("🗑️ Limpar conversa"):

    st.session_state.mensagens = []

    st.session_state.perfil_financeiro = {

        "renda_mensal": None,
        "despesas_mensais": None,
        "reserva_atual": None,
        "objetivo_financeiro": None,
        "valor_objetivo": None,
        "prazo_objetivo": None,
        "tipo_trabalho": None
    }

    st.rerun()

# =====================================
# DADOS DO USUÁRIO
# =====================================

st.divider()

st.subheader("Informe seus dados financeiros")

renda_mensal = st.number_input(
    "Renda Mensal (R$)",
    min_value=0.0,
    step=100.0
)

despesas_mensais = st.number_input(
    "Despesas Mensais (R$)",
    min_value=0.0,
    step=100.0
)

reserva_atual = st.number_input(
    "Reserva de Emergência Atual (R$)",
    min_value=0.0,
    step=100.0
)

atualizar_memoria(
    renda_mensal,
    despesas_mensais,
    reserva_atual
)

# =====================================
# EXIBIR HISTÓRICO
# =====================================

st.divider()

for msg in st.session_state.mensagens:

    with st.chat_message(msg["role"]):

        st.write(msg["content"])

# =====================================
# CHAT
# =====================================

pergunta = st.chat_input(
    "Digite sua dúvida financeira..."
)

if pergunta:

    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    st.chat_message("user").write(pergunta)

    with st.spinner(
        "Analisando sua situação financeira..."
    ):

        try:

            resposta = perguntar(pergunta)

            st.session_state.mensagens.append(
                {
                    "role": "assistant",
                    "content": resposta
                }
            )

            st.chat_message(
                "assistant"
            ).write(resposta)

        except Exception as erro:

            st.error(
                f"Erro ao consultar o modelo: {erro}"
            )