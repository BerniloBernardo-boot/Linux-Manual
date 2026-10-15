---
title: "Referência: terminal, tmux e atalhos"
category: reference
level: basico
prerequisites:
  - "02-terminal/learn/o-terminal-pty-e-o-shell"
distributions:
  - universal
requires:
  - "terminal, PTY e shell"
related:
  - "02-terminal/troubleshooting/terminal-comportamento-estranho"
commands:
  - tmux
  - tput
  - infocmp
  - stty
  - tty
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), tmux 3.7c, TERM=xterm-256color"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Referência: terminal, tmux e atalhos

> Documento de referência: tabelas, sintaxe e localizações — sem progressão
> didática. Exceção justificada ao template learn (missão §3): consolida o que o
> tópico `learn/` ensina; remete para ele em vez de repetir.

## 1. Tabela principal

### Variáveis e identificação

| Item | Comando | Valor aqui (executado) |
|------|---------|------------------------|
| Dialeto do terminal | `echo $TERM` | `xterm-256color` |
| Shell de login | `echo $SHELL` | `/usr/bin/bash` |
| Meu TTY | `tty` | `not a tty` (sem terminal de controlo) |
| Cores suportadas | `tput colors` | `256` |
| Capacidades | `infocmp \| head` | `xterm-256color`, `am bce ccc km …` |
| Escravos PTY | `ls /dev/pts/` | `0 1 ptmx` |
| Mestre PTY | `ls -l /dev/ptmx` | `crw-rw-rw- root tty 5, 2` |

### Atalhos readline (modo emacs, omissão do bash — executados via `bind -p`)

| Teclas | Ação |
|--------|------|
| `Ctrl+A` / `Ctrl+E` | início / fim da linha |
| `Ctrl+U` (`unix-line-discard`) | apaga até ao início (ver `bind -p`) |
| `Alt+Backspace` (`backward-kill-word`) | apaga palavra anterior |
| `Ctrl+L` (`clear-screen`) | limpa o ecrã, mantém a linha |
| `Ctrl+R` (`reverse-search-history`) | pesquisa no histórico |
| `Ctrl+C` / `Ctrl+D` | interrompe / EOF (disciplina de linha, `stty`) |

### tmux — sessão e janelas (prefixo **deste ambiente**: `C-Space`)

| Ação | Teclas (`P` = prefixo) | Comando equivalente |
|------|------------------------|---------------------|
| Nova sessão destacada | — | `tmux new-session -d -s nome` |
| Listar / anexar | — | `tmux ls` / `tmux attach -t nome` |
| Nova janela | `P c` | `tmux new-window` |
| Dividir vertical / horizontal | `P "` / `P %` | `split-window` / `split-window -h` |
| Última janela | `P l` | `last-window` |
| Desanexar (manter sessão) | `P d` | `detach-client` |
| Matar painel / sessão | — | `kill-pane` / `kill-session -t nome` |
| Modo cópia | `P [` | `copy-mode` |

Conceitos: [o-terminal-pty-e-o-shell.md](../learn/o-terminal-pty-e-o-shell.md).

## 2. Sintaxe e opções

```bash
tmux new-session -d -s <nome> [-x larg -y alt]  # sessão destacada
tmux ls                                        # listar sessões
tmux attach -t <nome>                          # anexar
tmux kill-session -t <nome>                    # destruir (reversível: só a sessão)
tmux show-options -g <opção>                   # ler config (ex.: prefix, status)
tput colors                                    # nº de cores do dialeto
infocmp [<dialeto>]                            # capacidades terminfo
stty -a                                        # disciplina de linha (exige TTY)
```

## 3. Ficheiros e localizações

| Caminho | Conteúdo |
|---------|----------|
| `/dev/ptmx`, `/dev/pts/*` | Mestre e escravos PTY |
| `~/.config/tmux/tmux.conf` | Config local (aqui: `set -g prefix C-Space`, `prefix2 C-b`) |
| `/usr/share/terminfo/` | Base terminfo (`x/xterm-256color` aqui) |
| `/tmp/tmux-<uid>/default` | Socket do servidor (some com `kill-server`) |

## 4. Diferenças entre distribuições

| Família | Notas | Evidência |
|---------|-------|-----------|
| Arch (base deste teste) | `tmux` 3.7c instalado; `screen` 5.0.2-2 só nos repos; prefixo local `C-Space` (config Omarchy), `C-b` como `prefix2` | **executada aqui** |
| Debian/Ubuntu | `tmux` e `screen` nos repos (`apt install tmux screen`); omissão upstream `C-b` salvo config | documentada, não executada aqui |
| Fedora/RHEL, openSUSE | Idem via `dnf`/`zypper` | documentada, não executada aqui |
| Alpine | `tmux` no repo `main`; `screen` pode faltar na base mínima | documentada, não executada aqui |

### Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, x86_64), tmux 3.7c, `TERM=xterm-256color`, 2026-10-15.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `bind -p \| grep …` | atalhos emacs | `C-a/C-e/C-l`, `backward-kill-word` etc. | executado |
| `tmux list-keys -T prefix` | teclas omissas | `" % c d l [ 0-9 & ,` presentes | executado |
| `tmux show-options -g prefix/status` (com servidor) | config efetiva | `prefix C-Space`, `status on` | executado |
| Config local (`~/.config/tmux/tmux.conf`) | origem do prefixo | `set -g prefix C-Space`, `prefix2 C-b` | executado |
| `screen` nos repos (`pacman -Si`) | disponibilidade | `screen 5.0.2-2`, não instalado | executado |

Limitações: atalhos de outros modos (vi) e de outras distros não testados.

## 5. Ver também (sem duplicar)

- [o-terminal-pty-e-o-shell.md](../learn/o-terminal-pty-e-o-shell.md) — conceitos
- [terminal-comportamento-estranho.md](../troubleshooting/terminal-comportamento-estranho.md) — diagnóstico

## 6. Referências oficiais

- `man 1 tmux` — multiplexador (sessões, teclas, opções).
- `man 1 stty` + POSIX XCU `stty` — https://pubs.opengroup.org/onlinepubs/9799919799/utilities/stty.html
- `man 5 terminfo` — base de capacidades do terminal.
