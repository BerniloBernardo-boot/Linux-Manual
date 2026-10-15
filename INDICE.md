# ÍNDICE

> Gerado manualmente na FASE 1. Futuro: gerar automaticamente a partir dos metadados YAML.

## Eixos

- `01-fundamentos/` — o que é Linux, kernel vs. distro, filosofia Unix/POSIX, hierarquia/FHS, licenças, LEARN/SOLVE/BUILD ([tópico 1](01-fundamentos/learn/o-que-e-linux-kernel-vs-distribuicao.md), [tópico 2](01-fundamentos/learn/filosofia-unix-e-posix.md), [tópico 3](01-fundamentos/learn/hierarquia-e-fhs-essencial.md), [tópico 4](01-fundamentos/learn/licencas-e-software-livre-essencial.md))
- `02-terminal/` — emuladores, PTY, readline, multiplexadores ([learn](02-terminal/learn/o-terminal-pty-e-o-shell.md), [reference](02-terminal/reference/terminal-tmux-e-atalhos.md), [troubleshooting](02-terminal/troubleshooting/terminal-comportamento-estranho.md))
- `03-comandos/` — anatomia, man/info, redirecionamento, pipes ([learn](03-comandos/learn/anatomia-comandos-pipes-e-redirecionamento.md), [reference](03-comandos/reference/comandos-e-redirecionamento.md), [troubleshooting](03-comandos/troubleshooting/comando-falhou-ou-saiu-vazio.md))
- `04-filesystem/` — hierarquia, inodes, links, montagem
- `05-permissoes/` — octal/simbólico, umask, ACL, sudo
- `06-processos/` — PID, sinais, jobs, nice, cgroups (visão geral)
- `07-shell/` — bash, scripting, expansões, dotfiles
- `08-pacotes/` — apt/pacman/dnf/zypper/apk/xbps/nix
- `09-systemd/` — units, journalctl, timers (+ alternativas sem systemd)
- `10-boot/` — firmware, bootloader, initramfs, runlevels/targets
- `11-storage/` — partições, LVM, filesystems, swap
- `12-networking/` — IP, roteamento, DNS, NetworkManager/systemd-networkd
- `13-seguranca/` — utilizadores, firewall, SELinux/AppArmor, SSH
- `14-kernel/` — módulos, sysctl, versões
- `15-drivers/` — firmware, DKMS
- `16-graficos/` — X11/Wayland, GPU
- `17-audio/` — ALSA/PipeWire/PulseAudio
- `18-performance/` — profiling, i/o, memória
- `19-troubleshooting/` — enciclopédia por sintoma
- `20-desenvolvimento/` — toolchain, gcc, make
- `21-git/` — (ponte com repositório Git existente)
- `22-docker/` · `23-containers/` · `24-virtualizacao/` — isolamento e VMs
- `25-servidores/` — nginx, SSH server, logs
- `26-devops/` — CI, IaC visão geral
- `27-automacao/` — cron/systemd timers, Ansible visão geral
- `28-projetos/` — guiados e livres
- `29-labs/` — laboratórios com falha intencional
- `30-cheatsheets/` — referência rápida
- `31-diagrams/` — Mermaid por subsistema
- `32-glossary/` — glossário
- `33-distributions/` — particularidades por família

## Trilhas

- LEARN: `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → ...`
- SOLVE: começar em `19-troubleshooting/README.md`.
- BUILD: `29-labs/README.md → 28-projetos/README.md`.
