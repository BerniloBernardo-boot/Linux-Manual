# Storage

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar o nível abaixo do filesystem: tabelas de partição (GPT/MBR), filesystems e
`mkfs`, LVM, encriptação (LUKS), swap, e noções de RAID/Btrfs — com ênfase total em
não destruir dados (backup, identificação correta do disco, reversão).

## Pré-requisitos

- `04-filesystem` (montagem) e `10-boot` (`/boot`, ESP).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/particoes-e-volumes.md` | learn | GPT vs. MBR, `mkfs`, LVM, LUKS, swap (conceitos + demonstração segura) |
| `reference/lsblk-df-du.md` | reference | Tabelas: `lsblk`, `blkid`, `df`, `du`, `mount`, `swapon` |
| `troubleshooting/disco-cheio.md` | troubleshooting | Encontrar consumo (`du -x`), logs, subvolumes, inodes esgotados |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Regra do eixo: demonstrações
destrutivas só em VM/disco descartável ou ficheiros-imagem (`fallocate` + loop),
nunca no sistema real — a política de verificação proíbe evidência destrutiva.

## Notas técnicas do eixo

- `mkfs`, `parted`, `gdisk`, `cryptsetup` e `dd` **destroem dados** sem confirmação
  útil: `risk: destrutivo` + bloco de alerta + pré-condições em cada tópico.
- Confirmar o disco com `lsblk` antes de qualquer escrita; `/dev/sda` vs. `/dev/sdb`
  trocado é perda total.
- LUKS sem backup do cabeçalho (`cryptsetup luksHeaderBackup`) = sem recuperação
  possível se corromper — o learn inclui o procedimento.
