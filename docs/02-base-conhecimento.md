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

A base de conhecimento fornece informações estruturadas para que o FinPlan AI gere respostas mais consistentes, personalizadas e seguras.

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

Os dados não representam recomendações financeiras reais, não possuem atualização em tempo real e são utilizados exclusivamente para fins acadêmicos e demonstração do projeto FinPlan AI.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
