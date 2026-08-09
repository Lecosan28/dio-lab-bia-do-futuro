# Base de Conhecimento

## Dados Utilizados

| Arquivo                          | Formato | Utilização no Agente                                                                                                                                                  |
| -------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `perfil_usuario.json`            | JSON    | Armazena perfis de usuários fictícios contendo idade, profissão, renda mensal, despesas mensais e perfil de risco. Permite personalizar as recomendações do agente.   |
| `metas_financeiras.json`         | JSON    | Contém diferentes objetivos financeiros, como reserva de emergência, notebook, moto, viagem, pós-graduação e entrada de imóvel, com valores e prazos de referência.   |
| `produtos_renda_fixa.json`       | JSON    | Reúne informações sobre produtos financeiros adequados a diferentes perfis e objetivos, incluindo Tesouro Selic, CDB, LCI/LCA e Fundos Imobiliários.                  |
| `conceitos_financeiros.json`     | JSON    | Base de conhecimento utilizada para explicar conceitos financeiros como CDI, CDB, Tesouro Selic, liquidez, inflação, rentabilidade, diversificação e juros compostos. |
| `regras_reserva_emergencia.json` | JSON    | Define regras utilizadas pelo agente para calcular a reserva de emergência recomendada de acordo com a situação profissional do usuário.                              |
| `historico_planejamento.csv`     | CSV     | Armazena exemplos de planejamentos financeiros realizados, incluindo metas, aportes mensais e prazos, permitindo análises comparativas e simulações.                  |
| `gastos_mensais.csv`             | CSV     | Contém registros de despesas organizadas por categoria, possibilitando identificar padrões de gastos e oportunidades de economia.                                     |

## Objetivo da Base de Conhecimento

A base de conhecimento fornece informações estruturadas para que o SmartFinance AI gere respostas mais consistentes, personalizadas e seguras.

Os dados são utilizados para:

* Compreender o perfil financeiro do usuário;
* Personalizar recomendações de acordo com renda, despesas e perfil de risco;
* Calcular reservas de emergência;
* Planejar metas financeiras de curto, médio e longo prazo;
* Explicar conceitos financeiros em linguagem acessível;
* Sugerir produtos financeiros compatíveis com os objetivos informados;
* Identificar oportunidades de economia a partir dos padrões de gastos;
* Reduzir riscos de respostas incorretas ou sem contexto.

## Fontes de Informação

A base de conhecimento é composta por dados simulados (mockados) criados exclusivamente para fins educacionais e demonstração do funcionamento do agente.

As informações financeiras utilizadas seguem conceitos amplamente difundidos em educação financeira e planejamento financeiro pessoal, incluindo:

* Reserva de emergência;
* Planejamento financeiro pessoal;
* Perfil de risco;
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

## Adaptações nos Dados

A base de conhecimento original foi expandida para representar cenários mais próximos de situações reais de planejamento financeiro.

As principais adaptações realizadas foram:

* Criação de múltiplos perfis de usuários com diferentes profissões, níveis de renda e perfis de risco;
* Inclusão de diversas metas financeiras, como reserva de emergência, compra de notebook, moto, viagem, pós-graduação e entrada de imóvel;
* Estruturação de uma base de produtos financeiros com informações sobre perfil recomendado, liquidez e objetivo de uso;
* Ampliação da base de conceitos financeiros para apoiar explicações educativas durante as interações;
* Criação de regras específicas para cálculo da reserva de emergência conforme a situação profissional do usuário;
* Inclusão de históricos de planejamento financeiro para permitir simulações e análises comparativas;
* Inclusão de registros de gastos categorizados para identificação de padrões de consumo e oportunidades de economia.

Essas adaptações tornam o agente mais capaz de gerar respostas personalizadas, contextualizadas e alinhadas aos objetivos financeiros dos usuários.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV localizados na pasta `data/` são carregados no início da execução do agente.

Os dados são convertidos para estruturas de dados internas (listas e dicionários) e permanecem disponíveis durante toda a sessão. Dessa forma, o agente pode consultar informações sobre perfis financeiros, metas, produtos financeiros, conceitos financeiros, regras de reserva de emergência e históricos de planejamento sempre que necessário.

### Como os dados são usados no prompt?

Os dados são utilizados de duas formas:

1. **Contexto fixo (System Prompt):**

   * Regras de negócio;
   * Regras de segurança;
   * Conceitos financeiros básicos;
   * Limitações do agente.

2. **Contexto dinâmico:**

   * Perfil do usuário;
   * Objetivos financeiros;
   * Gastos informados;
   * Histórico de planejamento;
   * Produtos financeiros compatíveis com o perfil.

Antes de gerar uma resposta, o agente seleciona apenas as informações mais relevantes para a solicitação atual e as inclui no contexto enviado ao modelo de IA.

Essa estratégia reduz o volume de informações processadas e melhora a qualidade das respostas.

---

## Exemplo de Contexto Montado

> Exemplo de contexto enviado ao agente antes da geração da resposta.

```text
Perfil do Usuário

- Profissão: Desenvolvedor Júnior
- Idade: 24 anos
- Perfil de Risco: Moderado
- Renda Mensal: R$ 4.500
- Despesas Mensais: R$ 2.800

Objetivo Financeiro

- Meta: Comprar um notebook
- Valor da Meta: R$ 5.000
- Prazo: 12 meses

Regras de Reserva de Emergência

- Reserva recomendada: 6 meses de despesas
- Valor recomendado: R$ 16.800

Produtos Compatíveis

- Tesouro Selic
- CDB com Liquidez Diária
- LCI/LCA

Conceitos Relevantes

- Liquidez: facilidade de converter um investimento em dinheiro.
- Reserva de Emergência: valor destinado a imprevistos financeiros.

Instruções ao Agente

- Priorizar educação financeira.
- Não prometer rentabilidade.
- Não realizar recomendações sem contexto suficiente.
- Solicitar mais informações quando necessário.
```
