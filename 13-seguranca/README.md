# Segurança

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a postura defensiva de base: utilizadores e `sudo`, SSH endurecido, firewalls
(`ufw`/`firewalld`/`nftables`), SELinux/AppArmor, atualizações e backups — com a regra
de nunca criar configuração insegura em exemplos para iniciantes.

## Pré-requisitos

- `05-permissoes`, `08-pacotes`, `12-networking`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/usuarios-sudo-e-ssh.md` | learn | Contas, `sudoers`, chaves SSH, `sshd_config` essencial |
| `learn/firewall-e-mac.md` | learn | `ufw` vs. `firewalld` vs. `nftables`; SELinux/AppArmor |
| `reference/hardening-essencial.md` | reference | Checklist: updates, SSH, firewall, fail2ban, backups 3-2-1 |
| `troubleshooting/fui-comprometido.md` | troubleshooting | Sinais, contenção (isolar rede), evidências, reinstalação limpa |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Eixo transversal: aplica-se a
`25-servidores` e a qualquer máquina exposta.

## Notas técnicas do eixo

- Autenticação por palavra-passe SSH exposta à Internet recebe força bruta em minutos:
  chaves + `PasswordAuthentication no` + porta/fail2ban como camadas, nunca uma só.
- `ufw` (Debian/Ubuntu) e `firewalld` (Fedora/openSUSE) são frontends; a base moderna
  é `nftables` (sucessor do `iptables`) — o learn mostra as três camadas.
- Conta comprometida não se "limpa": contenção + backup de dados + reinstalação a
  partir de fonte confiável; logs servem para âmbito, não para absolvição.
