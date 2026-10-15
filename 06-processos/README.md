# Processos

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar o ciclo de vida dos programas em execução: PID, estados, sinais, jobs do shell,
prioridades (`nice`), e a visão geral de serviços (systemd units) e cgroups — e como
investigar consumo anormal de CPU/memória e terminar processos com segurança.

## Pré-requisitos

- `02-terminal`, `03-comandos` (concluídos).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/processos-sinais-e-jobs.md` | learn | PID/PPID, estados, sinais, `&`, `jobs`, `fg`, `bg`, `nice` |
| `reference/ps-kill-e-sinais.md` | reference | Tabelas: `ps`, `top`/`htop`, sinais e `kill`, prioridades |
| `troubleshooting/processo-consome-recursos.md` | troubleshooting | CPU/memória alta: medir, identificar, agir sem `kill -9` precipitado |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Continua em `09-systemd`
(serviços persistentes), `14-kernel` (agendador, OOM) e `18-performance` (profiling).

## Notas técnicas do eixo

- `SIGTERM` (15, omissão) pede terminação limpa; `SIGKILL` (9) não pode ser
  intercetado nem ignorado — usar só quando o processo não responde ao TERM, pois
  impede cleanup (ficheiros temporários, locks).
- `kill -9` em PID errado mata o processo errado: confirmar com `ps -o pid,comm`
  antes. `killall`/`pkill` por nome exigem redobrada atenção.
- Zumbis (`Z`) não consomem recursos — o problema é o pai que não recolhe o estado.
