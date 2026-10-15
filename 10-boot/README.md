# Boot

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a sequência firmware → bootloader → kernel → initramfs → init: UEFI vs. BIOS,
GRUB vs. systemd-boot, parâmetros de kernel, e como recuperar um sistema que não
arranca (live USB, `chroot`, reinstalação do bootloader).

## Pré-requisitos

- `04-filesystem` (`/boot`), `09-systemd` e `11-storage` (partições).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/arranque-do-firmware-ao-login.md` | learn | UEFI/BIOS, ESP, bootloader, initramfs, targets |
| `reference/parametros-e-bootloader.md` | reference | Parâmetros de kernel, entradas GRUB/systemd-boot, `efibootmgr` |
| `troubleshooting/sistema-nao-arranca.md` | troubleshooting | GRUB rescue, kernel panic, `fstab` mau, `/boot` cheio |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. O troubleshooting é de leitura
obrigatória antes de tocar em bootloader em produção.

## Notas técnicas do eixo

- A ESP (`/boot/efi`) é vfat e partilhada com o firmware — operações destrutivas aqui
  afetam todos os sistemas instalados (dual-boot incluído).
- `/boot` pequena e cheia impede instalar kernels novos e, no limite, arrancar após
  atualização — gerir kernels pelo gestor, nunca com `rm`.
- `efibootmgr -v` (somente leitura) mostra a ordem de boot UEFI; alterar a ordem é
  reversível, apagar entradas exige saber recriar.
