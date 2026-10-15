# Pacotes

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a instalar, atualizar e remover software com o gestor de cada família
(`apt`, `pacman`, `dnf`, `zypper`, `apk`, `xbps`, `nix`), e a perceber repositórios,
chaves, dependências e reversão — sem partir o sistema a meio de uma atualização.

## Pré-requisitos

- `01-fundamentos` (licenças, kernel vs. distro) e `03-comandos`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/gerenciadores-de-pacotes.md` | learn | Conceito universal + tabela `apt/pacman/dnf/zypper/apk/xbps/nix` |
| `reference/instalar-remover-atualizar.md` | reference | Comandos por família: instalar, remover, pesquisar, atualizar, limpar cache |
| `troubleshooting/pacote-quebrado-ou-conflito.md` | troubleshooting | Chaves, dependências, interrupção a meio, rollback |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Ligações: `01-fundamentos`
(licenças), `13-seguranca` (procedência e assinaturas) e `33-distributions` (matriz).

## Notas técnicas do eixo

- Arch é rolling: atualização parcial (`pacman -Sy pacote` sem `-u`) quebra
  dependências — atualizar sempre o sistema completo (`pacman -Syu`).
- Debian/Ubuntu: `apt update` (índices) ≠ `apt upgrade` (pacotes); `PPA` é de
  terceiros — registar a origem.
- NixOS é declarativo (`configuration.nix` + `nixos-rebuild`): "instalar" é
  descrever o estado desejado, modelo diferente documentado à parte.
- Nunca interromper o gestor a meio (`Ctrl+C` no `dpkg`/`pacman` deixa o banco
  inconsistente — o troubleshooting cobre a recuperação).
