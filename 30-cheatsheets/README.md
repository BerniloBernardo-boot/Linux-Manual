# Cheatsheets

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Referência rápida para quem já aprendeu: uma página por tema, comandos prontos com
o risco sinalizado — sem ensinar do zero (para isso, os eixos) e sem comandos
destrutivos sem alerta.

## Pré-requisitos

- Os eixos correspondentes (cheatsheet pressupõe conceito aprendido).

## Documentos planeados

| Documento | Escopo |
|-----------|--------|
| `inspecao-do-sistema.md` | `uname`, `os-release`, `getconf`, `lsblk`, `df`, `ss` |
| `permissoes.md` | `chmod`/`chown`/`umask`/ACL em 1 página |
| `rede.md` | `ip`, `ss`, `resolvectl`, `nmcli`, diagnóstico em 5 linhas |
| `systemd.md` | `systemctl`, `journalctl`, timers em 1 página |
| `pacotes.md` | Tabela apt/pacman/dnf/zypper/apk/xbps/nix |

Cada cheatsheet exige `risk:` correto e `> ⚠️` em comandos com escrita/destruição;
`category: cheatsheet` + evidência quando testado.

## Como usar

Consulta, não estudo. Se um comando precisa de explicação, o link para o tópico
`learn/` correspondente vem junto — cheatsheet não duplica didática.

## Notas técnicas do eixo

- Uma página por tema, densa mas legível; nada de "guia completo" disfarçado.
- Comandos por família lado a lado (matriz), nunca só a distro do autor.
