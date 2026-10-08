---
title: "Estrutura do CPF"
pergunta: "Como é a estrutura do CPF?"
description: "Veja como cada um dos 11 dígitos do CPF é formado: oito dígitos-base aleatórios, um dígito de região fiscal e dois dígitos verificadores calculados pelo módulo 11."
definicao: "O CPF tem 11 dígitos decimais: oito dígitos-base atribuídos aleatoriamente na inscrição, um nono dígito que indica a região fiscal e dois dígitos verificadores calculados pelo módulo 11. A pontuação — pontos e hífen — é apenas apresentação; 12345678909 e 123.456.789-09 são o mesmo CPF."
date: 2026-09-29
lastmod: 2026-10-08
aliases:
  - /artigos/estrutura-do-cpf/
faq:
  - q: "O CPF revela idade, nome ou cidade?"
    a: "Não. Os dígitos-base são sorteados e o nono dígito indica apenas a região fiscal da inscrição."
  - q: "A pontuação faz parte do CPF?"
    a: "Não. É só apresentação: 12345678909 e 123.456.789-09 são o mesmo CPF."
---
Olhando para 123.456.789-09, é fácil tratar o CPF como um bloco opaco de números. Mas cada posição tem uma função definida: os oito primeiros dígitos são aleatórios, o nono identifica a região fiscal e os dois últimos garantem a integridade do número por meio de cálculo matemático.

## Os onze dígitos e suas funções

| Posição | Função |
|---|---|
| 1º ao 8º | Dígitos-base, atribuídos aleatoriamente no momento da inscrição |
| 9º | [Região fiscal](/glossario/regiao-fiscal/) responsável pela inscrição |
| 10º e 11º | [Dígitos verificadores](/glossario/digito-verificador/), calculados por um algoritmo público da Receita Federal |

## Lendo um CPF real

Em 123.456.789-09, o segmento 12345678 é a base aleatória, o **9** é o nono dígito — correspondente à 9ª região fiscal, que reúne PR e SC — e **09** são os verificadores calculados a partir dos nove primeiros dígitos. Este número é apenas ilustrativo, usado na própria descrição pública do formato.

## Pontuação e dígitos brutos

Os nove primeiros dígitos formam três grupos de três, separados por ponto. Depois vem um hífen e os dois últimos dígitos: `123.456.789-09`. Sem formatação, o mesmo CPF é `12345678909`. Os dois formatos representam exatamente o mesmo número; sistemas devem aceitar ambos e normalizar antes de qualquer validação.

## O que o CPF não diz sobre você

Como o número é vitalício e só muda por decisão judicial, o nono dígito não se atualiza quando a pessoa muda de estado. Os dígitos-base são sorteados, sem relação com nome, data de nascimento ou cidade. Para o contexto geral do cadastro, veja [CPF](/glossario/cpf/).
