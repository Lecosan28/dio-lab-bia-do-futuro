# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|----------|----------|----------|
| `conceitos_financeiros.json` | JSON | Base de conhecimento utilizada para explicar conceitos financeiros em linguagem simples, como CDI, CDB, Tesouro Selic, liquidez, inflação, juros compostos, rentabilidade e diversificação. |
| `metas_financeiras.json` | JSON | Contém exemplos de metas financeiras que auxiliam o agente na elaboração de estratégias de planejamento e educação financeira. |
| `produtos_renda_fixa.json` | JSON | Reúne informações sobre produtos financeiros de renda fixa, suas características, liquidez, objetivos de uso e riscos associados. |
| `regras_reserva_emergencia.json` | JSON | Define as regras utilizadas pelo agente para orientar o cálculo da reserva de emergência conforme a situação financeira e profissional do usuário. |

---

# Objetivo da Base de Conhecimento

A base de conhecimento fornece informações estruturadas para que o SmartFinance AI gere respostas mais consistentes, educativas e seguras.

Os dados são utilizados para:

* Explicar conceitos financeiros em linguagem acessível;
* Auxiliar no cálculo da reserva de emergência;
* Apoiar o planejamento de metas financeiras;
* Apresentar características de produtos financeiros;
* Orientar usuários iniciantes em educação financeira;
* Reduzir o risco de respostas incorretas ou inventadas;
* Fornecer contexto para recomendações educativas.

Diferentemente das versões iniciais do projeto, o agente não depende mais de perfis financeiros pré-cadastrados.

Os dados financeiros são informados diretamente pelo usuário durante a utilização da aplicação e armazenados na memória da sessão, permitindo análises personalizadas em tempo real.

---

# Fontes de Informação

A base de conhecimento é composta por dados simulados (mockados), criados exclusivamente para fins educacionais e demonstração do funcionamento do agente.

As informações utilizadas seguem conceitos amplamente difundidos em educação financeira e planejamento financeiro pessoal, incluindo:

* Reserva de emergência;
* Planejamento financeiro pessoal;
* Renda fixa;
* Tesouro Selic;
* CDB;
* LCI/LCA;
* CDI;
* Liquidez;
* Rentabilidade;
* Inflação;
* Juros compostos;
* Diversificação básica de investimentos.

Os dados não representam recomendações financeiras reais, não possuem atualização em tempo real e são utilizados exclusivamente para fins acadêmicos e demonstração do projeto SmartFinance AI.

---

# Adaptações Realizadas no Projeto

Durante o desenvolvimento do SmartFinance AI, a estrutura da base de conhecimento foi simplificada para tornar o agente mais flexível e próximo de uma aplicação real.

As principais adaptações realizadas foram:

* Remoção do arquivo `perfil_investidor.json`;
* Remoção do arquivo `historico_atendimento.csv`;
* Remoção do arquivo `produtos_financeiros.json`;
* Remoção do arquivo `transacoes.csv`;
* Criação do arquivo `conceitos_financeiros.json`;
* Criação do arquivo `metas_financeiras.json`;
* Criação do arquivo `produtos_renda_fixa.json`;
* Criação do arquivo `regras_reserva_emergencia.json`;
* Eliminação da dependência de usuários fictícios pré-cadastrados;
* Substituição dos perfis simulados por dados informados em tempo real pelo usuário;
* Implementação de memória de sessão para armazenar informações fornecidas durante a conversa;
* Foco em educação financeira, planejamento financeiro e reserva de emergência;
* Utilização exclusiva de bases de conhecimento voltadas para conceitos, metas, produtos financeiros e regras financeiras.

Essas alterações tornaram o agente mais adaptável a diferentes usuários, permitindo recomendações personalizadas sem depender de dados previamente cadastrados.

---

# Estratégia de Integração

## Como os dados são carregados?

Os arquivos JSON localizados na pasta `data/` são carregados no início da execução do agente.

Os dados são convertidos para estruturas internas do Python (dicionários e listas) e permanecem disponíveis durante toda a sessão.

Dessa forma, o agente pode consultar conceitos financeiros, metas financeiras, produtos de renda fixa e regras de reserva de emergência sempre que necessário.

---

## Exemplo de Carregamento da Base de Conhecimento

```python

with open("../data/metas_financeiras.json", "r", encoding="utf-8") as f:
    produtos_renda_fixa = json.load(f)

with open("../data/produtos_renda_fixa.json", "r", encoding="utf-8") as f:
    produtos_renda_fixa = json.load(f)

with open("../data/conceitos_financeiros.json", "r", encoding="utf-8") as f:
    conceitos_financeiros = json.load(f)

with open("../data/regras_reserva_emergencia.json", "r", encoding="utf-8") as f:
    regras_reserva = json.load(f)

print("Base de conhecimento carregada com sucesso!")

print("Base de conhecimento carregada com sucesso!")
```

---

## Como os dados são utilizados pelo agente?

As informações da base de conhecimento são incorporadas dinamicamente ao contexto enviado ao modelo de IA.

Além disso, os dados fornecidos pelo usuário durante a conversa são armazenados na memória da sessão, permitindo continuidade no atendimento.

Exemplos de informações utilizadas:

* Renda mensal informada pelo usuário;
* Despesas mensais informadas pelo usuário;
* Valor atual da reserva de emergência;
* Objetivos financeiros mencionados durante a conversa;
* Conceitos financeiros necessários para responder perguntas;
* Produtos financeiros presentes na base de conhecimento;
* Regras de cálculo da reserva de emergência.

Essa abordagem permite que o agente funcione como um assistente financeiro conversacional, mantendo contexto e evitando perguntas repetidas.

---

# Exemplo de Contexto Montado

```text
DADOS FINANCEIROS DO USUÁRIO

- Renda Mensal: R$ 4.500
- Despesas Mensais: R$ 2.800
- Reserva Atual: R$ 5.000

MEMÓRIA DA CONVERSA

- Objetivo: Comprar uma moto
- Prazo desejado: 36 meses

REGRAS DE RESERVA DE EMERGÊNCIA

- Recomenda-se entre 6 e 12 meses de despesas
- Valor mínimo sugerido: R$ 16.800

PRODUTOS FINANCEIROS DISPONÍVEIS

- Tesouro Selic
- CDB com Liquidez Diária
- LCI/LCA

INSTRUÇÕES DO SISTEMA

- Não prometer rentabilidade.
- Não inventar informações.
- Priorizar educação financeira.
- Utilizar informações já fornecidas pelo usuário.
- Solicitar apenas os dados que ainda não foram informados.
```

---

# Evolução da Arquitetura

A versão inicial do projeto utilizava usuários fictícios e dados financeiros previamente cadastrados.

Na versão final, o SmartFinance AI passou a utilizar:

* Dados financeiros fornecidos em tempo real;
* Memória estruturada da conversa;
* Histórico persistente da sessão;
* Atualização dinâmica das informações do usuário;
* Planejamento financeiro contextualizado.

Essa evolução aproximou o projeto do comportamento esperado de um agente financeiro real, capaz de acompanhar o contexto da conversa e fornecer orientações mais consistentes e personalizadas.
