---
title: "Validador de CPF"
seoTitle: "Validador de CPF Online: confira se um CPF é válido"
description: "Validador de CPF online e gratuito: digite um CPF e confira na hora se os dígitos verificadores estão corretos. Sem enviar dados."
layout: "validador"
faq:
  - q: "O validador diz se o CPF existe?"
    a: "Não. Ele só confere a conta matemática dos dígitos verificadores. Para saber se o CPF existe e está regular, consulte a Receita Federal com CPF e data de nascimento."
  - q: "Posso digitar com ou sem pontos e traço?"
    a: "Sim. O validador ignora a pontuação e considera apenas os dígitos."
  - q: "Meus dados ficam salvos?"
    a: "Não. A conferência acontece no seu navegador e o número não é enviado a nenhum servidor."
  - q: "Por que 111.111.111-11 aparece como inválido?"
    a: "Ele passa na conta do módulo 11, mas sequências de dígitos repetidos costumam ser rejeitadas pelos sistemas, então o validador as trata como inválidas."
---

## Como o validador confere o CPF

1. Remove a pontuação e mantém só os dígitos.
2. Confere se há exatamente 11 dígitos e se não são todos iguais.
3. Recalcula o 10º dígito a partir dos nove primeiros, pelo módulo 11.
4. Recalcula o 11º dígito a partir dos dez primeiros.
5. Compara os dois dígitos calculados com os informados.

O cálculo completo, com exemplo, está em [como calcular os dígitos verificadores](/glossario/digito-verificador/), e o passo a passo em [como validar um CPF](/glossario/validacao-de-cpf/).

## O que um CPF válido não prova

A validação só detecta erros de digitação. Um CPF válido pode não existir na base da Receita Federal ou pertencer a alguém que você não conhece. Para conferir a situação de um CPF real, veja [como consultar a situação do CPF](/glossario/consulta-de-cpf/).

## Exemplos para testar

| CPF | Resultado esperado |
|---|---|
| 123.456.789-09 | Válido (exemplo de formato) |
| 012.345.678-90 | Válido (começa com zero) |
| 123.456.789-10 | Inválido (dígito verificador errado) |
| 111.111.111-11 | Inválido (dígitos repetidos) |
| 1234 | Inválido (tamanho) |

Precisa de números para testar? Use o [gerador de CPF](/).
