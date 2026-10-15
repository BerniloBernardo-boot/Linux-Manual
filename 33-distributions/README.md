# Distributions

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ser a fonte única das diferenças entre famílias: Debian/Ubuntu (`apt`), Arch
(`pacman`), Fedora/RHEL (`dnf`, SELinux), openSUSE (`zypper`, YaST), Alpine (`apk`,
OpenRC, musl), Void (`xbps`, runit), NixOS (`nix`, declarativo) — para que nenhum
tópico assuma comando universal.

## Pré-requisitos

- `01-fundamentos` (matriz de distribuições) e `08-pacotes`.

## Documentos planeados

| Documento | Escopo |
|-----------|--------|
| `debian-ubuntu.md` | `apt`, `sudo`, netplan, `non-free-firmware` |
| `arch.md` | `pacman`, AUR, rolling, `mkinitcpio` |
| `fedora-rhel.md` | `dnf`, SELinux enforcing, RPM Fusion |
| `opensuse.md` | `zypper`, YaST, Tumbleweed vs. Leap |
| `alpine-void.md` | `apk`+OpenRC+musl; `xbps`+runit |
| `nixos.md` | `configuration.nix`, `allowUnfree`, `/nix/store` |

Cada ficha: gestor, init, firewall, rede, boot, particularidades + o que **não**
assumir. Compatibilidade só com evidência (política `VERIFICACAO.md` §1.3).

## Como usar

Tópicos ligam para aqui nas tabelas cross-distro; este eixo detalha o que a tabela
resume. Divergência nova encontrada ao escrever → atualiza-se a ficha e o tópico.

## Notas técnicas do eixo

- Rolling (Arch, Tumbleweed) vs. stable (Debian, RHEL, Leap): política de atualização
  muda procedimentos de upgrade e rollback.
- Sem systemd (Alpine, Void): `systemctl` não existe — alternativas documentadas,
  nunca "instale o systemd".
