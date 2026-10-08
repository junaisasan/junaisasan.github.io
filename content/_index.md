---
title: "Gerador de CPF"
seoTitle: "Gerador de CPF"
description: "Gerador de CPF online: gere um CPF válido e aleatório, com ou sem pontuação e por estado. Grátis, para testes de software."
faq:
  - q: "O CPF gerado é real?"
    a: "Não. Ele é matematicamente válido, mas fictício. Como a combinação é aleatória, pode coincidir com o CPF de uma pessoa real, por isso não deve ser usado em cadastros de verdade."
  - q: "Posso usar o CPF gerado para me cadastrar em sites ou serviços?"
    a: "Não. O gerador serve para testar sistemas, formulários e validações. Usar números gerados para fraude ou identidade falsa é indevido."
  - q: "Como o dígito verificador do CPF é calculado?"
    a: "Cada um dos dois últimos dígitos vem de uma soma ponderada dos dígitos anteriores, com o resto da divisão por 11 (módulo 11). O segundo dígito usa o primeiro no cálculo."
  - q: "O que o nono dígito do CPF indica?"
    a: "A região fiscal em que o CPF foi inscrito. Por isso o gerador permite escolher o estado de origem."
  - q: "Por que 111.111.111-11 é tratado como inválido?"
    a: "Sequências de dígitos repetidos passam na conta do módulo 11, mas costumam ser rejeitadas pelos sistemas na prática. Este gerador evita esse tipo de número."
  - q: "Como gerar vários CPFs de uma vez?"
    a: "Escolha a quantidade (de 1 a 100) antes de clicar em Gerar CPF. Os números saem em lista, sem repetição, e você pode copiar tudo de uma vez."
  - q: "Posso baixar os CPFs gerados em CSV?"
    a: "Sim. Ao gerar mais de um CPF aparece o botão Baixar CSV. O arquivo é montado no seu navegador, sem enviar nada a servidor algum."
  - q: "Como gerar CPF sem pontuação?"
    a: "Marque Não em Gerar com pontuação. O número sai só com os 11 dígitos, no formato usado em campos de banco de dados e APIs."
  - q: "Como gerar um CPF de um estado específico?"
    a: "Escolha o estado em Estado de origem. O gerador usa o nono dígito da região fiscal correspondente, por exemplo 8 para São Paulo."
---

## Gerador de CPF: gere um CPF válido em segundos

Este gerador de CPF cria números com 11 dígitos no formato correto e com os dois [dígitos verificadores](/glossario/digito-verificador/) calculados pelo módulo 11. Você pode gerar com ou sem pontuação e escolher o estado de origem. Os números são fictícios, só para testes.

Quem busca por gerador cpf ou gerador de CPF online costuma precisar disso para testar formulários, cadastros e [validações de CPF](/glossario/validacao-de-cpf/).

## O que é um CPF válido?

Um CPF válido é aquele em que os dois últimos dígitos batem com o cálculo feito sobre os anteriores. O [CPF](/glossario/cpf/) tem onze dígitos: oito são atribuídos de forma aleatória na inscrição, o nono indica a [região fiscal](/glossario/regiao-fiscal/) e os dois últimos são verificadores. A [estrutura do CPF](/glossario/estrutura-do-cpf/) detalha o que cada posição significa.

Muita gente pesquisa por “cpf valido” ou “cpf aleatorio valido” sem acento, mas a ideia é a mesma: um número que passa na validação. Ser válido não significa estar registrado em nome de alguém. Para conferir um número, use o [validador de CPF](/validador-de-cpf/).

## Como funciona o gerador de CPF

1. Sorteia oito dígitos.
2. Define o nono dígito: o da [região fiscal](/glossario/regiao-fiscal/) do estado escolhido, ou aleatório se você deixar “Indiferente”.
3. Calcula o primeiro e o segundo dígito verificador pelo [módulo 11](/glossario/digito-verificador/).
4. Aplica a pontuação, se você pediu: o número 12345678909 vira 123.456.789-09.

Quem quer reproduzir a conta em código encontra funções prontas no [algoritmo do CPF](/glossario/algoritmo-do-cpf/), em JavaScript, Python e PHP.

## CPF aleatório válido: para que serve (e para que não serve)

Serve para testes de software, demonstrações, preenchimento de formulários em ambiente de desenvolvimento e aulas de programação. O verbete sobre [CPF para testes de software](/glossario/cpf-para-testes/) explica por que usar números gerados em vez de CPFs reais.

Não serve para cadastros reais, comprovação de identidade ou qualquer tipo de [fraude de identidade](/glossario/fraude-de-identidade/). Usar números gerados para criar uma identidade falsa é indevido.

## Gerar CPF por estado, sem pontuação e em massa

Além do CPF avulso, o gerador aceita três ajustes que costumam ser pedidos em testes:

- **Por estado:** o nono dígito segue a [região fiscal](/glossario/regiao-fiscal/) do estado escolhido. A tabela completa está mais abaixo.
- **Sem pontuação:** só os 11 dígitos, pronto para colar em um campo de banco de dados ou em uma requisição de API.
- **Em massa:** gere até 100 CPFs sem repetição, copie a lista inteira ou baixe em CSV para importar em planilhas e ferramentas de teste.

## Boas práticas ao usar CPF gerado em testes

Use sempre números gerados em ambientes de teste e mantenha-os separados da produção. Os casos de teste mais úteis (sem pontuação, dígito errado, sequências repetidas, zero à esquerda) estão em [CPF para testes de software](/glossario/cpf-para-testes/), e o [algoritmo do CPF](/glossario/algoritmo-do-cpf/) traz o código. Para checar um número que você já tem, use o [validador de CPF](/validador-de-cpf/).

## CPF válido não é CPF existente

A conta do módulo 11 só detecta erro de digitação. Um número pode passar na validação e não estar inscrito em nenhum cadastro, ou coincidir com o de uma pessoa real. Quem precisa conferir a situação de um CPF de verdade deve seguir o passo a passo da [consulta de CPF](/glossario/consulta-de-cpf/), direto no site da [Receita Federal](/glossario/receita-federal/).

O resultado da consulta pode ser regular, pendente, suspensa, cancelada ou nula. Cada uma está explicada em [situação cadastral do CPF](/glossario/situacao-cadastral/).

## O CPF em números

Alguns números ajudam a dimensionar o CPF no Brasil. Cada um tem fonte e data, e os períodos e escopos são diferentes, então não devem ser somados:

- A [Serpro](/glossario/serpro/) informa 226 milhões de CPFs ativos, incluindo brasileiros e estrangeiros (2026). Veja as [estatísticas da base de CPFs](/estatisticas/base-de-cpfs/).
- Até 12 de junho de 2026, mais de 55,8 milhões de [CIN](/glossario/cin/) haviam sido emitidas, segundo o Ministério da Justiça. Veja as [estatísticas da CIN](/estatisticas/cin/).
- A Serasa Experian registrou 476.060 tentativas de [fraude de identidade](/glossario/fraude-de-identidade/) em fluxos de cadastro em maio de 2026, uma a cada 5,6 segundos. Veja as [estatísticas de fraude de identidade](/estatisticas/fraude-de-identidade/).
- A Receita Federal recebeu 44.498.717 declarações de [IRPF](/glossario/irpf/) em 2026, e havia 70.085.591 [CNPJs](/glossario/cnpj/) registrados em setembro de 2026, dos quais 26.937.244 ativos. Veja as [estatísticas de declarações e CNPJ](/estatisticas/declaracoes-e-cnpj/).

O [painel de estatísticas do CPF](/estatisticas/) reúne todos os números, com data, fonte e ressalvas.

## CPF, identidade e outros documentos

A [inscrição no CPF](/glossario/inscricao-no-cpf/) é obrigatória em situações como relação tributária, conta bancária e benefício do INSS, e voluntária nos demais casos. Desde a [Lei 14.534/2023](/glossario/lei-14534/), o CPF é o número único de identificação em documentos oficiais, e a CIN o adota como número. A diferença entre os documentos está em [CPF, CNPJ, RG e CIN](/glossario/cpf-cnpj-rg-cin/).

Para assinar documentos digitalmente com validade jurídica, existe o [e-CPF](/glossario/e-cpf/), que usa o mesmo número. Todos os termos estão no [glossário do CPF](/glossario/).

## CPF generator: how it works

This CPF generator produces random Brazilian taxpayer numbers that pass the standard check-digit validation (modulo 11). The numbers are fictional and meant only for software testing and development.

## Estrutura do CPF e região fiscal

O nono dígito indica a [região fiscal](/glossario/regiao-fiscal/) responsável pela inscrição (veja também a [estrutura do CPF](/glossario/estrutura-do-cpf/)):

| Nono dígito | Estados |
|---|---|
| 1 | DF, GO, MT, MS, TO |
| 2 | AC, AP, AM, PA, RO, RR |
| 3 | CE, MA, PI |
| 4 | AL, PB, PE, RN |
| 5 | BA, SE |
| 6 | MG |
| 7 | ES, RJ |
| 8 | SP |
| 9 | PR, SC |
| 0 | RS |

## Infográfico: CPF, muito além de 11 números

{{< infographic >}}
