# Código da Aplicação

Esta pasta contém o código-fonte do projeto **SmartFinance AI**, um agente financeiro inteligente voltado para educação financeira, planejamento financeiro e construção de reserva de emergência.

## Estrutura da Pasta

```text
src/
└── app.py
```

### app.py

Arquivo principal da aplicação.

Responsável por:

- Construir a interface web utilizando Streamlit;
- Coletar informações financeiras do usuário;
- Gerenciar a memória estruturada da conversa;
- Consultar a base de conhecimento financeira;
- Montar o contexto enviado ao modelo de IA;
- Realizar a comunicação com o Ollama;
- Exibir respostas personalizadas ao usuário.

---

## Tecnologias Utilizadas

- Python
- Streamlit
- Ollama
- Requests
- JSON

---

## Dependências

Exemplo do arquivo `requirements.txt`:

```text
streamlit
requests
```

---

## Base de Conhecimento Utilizada

A aplicação consulta os seguintes arquivos localizados na pasta `data/`:

```text
data/
├── conceitos_financeiros.json
├── metas_financeiras.json
├── produtos_renda_fixa.json
└── regras_reserva_emergencia.json
```

Esses arquivos fornecem informações utilizadas pelo agente para:

- Explicar conceitos financeiros;
- Planejar metas financeiras;
- Calcular reservas de emergência;
- Apresentar produtos financeiros de forma educativa.

---

## Como Executar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar o Ollama

Verifique se o Ollama está em execução localmente.

Exemplo:

```bash
ollama serve
```

### 3. Executar a aplicação

A partir da raiz do projeto:

```bash
python -m streamlit run src/app.py
```

ou

```bash
py -m streamlit run src/app.py
```

---

## Funcionalidades

- Planejamento financeiro personalizado;
- Cálculo de reserva de emergência;
- Educação financeira;
- Memória estruturada da conversa;
- Explicação de conceitos financeiros;
- Simulação de metas financeiras;
- Recomendações educativas baseadas no contexto do usuário;
- Estratégias de segurança para redução de alucinações da IA.

---

## Observação

O SmartFinance AI possui finalidade exclusivamente educacional.

As respostas fornecidas não constituem consultoria financeira profissional, recomendação de investimentos ou garantia de rentabilidade futura.
