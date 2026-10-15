# Drivers

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar como o hardware ganha suporte: drivers na árvore vs. externos, firmware
(`linux-firmware`), DKMS, NVIDIA/ Broadcom/ impressoras (casos clássicos) e como
identificar hardware (`lspci`, `lsusb`, `lshw`) antes de instalar qualquer coisa.

## Pré-requisitos

- `14-kernel` (módulos) e `08-pacotes`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/hardware-e-drivers.md` | learn | Identificar hardware, driver na árvore vs. DKMS vs. blob |
| `reference/lspci-lsusb-lshw.md` | reference | Tabelas de identificação e de pacotes por família |
| `troubleshooting/hardware-nao-reconhecido.md` | troubleshooting | `dmesg | grep -i firmware`, kernel antigo, Secure Boot vs. DKMS |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Primeiro identificar
(`lspci -k` mostra o driver em uso), depois agir — nunca instalar drivers às cegas.

## Notas técnicas do eixo

- `lspci -k` / `lsusb` + `dmesg` dizem se falta driver, firmware ou ambos.
- Módulos DKMS partem com Secure Boot ativo sem chave MOK registada — o
  troubleshooting cobre o diagnóstico (não o bypass inseguro).
- Firmware proprietário é redistribuível mas não livre (ver `01-fundamentos`,
  licenças): distros 100% livres recusam-no e algum hardware fica sem suporte.
