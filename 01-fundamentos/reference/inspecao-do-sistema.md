---
title: "Referência: inspeção do sistema"
category: reference
level: basico
prerequisites:
  - "01-fundamentos/learn/o-que-e-linux-kernel-vs-distribuicao"
distributions:
  - universal
requires:
  - "kernel vs. distribuição"
related:
  - "01-fundamentos/troubleshooting/nao-consigo-identificar-o-sistema"
commands:
  - uname
  - hostnamectl
  - cat
  - getconf
  - command
  - ls
  - stat
  - readlink
  - df
  - findmnt
  - pacman
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64)"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Referência: inspeção do sistema

> Documento de referência: tabelas, sintaxe e localizações — sem progressão
> didática. Exceção justificada ao template learn (missão §3): consolida o que os
> tópicos `learn/` ensinam; remete para eles em vez de repetir.

## 1. Tabela principal

| Pergunta | Comando (somente leitura) | Resposta neste ambiente (executado) |
|----------|---------------------------|-------------------------------------|
| Qual kernel? | `uname -srmo` | `Linux 7.2.5-3-omarchy x86_64 GNU/Linux` |
| Kernel completo? | `uname -a` | `Linux bilijin 7.2.5-3-omarchy #1 SMP PREEMPT_DYNAMIC Mon, 14 Sep 2026 19:55:01 +0000 x86_64 GNU/Linux` |
| Qual distro? | `cat /etc/os-release` | `ID=omarchy`, `ID_LIKE=arch` |
| Edição POSIX? | `getconf _POSIX_VERSION` | `200809` (= POSIX.1-2008/SUSv4) |
| Variantes POSIX/X/Open? | `getconf -a \| grep -E 'VERSION'` | `_POSIX_VERSION=200809`, `_XOPEN_VERSION=700`, `POSIX2_VERSION=200809` |
| Qual `sh` real? | `ls -l /bin/sh` | `/bin/sh -> bash` |
| Onde está um comando? | `command -v <nome>` | ex.: `ls` → `/usr/bin/ls`; `printf` → builtin |
| Licença de um pacote? | `pacman -Qi <pacote> \| grep -i Licenses` | ex.: `bash` → `GPL-3.0-or-later` |
| O que está montado? | `findmnt` / `df -h` | `/` btrfs `@`; `/boot` vfat 2G; `/var/log` subvolume `@log` |

Conceitos: [o-que-e-linux-kernel-vs-distribuicao.md](../learn/o-que-e-linux-kernel-vs-distribuicao.md),
[filosofia-unix-e-posix.md](../learn/filosofia-unix-e-posix.md),
[hierarquia-e-fhs-essencial.md](../learn/hierarquia-e-fhs-essencial.md),
[licencas-e-software-livre-essencial.md](../learn/licencas-e-software-livre-essencial.md).

## 2. Sintaxe e opções

```bash
uname -srmo                 # nome, versão, máquina, sistema operativo
cat /etc/os-release         # ID, ID_LIKE, VERSION_ID da distro
getconf _POSIX_VERSION      # edição POSIX efetiva (sem sufixo L)
getconf -a | grep VERSION   # todas as versões declaradas
command -v <nome>           # localizador portátil (intrínseco POSIX)
stat -c '%n -> %F' <caminho>  # tipo de objeto
readlink <symlink>          # alvo do link
df -h <ponto>               # ocupação da montagem
findmnt [<ponto>]           # detalhe da montagem
```

## 3. Ficheiros e localizações

| Caminho | Conteúdo | Notas |
|---------|----------|-------|
| `/etc/os-release` | Identidade da distro | Campos `ID`, `ID_LIKE`, `VERSION_ID` |
| `/usr/share/licenses/<pacote>/` | Texto de licença (Arch) | 593 pastas aqui; canónicos em `spdx/` (101) |
| `/usr/share/doc/<pacote>/copyright` | Licença (Debian/Ubuntu; documentado, não executado) | Formato próprio Debian |
| `/usr/lib/firmware/` | Binários de firmware | 730 ficheiros aqui |
| `/proc/version` | Versão do kernel (virtual) | Janela do kernel, não ficheiro em disco |
| `/bin`, `/sbin`, `/lib`, `/lib64` | Symlinks para `usr/*` aqui (*merged-usr*) | Noutras distros podem ser diretórios reais |

## 4. Diferenças entre distribuições

| Família | Identificar distro/pacote | Evidência |
|---------|---------------------------|-----------|
| Arch (base deste teste) | `cat /etc/os-release`; `pacman -Qi` | **executada aqui** |
| Debian/Ubuntu | `cat /etc/os-release`; `dpkg -s <pacote>` / `apt show` | documentada, não executada aqui |
| Fedora/RHEL | `cat /etc/os-release`; `rpm -qi <pacote>` | documentada, não executada aqui |
| openSUSE | `cat /etc/os-release`; `rpm -qi` / `zypper info` | documentada, não executada aqui |
| Alpine | `cat /etc/os-release`; `apk info` | documentada, não executada aqui |
| Void | `cat /etc/os-release`; `xbps-query` | documentada, não executada aqui |
| NixOS | `cat /etc/os-release`; `nix-env -q` | documentada, não executada aqui |

### Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), 2026-10-15.
Comandos novos desta referência (`uname -a`, `hostnamectl`, `getconf -a`) executados
agora; restantes herdados dos tópicos `learn/` com a mesma evidência.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `uname -a` | linha completa do kernel | idêntica à transcrita | executado |
| `hostnamectl` (excerto) | SO, kernel, arquitetura | `Operating System: Omarchy`, `Kernel: Linux 7.2.5-3-omarchy`, `Architecture: x86-64` | executado |
| `getconf -a \| grep VERSION` | versões declaradas | `200809`, `700`, `POSIX2_VERSION 200809` | executado |
| Equivalentes `dpkg`/`rpm`/`apk`/`xbps`/`nix` | — | — | **não executados** |

Limitações: um único ambiente; gestores de outras famílias só documentados.

## 5. Ver também (sem duplicar)

- [o-que-e-linux-kernel-vs-distribuicao.md](../learn/o-que-e-linux-kernel-vs-distribuicao.md) — conceito kernel vs. distro
- [filosofia-unix-e-posix.md](../learn/filosofia-unix-e-posix.md) — POSIX e portabilidade
- [hierarquia-e-fhs-essencial.md](../learn/hierarquia-e-fhs-essencial.md) — hierarquia e FHS
- [licencas-e-software-livre-essencial.md](../learn/licencas-e-software-livre-essencial.md) — licenças
- [nao-consigo-identificar-o-sistema.md](../troubleshooting/nao-consigo-identificar-o-sistema.md) — diagnóstico quando a identificação falha

## 6. Referências oficiais

- kernel.org — "About Linux Kernel" — https://www.kernel.org/linux.html
- POSIX.1-2024, `<unistd.h>` (`_POSIX_VERSION = 202405L`) — https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/unistd.h.html
- FHS 3.0 — https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html
