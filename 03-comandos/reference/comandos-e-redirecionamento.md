---
title: "Referência: comandos e redirecionamento"
category: reference
level: basico
prerequisites:
  - "03-comandos/learn/anatomia-comandos-pipes-e-redirecionamento"
distributions:
  - universal
requires:
  - "anatomia, pipes e redirecionamento"
related:
  - "03-comandos/troubleshooting/comando-falhou-ou-saiu-vazio"
commands:
  - type
  - man
  - cat
  - sort
  - head
  - wc
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), bash 5.3.15"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Referência: comandos e redirecionamento

> Documento de referência: tabelas, sintaxe e localizações — sem progressão
> didática. Exceção justificada ao template learn (missão §3): consolida o que o
> tópico `learn/` ensina; remete para ele em vez de repetir.

## 1. Tabela principal

### Operadores (todos POSIX, qualquer `sh`)

| Operador | Efeito | Risco |
|----------|--------|-------|
| `>` | stdout → ficheiro (**trunca**) | destrói conteúdo |
| `>>` | stdout → ficheiro (acrescenta) | seguro |
| `<` | ficheiro → stdin | seguro |
| `<<EOF` | here-document → stdin | seguro |
| `<<< 'txt'` | here-string → stdin (extensão, bash/zsh) | seguro |
| `2>` | stderr → ficheiro | seguro |
| `> f 2>&1` | stdout+stderr → ficheiro | trunca `f` |
| `\|` | stdout → stdin do próximo | seguro |
| `$?` | estado do último comando/pipe | só o último sem `pipefail` |

### Natureza e ajuda (valores aqui, executados)

| Pergunta | Comando | Resposta aqui |
|----------|---------|---------------|
| Tipo? | `type ls echo cd test printf` | externo; 4 builtins |
| Ajuda rápida | `ls --help` | `Usage: ls [OPTION]...` |
| Manual | `man -w ls printf` | `man1/ls.1.gz`, `man1/printf.1.gz` |
| Info GNU | `info --version` | `texinfo 7.3` |
| Localizador portátil | `command -v` | intrínseco POSIX (ver tópico 2) |

Conceitos: [anatomia-comandos-pipes-e-redirecionamento.md](../learn/anatomia-comandos-pipes-e-redirecionamento.md).

## 2. Sintaxe e opções

```bash
cmd > f 2> e; echo "rc=$?"   # separar canais + estado (padrão de diagnóstico)
cmd >> f                     # acrescentar sem truncar
a | b | c                    # cadeia de filtros
set -o pipefail              # (bash) estado do pipe = 1.ª falha
set -o noclobber             # (interativo) recusar `>` sobre existente
cat <<< 'texto'              # stdin sem ficheiro
```

## 3. Ficheiros e localizações

| Caminho | Conteúdo |
|---------|----------|
| `/usr/share/man/man1/` | Manuais (`ls.1.gz` aqui) |
| `/usr/bin/` | Externos (3577 entradas aqui) |

## 4. Diferenças entre distribuições

| Família | Notas | Evidência |
|---------|-------|-----------|
| Arch (base deste teste) | GNU coreutils, `man-db`, `texinfo` | **executada aqui** |
| Debian/Ubuntu | `info` nem sempre instalado | documentada, não executada aqui |
| Alpine/BusyBox | flags reduzidas; sem `info`; `man` opcional | documentada, não executada aqui |

### Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, x86_64), bash 5.3.15, 2026-10-15. Herdada do
tópico `learn/` (mesma sessão de testes em `/tmp/opencode/cmd`); operadores da
tabela todos exercitados nos Exemplos 2–4.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| Operadores `> >> 2> \| <<< $?` | tabela acima | conforme Exemplos 2–4 | executado |
| `type` + ajudas | naturezas + man/info | externo/builtins; texinfo 7.3 | executado |
| Flags BusyBox reduzidas | — | — | **não executado** |

Limitações: `noclobber` citado como opção interativa, não demonstrado; BusyBox não testado.

## 5. Ver também (sem duplicar)

- [anatomia-comandos-pipes-e-redirecionamento.md](../learn/anatomia-comandos-pipes-e-redirecionamento.md) — conceitos
- [comando-falhou-ou-saiu-vazio.md](../troubleshooting/comando-falhou-ou-saiu-vazio.md) — diagnóstico

## 6. Referências oficiais

- POSIX.1-2024, Shell Command Language — https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html
