# Shell

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar o `bash` como linguagem: expansões (`~`, `$var`, `$(...)`, `*`), quoting,
variáveis e ambiente, funções, fluxo (`if`, `for`, `while`, `case`), dotfiles e
histórico — e a fronteira entre o portátil (POSIX `sh`) e as extensões bash.

## Pré-requisitos

- `02-terminal`, `03-comandos` (concluídos) e `01-fundamentos` (POSIX).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/bash-e-posix-sh.md` | learn | O que é POSIX-estrito vs. bashismo; shebang correto |
| `learn/scripting-essencial.md` | learn | Primeiro script seguro: quoting, testes, erros, `set -euo pipefail` |
| `reference/expansoes-e-quoting.md` | reference | Tabelas de expansões, quoting, parâmetros especiais (`$?`, `$#`, `$@`) |
| `troubleshooting/script-falha-noutro-sh.md` | troubleshooting | Funciona em `bash`, parte em `dash`: caçar bashismos |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Ponte com `27-automacao`
(cron, timers) e `26-devops` (scripts em CI). Usar `shellcheck` em todos os exemplos.

## Notas técnicas do eixo

- `set -euo pipefail` é extensão bash (não POSIX): ótimo para scripts `bash`
  explícitos (`#!/usr/bin/env bash`), proibido em scripts `#!/bin/sh` portáteis.
- Variáveis sempre entre aspas (`"$var"`); `for f in $(ls)` é quase sempre errado
  (usar glob `for f in *`).
- Dotfiles (`.bashrc` vs. `.bash_profile` vs. `.profile`) diferem entre login e
  não-login, interativo e não-interativo — o tópico learn mapeia cada caso.
