# Filesystem

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar como o espaço em disco é organizado e acedido: tipos de sistemas de ficheiros
(ext4, Btrfs, XFS, vfat), inodes, links duros e simbólicos, montagem (`mount`,
`/etc/fstab`), e como diagnosticar disco cheio ou montagens falhadas — sem destruir dados.

## Pré-requisitos

- `01-fundamentos` (hierarquia e FHS essencial — concluído).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/montagem-e-tipos-de-fs.md` | learn | Montar/desmontar, `fstab`, ext4 vs. Btrfs vs. XFS vs. vfat |
| `learn/inodes-links-duros-e-simbolicos.md` | learn | Inodes, `ln` vs. `ln -s`, quando cada um parte |
| `reference/hierarquia-e-montagens.md` | reference | Tabelas: `lsblk`, `df`, `du`, `findmnt`, opções de montagem |
| `troubleshooting/disco-cheio-ou-montagem-falhou.md` | troubleshooting | `No space left`, UUID errado, `fstab` com erro |

## Como usar

Ordem: `learn/` (conceitos) → `reference/` (comandos) → `troubleshooting/` (sintomas).
Eixo seguinte natural: `05-permissoes` (quem pode escrever onde) e `11-storage`
(partições e volumes, o nível abaixo da montagem).

## Notas técnicas do eixo

- ext4 é a omissão na maioria das distros; Btrfs é omissão no openSUSE e opção no
  Fedora/Arch (subvolumes `@`/`@log` observados neste projeto); XFS é tradicional em
  RHEL; `/boot` EFI é vfat e pequena — nunca apagar lá à mão.
- `/etc/fstab` com erro pode impedir o arranque: editar com backup e validar com
  `findmnt --verify` (detalhe no tópico learn).
- Comandos deste eixo nunca apagam por si; `mkfs`/`parted` pertencem a `11-storage`
  e são destrutivos — aqui só se inspeciona e monta.
