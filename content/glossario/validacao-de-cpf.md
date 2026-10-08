---
title: "Validação de CPF"
pergunta: "Como validar um CPF?"
description: "Aprenda a diferença entre validar e consultar um CPF, o passo a passo para checar os dígitos verificadores e os erros mais comuns de quem implementa a validação."
definicao: "Validar um CPF é recalcular os dois dígitos verificadores a partir dos nove primeiros e compará-los com os informados. Se coincidirem, o número é matematicamente válido — mas isso não prova que ele existe na base da Receita Federal nem que está regular."
date: 2026-09-29
lastmod: 2026-10-08
aliases:
  - /artigos/como-validar-cpf/
faq:
  - q: "Um CPF válido existe na Receita Federal?"
    a: "Não necessariamente. A conta só detecta erros de digitação; um número gerado ao acaso pode ser válido e não ter dono."
  - q: "111.111.111-11 é um CPF válido?"
    a: "Passa na conta do módulo 11, mas sequências repetidas costumam ser rejeitadas pelos sistemas e são tratadas como inválidas."
---
Existe uma distinção fundamental que muita gente não percebe: **validar** e **consultar** um CPF são operações completamente diferentes. Validar é uma conta matemática — rápida, local, sem internet. Consultar é verificar a existência e a situação real do número na Receita Federal. Para conferir agora sem escrever código, use o [validador de CPF online](/validador-de-cpf/).

## Validar não é confirmar existência

A validação só detecta erros de digitação. Um número gerado aleatoriamente pode passar em todos os critérios matemáticos e ainda assim não ter dono na base da Receita. Para saber a situação real de um CPF é preciso fazer a [consulta de CPF](/glossario/consulta-de-cpf/), com número e data de nascimento.

## Como validar: passo a passo

1. **Remova a pontuação.** Deixe só os dígitos: 123.456.789-09 vira 12345678909.
2. **Confira o tamanho.** Precisam ser exatamente 11 dígitos, sem letras.
3. **Rejeite sequências repetidas.** 111.111.111-11 e similares passam na conta, mas os sistemas costumam tratá-los como inválidos.
4. **Recalcule o 10º dígito** a partir dos nove primeiros e compare.
5. **Recalcule o 11º dígito** a partir dos dez primeiros e compare.

O cálculo completo está explicado em [dígito verificador do CPF](/glossario/digito-verificador/).

## Limitações da validação

Um CPF válido matematicamente não significa que ele pertence a uma pessoa específica, que essa pessoa existe ou que o CPF está regular. A conta apenas detecta erros de transcrição — como trocar dois dígitos ou digitar um número a mais.

## Erros frequentes de desenvolvedor

- **Guardar o CPF como número.** Um CPF pode começar com zero, como 012.345.678-90. Trate sempre como texto.
- **Aceitar só o formato com pontos.** Aceite as duas formas e normalize antes de validar.
- **Achar que válido é real.** Um número gerado ao acaso pode ser válido e mesmo assim não ter dono cadastrado.
