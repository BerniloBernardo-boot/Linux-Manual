# Gráficos

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a pilha gráfica: Wayland vs. X11, compositores, drivers GPU
(AMD/Intel abertos, NVIDIA proprietário/NVK), e diagnóstico de "ecrã preto",
resolução errada e aceleração ausente — sem recomendar `nomodeset` permanente.

## Pré-requisitos

- `14-kernel`, `15-drivers` e `12-networking` (sessões remotas usam outros protocolos).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/wayland-vs-x11.md` | learn | Protocolos, compositores, XWayland, partilha de ecrã |
| `reference/gpu-e-sessao.md` | reference | `lspci`, `glxinfo`/`vulkaninfo`, variáveis `WAYLAND_DISPLAY`/`DISPLAY` |
| `troubleshooting/ecra-preto-ou-sem-aceleracao.md` | troubleshooting | Sessão cai para software, NVIDIA vs. nouveau, logs do compositor |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. A sessão gráfica varia muito
entre GNOME/KDE/Sway — os tópicos ensinam a identificar a sessão antes de agir
(`echo $XDG_SESSION_TYPE`).

## Notas técnicas do eixo

- Wayland é omissão em GNOME/KDE atuais; X11 mantém-se para casos legados e NVIDIA
  antiga — a escolha vive no gestor de login, não se impõe por variável.
- NVIDIA proprietário + Wayland amadureceu (GBM); `nouveau`/NVK são a via aberta,
  com performance variável por geração.
- Partilha de ecrã e gravação usam PipeWire/portais no Wayland — "não funciona no
  Discord/Zoom" é quase sempre portal ausente, não driver.
