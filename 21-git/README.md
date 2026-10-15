# Git

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar Git onde ele vive (Linux): configuração, ciclo add/commit/push/pull, branches
e merge, resolução de conflitos, e fluxos profissionais (PRs, revisão) — com ponte
para o repositório Git existente do utilizador quando aplicável.

## Pré-requisitos

- `03-comandos`, `07-shell` e `01-fundamentos` (SSH/chaves para remotos).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/git-essencial.md` | learn | Config, ciclo base, branches, merge, remoto |
| `reference/comandos-git.md` | reference | Tabelas por tarefa: dia a dia, desfazer, inspecionar, colaborar |
| `troubleshooting/conflitos-e-estados.md` | troubleshooting | Conflitos, detached HEAD, `push` rejeitado, recuperar commits (`reflog`) |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Praticar em repositório
descartável antes do real; `push --force` em branch partilhado é proibido nos exemplos.

## Notas técnicas do eixo

- `user.name`/`user.email` + SSH (`ed25519`) ou token antes do primeiro `push`.
- `git pull --rebase` vs. merge: equipas definem um; misturar sem critério suja o histórico.
- Nada se perde facilmente: `reflog` recupera commits "perdidos"; `stash` guarda
  trabalho a meio antes de trocar de branch.
