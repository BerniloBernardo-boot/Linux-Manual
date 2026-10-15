---
title: "Sintoma: terminal com comportamento estranho"
category: troubleshooting
level: basico
prerequisites:
  - "02-terminal/learn/o-terminal-pty-e-o-shell"
distributions:
  - universal
requires:
  - "terminal, PTY e shell"
related:
  - "02-terminal/reference/terminal-tmux-e-atalhos"
commands:
  - tty
  - stty
  - tput
  - infocmp
  - tmux
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), tmux 3.7c"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Sintoma: terminal com comportamento estranho

## Sintoma

Qualquer destes: `stty: Inappropriate ioctl for device`; `tty` responde `not a tty`;
cores trocadas ou `tput: unknown terminal`; artefactos (`^[[A`, quadrados) no `vim`/`less`;
teclas de função não funcionam dentro de `tmux`/SSH; sessão "morta" ao fechar a janela.

## Hipóteses (ordenadas por probabilidade)

1. **Sem TTY**: stdin é pipe/ficheiro/CI — não há terminal para configurar.
2. **`TERM` errado ou ausente** no contexto atual (herdado, SSH, `tmux` aninhado).
3. **Base terminfo ausente** no sistema remoto/mínimo.
4. Processo **preso ao PTY** que morreu (janela/SSH fechada sem multiplexador).

## Coleta de evidências

```bash
tty; ps -o pid,comm,tty -p $$   # há terminal de controlo? (somente leitura)
echo "TERM=$TERM"; tput colors  # dialeto válido? (somente leitura)
infocmp 2>&1 | head -n 2        # terminfo existe para este TERM?
tmux ls 2>&1                    # há multiplexador? (somente leitura)
ls /dev/pts/                    # que sessões existem? (somente leitura)
```

## Diagnóstico (como distinguir hipóteses)

| Hipótese | Evidência que confirma | Evidência que descarta |
|----------|------------------------|------------------------|
| Sem TTY | `not a tty` + `TT=?` + `stty` com `ioctl` | `tty` devolve `/dev/pts/N` |
| `TERM` errado | `tput: unknown terminal "..."` ou cores só no remoto | `infocmp` descreve o dialeto sem erro |
| terminfo ausente | `infocmp` falha no remoto, funciona no local | `ls /usr/share/terminfo` tem a entrada |
| PTY morto | Janela fechada, processo órfão, sem `tmux` | `tmux ls` mostra a sessão destacada |

## Causa raiz

Na maioria dos casos: Layer errada — tenta-se configurar (`stty`), colorir (`tput`) ou
interagir onde **não há terminal**, ou com **dialeto errado**. O mecanismo PTY/terminfo
está correto; a suposição sobre o contexto é que está errada.

## Correção

- Sem TTY: **nenhuma correção no sistema** — executar a parte interativa num terminal
  real; em scripts, ramificar (`[ -t 0 ] && …`).
- `TERM` errado: `export TERM=xterm-256color` (ou o dialeto do emulador real) **só na
  sessão afetada** — reversível por fechar a sessão; nunca forçar `TERM` dentro de
  `tmux` para o dialeto exterior (parte teclas; ver desafio do tópico learn).
- terminfo ausente no remoto: instalar pacote terminfo/ncurses do remoto
  (**documentado, não executado aqui**).
- PTY morto sem `tmux`: não há resgate; da próxima vez, sessão destacada
  (`tmux new-session -d`), que sobrevive — provado na evidência do tópico learn.

## Validação (como confirmar que resolveu)

```bash
tty && tput colors && infocmp >/dev/null && echo TERMINAL-OK
```

Resolvido quando: `tty` devolve `/dev/pts/N`, `tput` responde sem erro e os artefactos
desaparecem. Em `tmux`: `echo $TERM` mostra o dialeto do tmux, não o exterior.

## Prevenção

- Verificar `[ -t 0 ]` em scripts antes de `stty`/`tput`.
- Não propagar `TERM` exótico por SSH para sistemas mínimos.
- Trabalho longo/remoto sempre em `tmux` destacado; `kill-server` no fim em máquinas partilhadas.

## Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, x86_64), tmux 3.7c, 2026-10-15. Sintomas 1 e 4
reproduzidos de facto neste ambiente (sem TTY); sintomas 2–3 diagnosticados por
eliminação, com correção marcada como documentada.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `tty` | `not a tty` (sem TTY aqui) | `not a tty` | executado |
| `stty -a` sem TTY | erro honesto | `Inappropriate ioctl for device` | executado |
| `tput colors` + `infocmp` (dialeto válido) | `256`, descrição OK | idêntico | executado |
| ciclo tmux sobrevive sem janela | sessão destacada persiste | criada/listada/morta a pedido | executado |
| terminfo ausente no remoto | — | — | **não reproduzido** (sem 2.ª máquina) |

Limitações: sem SSH/remoto real; correções de `TERM`/terminfo noutros sistemas só documentadas.

## Referências oficiais

- Referência do eixo: [terminal-tmux-e-atalhos.md](../reference/terminal-tmux-e-atalhos.md)
- `man 1 stty`, `man 1 tput`, `man 1 tmux`.
