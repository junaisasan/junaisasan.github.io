---
title: "Algoritmo do CPF (código)"
pergunta: "Como gerar e validar CPF em código?"
description: "Funções prontas e comentadas para calcular o dígito verificador, validar e gerar CPF em JavaScript, Python e PHP — com explicação de cada escolha de implementação."
definicao: "O algoritmo do CPF calcula cada dígito verificador por soma ponderada e resto da divisão por 11. Com ele é possível validar e gerar CPFs em qualquer linguagem; abaixo há implementações prontas em JavaScript, Python e PHP."
date: 2026-09-29
lastmod: 2026-10-08
aliases:
  - /artigos/codigo-para-gerar-e-validar-cpf/
faq:
  - q: "Por que tratar o CPF como texto no código?"
    a: "Para preservar zeros à esquerda, como em 012.345.678-90."
  - q: "O CPF gerado por código serve para cadastros reais?"
    a: "Não. Os CPFs gerados são apenas para testes e podem coincidir com o de uma pessoa real."
---
JavaScript é a escolha natural para validação no navegador; Python domina ciência de dados e automação; PHP ainda move muitos sistemas legados de cadastro. As três implementações abaixo seguem o mesmo método — soma ponderada e resto da divisão por 11 (módulo 11) — explicado em detalhes em [dígito verificador do CPF](/glossario/digito-verificador/). Cada uma oferece três funções: calcular um dígito, validar e gerar.

Os CPFs gerados são apenas para testes. Leia antes [CPF para testes de software](/glossario/cpf-para-testes/).

## JavaScript

```js
// Calcula um dígito verificador a partir de um array de dígitos (9 ou 10 itens)
function calcDigito(digitos) {
  const peso = digitos.length + 1;
  let soma = 0;
  for (let i = 0; i < digitos.length; i++) soma += digitos[i] * (peso - i);
  const resto = soma % 11;
  return resto < 2 ? 0 : 11 - resto;
}

function validarCPF(cpf) {
  const d = String(cpf).replace(/\D/g, '');
  if (d.length !== 11 || /^(\d)\1{10}$/.test(d)) return false;
  const n = d.split('').map(Number);
  return calcDigito(n.slice(0, 9)) === n[9] && calcDigito(n.slice(0, 10)) === n[10];
}

function gerarCPF(comPontuacao = true) {
  let base;
  do {
    base = Array.from({ length: 9 }, () => Math.floor(Math.random() * 10));
  } while (base.every((n) => n === base[0]));
  base.push(calcDigito(base));
  base.push(calcDigito(base));
  const cpf = base.join('');
  return comPontuacao
    ? cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
    : cpf;
}
```

Uso:

```js
validarCPF('123.456.789-09'); // true
gerarCPF();                   // "529.982.247-25" (exemplo; muda a cada chamada)
gerarCPF(false);              // só dígitos
```

`Math.random()` basta para dados de teste. Não use estes números para nada que exija aleatoriedade segura.

## Python

```python
import random
import re


def calc_digito(base: str) -> int:
    """Calcula um dígito verificador a partir de 9 ou 10 dígitos."""
    peso = len(base) + 1
    soma = sum(int(d) * (peso - i) for i, d in enumerate(base))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto


def validar_cpf(cpf: str) -> bool:
    d = re.sub(r"\D", "", str(cpf))
    if len(d) != 11 or d == d[0] * 11:
        return False
    return calc_digito(d[:9]) == int(d[9]) and calc_digito(d[:10]) == int(d[10])


def gerar_cpf(com_pontuacao: bool = True) -> str:
    while True:
        base = "".join(str(random.randint(0, 9)) for _ in range(9))
        if base != base[0] * 9:
            break
    base += str(calc_digito(base))
    base += str(calc_digito(base))
    if com_pontuacao:
        return f"{base[:3]}.{base[3:6]}.{base[6:9]}-{base[9:]}"
    return base
```

Uso:

```python
validar_cpf("123.456.789-09")  # True
gerar_cpf()                    # ex.: "529.982.247-25"
gerar_cpf(False)               # só dígitos
```

## PHP

```php
<?php
// Calcula um dígito verificador a partir de 9 ou 10 dígitos
function calcDigito(string $base): int {
    $peso = strlen($base) + 1;
    $soma = 0;
    for ($i = 0; $i < strlen($base); $i++) {
        $soma += (int) $base[$i] * ($peso - $i);
    }
    $resto = $soma % 11;
    return $resto < 2 ? 0 : 11 - $resto;
}

function validarCpf(string $cpf): bool {
    $d = preg_replace('/\D/', '', $cpf);
    if (strlen($d) !== 11 || preg_match('/^(\d)\1{10}$/', $d)) {
        return false;
    }
    return calcDigito(substr($d, 0, 9)) === (int) $d[9]
        && calcDigito(substr($d, 0, 10)) === (int) $d[10];
}

function gerarCpf(bool $comPontuacao = true): string {
    do {
        $base = '';
        for ($i = 0; $i < 9; $i++) {
            $base .= random_int(0, 9);
        }
    } while (preg_match('/^(\d)\1{8}$/', $base));
    $base .= calcDigito($base);
    $base .= calcDigito($base);
    return $comPontuacao
        ? vsprintf('%s%s%s.%s%s%s.%s%s%s-%s%s', str_split($base))
        : $base;
}
```

Uso:

```php
validarCpf('123.456.789-09'); // true
gerarCpf();                   // ex.: "529.982.247-25"
gerarCpf(false);              // só dígitos
```

## Armadilhas a evitar

- O CPF é tratado como **texto**, para preservar zeros à esquerda.
- Sequências de dígitos repetidos (111.111.111-11 etc.) são rejeitadas na validação e evitadas na geração, pois os sistemas costumam tratá-las como inválidas.
- A validação confere apenas a matemática. Ela não prova que o CPF existe nem que está regular. Para isso, consulte a Receita Federal.
- Para gerar por estado, defina o nono dígito conforme a [região fiscal](/glossario/regiao-fiscal/) antes de calcular os dois últimos.
