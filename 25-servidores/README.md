# Servidores

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a expor serviços com responsabilidade: SSH server, nginx (vhosts, TLS),
logs e rotação, backups e restauro testado, firewall por serviço — sempre com
hardening antes de abrir portas.

## Pré-requisitos

- `12-networking`, `13-seguranca`, `09-systemd` e `05-permissoes`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/ssh-server-e-nginx.md` | learn | `sshd` endurecido, vhosts nginx, TLS (Let's Encrypt intro) |
| `reference/logs-backups-firewall.md` | reference | `journalctl`, `logrotate`, `rsync`/`borg` intro, regras por serviço |
| `troubleshooting/servico-inacessivel.md` | troubleshooting | Porta fechada? a escutar onde? firewall? DNS? TLS expirado? |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Primeiro local, depois LAN,
depois Internet — cada salto com a checklist de `13-seguranca` refeita.

## Notas técnicas do eixo

- `ss -tlnp` mostra o que escuta e onde (`127.0.0.1` ≠ `0.0.0.0`); firewall e
  escuta são controlos independentes — verificar os dois.
- Backup não testado não existe: `restore --dry-run`/extração de amostra antes de
  declarar cobertura (regra 3-2-1).
- Certificados expiram: monitorizar/renovar (ACME) em vez de descobrir na outage.
