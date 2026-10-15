# Automação

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar tarefas agendadas e repetíveis: cron vs. systemd timers, scripts idempotentes,
Ansible essencial — com logging e notificação de falha desde o dia um (tarefa
silenciosa que falha é pior que nenhuma).

## Pré-requisitos

- `07-shell`, `09-systemd` (timers) e `21-git` (versionar automação).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/cron-timers-e-ansible.md` | learn | Sintaxe cron, timers com `OnCalendar`, playbook mínimo |
| `reference/agendar-e-idempotencia.md` | reference | Tabelas cron, `systemctl --user` vs. sistema, módulos Ansible comuns |
| `troubleshooting/tarefa-nao-correm.md` | troubleshooting | Cron sem `PATH`/env, timer inativo, permissão, e-mail/saída perdida |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Toda automação versionada em
git, testada à mão uma vez antes de agendar, com saída para log.

## Notas técnicas do eixo

- Cron corre com ambiente mínimo (`PATH` curto, sem dotfiles): caminhos absolutos e
  variáveis explícitas, ou falha "misteriosa" que funciona à mão.
- systemd timers têm journal, dependências e `AccuracySec`/`RandomizedDelaySec` —
  preferi-los em sistemas com systemd; cron onde não há.
- Automatizar sem idempotência multiplica o estrago: reaplicar deve ser seguro.
