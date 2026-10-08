---
title: "Dígito verificador do CPF"
pergunta: "Como calcular os dígitos verificadores do CPF?"
description: "Passo a passo para calcular o 10º e o 11º dígito do CPF pelo módulo 11, com exemplo numérico completo, tabela de pesos e a regra do resto menor que 2."
definicao: "Os dois últimos dígitos do CPF são calculados a partir dos anteriores por uma soma ponderada e pelo resto da divisão por 11 (módulo 11). O 10º dígito usa os nove primeiros; o 11º usa os dez primeiros, incluindo o primeiro verificador."
date: 2026-09-29
lastmod: 2026-10-08
aliases:
  - /artigos/como-calcular-digitos-verificadores-cpf/
faq:
  - q: "Qual a regra do resto no módulo 11?"
    a: "Se o resto da divisão da soma por 11 for menor que 2, o dígito é 0. Caso contrário, o dígito é 11 menos o resto."
  - q: "Por que o CPF tem dois dígitos verificadores?"
    a: "Porque o cálculo pode resultar em 10, representado por 0, o que enfraquece a verificação. O segundo dígito ajuda a compensar."
---
Todo sistema de cadastro precisa detectar erros de digitação. O CPF resolve isso com dois dígitos no final do número, calculados matematicamente a partir dos nove anteriores. Se alguém trocar ou transpor um dígito, os verificadores não batem — e o número é rejeitado. O método usado é o módulo 11, o mesmo que o [CNPJ](/glossario/cnpj/) usa, com pesos diferentes.

## A fórmula

1. Multiplique cada dígito por um peso e some os resultados.
2. Divida a soma por 11 e pegue o resto.
3. Se o resto for menor que 2, o dígito é 0. Caso contrário, o dígito é 11 menos o resto.

## Calculando o décimo dígito

Use os 9 primeiros dígitos com pesos de 10 a 2. Para 123.456.789:

| Dígito | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Peso | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 |
| Produto | 10 | 18 | 24 | 28 | 30 | 30 | 28 | 24 | 18 |

A soma é 210. O resto de 210 dividido por 11 é 1, que é menor que 2, então o primeiro dígito é **0**.

## Calculando o décimo primeiro dígito

Agora use 10 dígitos (os nove primeiros mais o dígito calculado) com pesos de 11 a 2. Para 1234567890:

11 + 20 + 27 + 32 + 35 + 36 + 35 + 32 + 27 + 0 = 255

O resto de 255 dividido por 11 é 2, e 11 − 2 = **9**. O CPF completo é 123.456.789-09.

## Por que dois verificadores

Como 11 é primo, o método detecta erros de digitação e troca de posição entre dígitos. Porém, o cálculo pode resultar em 10, e a Receita Federal determinou que esse valor seja representado por 0. Isso enfraquece um pouco a verificação, e o segundo dígito foi adicionado para compensar essa limitação.

## Notas técnicas

- Existem formulações equivalentes do mesmo cálculo, com pesos em ordem inversa. Todas chegam aos mesmos dígitos.
- 012.345.678-90 é matematicamente válido, o que mostra que o cálculo aceita números com zero à esquerda.
- Sequências repetidas como 111.111.111-11 passam na conta, mas os sistemas costumam rejeitá-las por convenção.

Veja o código pronto em [JavaScript, Python e PHP](/glossario/algoritmo-do-cpf/). Para aplicar o cálculo na prática, consulte [validação de CPF](/glossario/validacao-de-cpf/).
