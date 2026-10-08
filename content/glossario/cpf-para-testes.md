---
title: "CPF para testes de software"
pergunta: "Como usar CPF gerado em testes de software?"
description: "Boas práticas para usar CPFs gerados em testes automatizados: por que evitar CPFs reais, casos de teste essenciais e os erros de implementação mais comuns."
definicao: "CPF para testes é um número gerado aleatoriamente que passa na validação dos dígitos verificadores, mas é fictício. Em testes de software ele substitui CPFs reais, evitando expor dados pessoais — e nunca deve ser usado em cadastros reais."
date: 2026-09-29
lastmod: 2026-10-08
aliases:
  - /artigos/gerar-cpf-para-testes-de-software/
faq:
  - q: "Por que não usar CPFs reais em testes?"
    a: "CPF é dado pessoal. Usá-lo em ambientes de teste cria risco de privacidade e pode misturar dados reais com dados de teste."
  - q: "Um CPF gerado pode coincidir com o de uma pessoa real?"
    a: "Sim, porque a geração é aleatória. Por isso ele serve para testes, nunca para cadastros de verdade."
---
Em testes automatizados, o CPF é um dos campos mais comuns de preencher corretamente: o formulário rejeita entradas inválidas, mas exige que a entrada seja matematicamente coerente. Usar o CPF de uma pessoa real resolve o problema imediato, mas cria outro maior.

## O risco de usar CPFs reais

CPF é dado pessoal. Usar o de uma pessoa real — o seu, o de um colega ou um copiado da internet — em ambientes de teste expõe informações privadas e pode misturar dados reais com dados fictícios em bases que não deveriam se misturar. A alternativa correta é gerar números válidos matematicamente, mas sem correspondência real.

## Lista de casos de teste

Alguns cenários que valem a pena cobrir antes de encerrar a suíte de testes:

- CPF válido com pontuação: `123.456.789-09`
- CPF válido sem pontuação: `12345678909`
- CPF com dígito verificador errado (troque o último dígito): `12345678900`
- Sequência repetida, como `111.111.111-11`
- Menos de 11 dígitos, mais de 11 dígitos, letras no lugar de números
- Campo vazio
- CPF que começa com zero, como `012.345.678-90`: confirme que o zero não some
- CPFs de regiões fiscais diferentes, se o sistema trata o nono dígito. O [gerador de CPF](/) permite escolher o estado

## Erros de implementação frequentes

- **Guardar o CPF como número inteiro.** Isso remove os zeros à esquerda. Trate sempre como texto.
- **Validar só o formato** (a máscara) e esquecer de recalcular os dígitos verificadores.
- **Reprovar CPF sem pontuação.** Normalize a entrada antes de validar; ambas as formas devem ser aceitas.

## Integrar ao código de testes

Você pode gerar CPFs diretamente no código, sem depender de fixtures manuais. Veja funções prontas para JavaScript, Python e PHP no [algoritmo do CPF](/glossario/algoritmo-do-cpf/), e entenda a regra matemática em [validação de CPF](/glossario/validacao-de-cpf/).
