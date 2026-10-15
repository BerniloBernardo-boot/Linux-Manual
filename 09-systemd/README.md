# Systemd

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar o init/serviços dominante: units (`service`, `timer`, `socket`, `target`),
`systemctl`, logs (`journalctl`), timers como alternativa ao cron — e as alternativas
para sistemas sem systemd (OpenRC no Alpine, runit no Void).

## Pré-requisitos

- `06-processos` e `10-boot` (ciclo de vida e arranque).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/systemctl-e-units.md` | learn | Units, estados, `enable` vs. `start`, dependências |
| `learn/journalctl-e-timers.md` | learn | `journalctl`, persistência, timers vs. cron |
| `reference/units-e-targets.md` | reference | Tabelas: tipos de unit, diretivas comuns, targets vs. runlevels |
| `troubleshooting/servico-nao-inicia.md` | troubleshooting | `failed`: `status`, journal, portas, permissões |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Alternativas sem systemd têm
secção própria em cada documento (nunca `systemctl` assumido universal).

## Notas técnicas do eixo

- `enable` (arrancar no boot) ≠ `start` (arrancar agora) — a confusão mais comum.
- `journalctl` volátil por omissão em algumas distros; persistência exige
  `/var/log/journal/` (detalhe no learn).
- Alpine usa OpenRC (`rc-service`, `rc-update`); Void usa runit (`sv`) — comandos
  documentados na tabela cross-distro de cada tópico, não testados neste ambiente.
