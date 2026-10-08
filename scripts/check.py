#!/usr/bin/env python3
"""Verificações de conteúdo (rode antes do commit): python3 scripts/check.py
- glossário e páginas de estatística: definição <= 50 palavras
- 2 a 3 links internos contextuais no corpo (fora de blocos de código); hubs (_index), a homepage (sem limite) e o validador são isentos
- <title> e H1 <= 55 caracteres; meta description <= 155
- nenhum link restante para /artigos/ fora de 'aliases'
"""
import re, glob, sys, os
ok = True
SITE = "Gerador de CPF"; SITE_DESC = "Gerador de CPF online: gere um CPF válido e aleatório, com ou sem pontuação e por estado."
def val(fm, k):
    x = re.search(rf'^{k}: "(.*)"$', fm, re.M)
    return x.group(1).replace('\\"', '"') if x else None
# limites: <title> renderizado e H1 <= 55 caracteres; meta description <= 155
for f in sorted(glob.glob('content/**/*.md', recursive=True)):
    fm = re.match(r'---\n(.*?)\n---', open(f, encoding='utf-8').read(), re.S).group(1)
    seo, per, tit, dsc = val(fm, 'seoTitle'), val(fm, 'pergunta'), val(fm, 'title'), val(fm, 'description')
    rendered = seo or (SITE if f == 'content/_index.md' else (per or tit))
    h1 = per or tit
    if len(rendered) > 55: print(f'title {len(rendered)} > 55: {f}'); ok = False
    if len(h1) > 55: print(f'h1 {len(h1)} > 55: {f}'); ok = False
    if len(dsc or SITE_DESC) > 155: print(f'description {len(dsc)} > 155: {f}'); ok = False
files = sorted(glob.glob('content/glossario/*.md') + glob.glob('content/estatisticas/*.md') + ['content/_index.md', 'content/validador-de-cpf.md'])
for f in files:
    t = open(f, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', t, re.S)
    fm, body = m.group(1), m.group(2)
    d = re.search(r'^definicao: "(.*)"$', fm, re.M)
    needs_def = ('glossario' in f or 'estatisticas' in f)
    if needs_def:
        if not d: print('SEM definicao:', f); ok = False
        else:
            n = len(d.group(1).split())
            if n > 50: print(f'definicao {n} palavras: {f}'); ok = False
    if f.endswith('_index.md') and f != 'content/_index.md':
        continue
    if f == 'content/_index.md':  # homepage: sem limite de links; deve linkar para todo o glossário e estatísticas
        have = set(re.findall(r'\]\((/[^)\s]*)\)', body))
        need = {'/glossario/' + os.path.basename(g)[:-3] + '/' for g in glob.glob('content/glossario/*.md') if not g.endswith('_index.md')}
        need |= {'/estatisticas/' + os.path.basename(g)[:-3] + '/' for g in glob.glob('content/estatisticas/*.md') if not g.endswith('_index.md')}
        need |= {'/glossario/', '/estatisticas/'}
        for m in sorted(need - have): print('homepage sem link para', m); ok = False
        continue
    if f.endswith('validador-de-cpf.md'):  # página de ferramenta: só checa /artigos/
        if '/artigos/' in body: print('link /artigos/ no corpo:', f); ok = False
        continue
    body_nocode = re.sub(r'```.*?```', '', body, flags=re.S)
    links = re.findall(r'\]\((/[^)\s]*)\)', body_nocode)
    n = len(links)
    if not 2 <= n <= 3:
        print(f'{n} links internos (esperado 2-3): {f} -> {links}'); ok = False
    if '/artigos/' in body: print('link /artigos/ no corpo:', f); ok = False
print('OK' if ok else 'FALHOU'); sys.exit(0 if ok else 1)
