# Kernel

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar o núcleo para além do "versão X": o que o kernel faz (agendamento, memória,
syscalls), módulos (`lsmod`, `modprobe`, DKMS), parâmetros (`sysctl`), escolha de
kernel (stable, LTS, zen, hardened) e leitura de `dmesg` — sem recompilar nada.

## Pré-requisitos

- `01-fundamentos` (o que é o kernel), `06-processos`, `15-drivers`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/o-que-o-kernel-faz.md` | learn | Syscalls, agendamento, memória virtual, userspace vs. kernelspace |
| `learn/modulos-e-sysctl.md` | learn | `lsmod`/`modprobe`, DKMS, `sysctl -w` reversível |
| `reference/dmesg-uname-sysctl.md` | reference | Tabelas: `uname`, `dmesg`, `sysctl`, `/proc/sys` |
| `troubleshooting/kernel-panic-ou-modulo-falha.md` | troubleshooting | Panic, módulo que não carrega, regressão após atualização (boot com LTS) |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Ligações: `14` alimenta
`15-drivers`, `18-performance` e `10-boot` (parâmetros).

## Notas técnicas do eixo

- Kernel Linux é GPL-2.0-only com exceção de syscall (ver `01-fundamentos`) —
  módulos proprietários (ex.: NVIDIA) vivem fora da árvore, via DKMS.
- `sysctl -w` é reversível (volta no reboot salvo em ficheiro); parâmetros de boot
  testam-se uma vez no GRUB antes de gravar.
- Regressão de kernel resolve-se arrancando o kernel anterior/LTS instalado em
  paralelo — nunca ter só um kernel em produção.
