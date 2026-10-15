# Áudio

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a pilha de áudio: ALSA (hardware), PipeWire/PulseAudio (servidores de sessão),
e diagnóstico de "sem som", dispositivo errado e Bluetooth instável — com comandos
somente leitura primeiro.

## Pré-requisitos

- `06-processos` (servidores por utilizador) e `15-drivers`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/alsa-pipewire-e-pulse.md` | learn | Camadas, `wpctl`/`pactl`, perfis e sinks |
| `reference/audio-diagnostico.md` | reference | Tabelas: `wpctl`, `pactl`, `alsamixer`, `dmesg | grep -i audio` |
| `troubleshooting/sem-som.md` | troubleshooting | Mudo? sink errado? perfil HDMI? Bluetooth? — isolar a camada |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Regra: nunca apagar config de
áudio do utilizador (`~/.config/pipewire`, `~/.config/pulse`) sem backup — é onde
vivem os perfis que funcionavam.

## Notas técnicas do eixo

- PipeWire é omissão nas distros atuais (substitui PulseAudio e JACK para o comum);
  `pactl` ainda funciona via compatibilidade na maioria dos casos.
- "Sem som após update" é quase sempre perfil/mudo, não driver: `wpctl status` e
  `alsamixer` (canal MM = mudo) antes de reinstalar seja o que for.
- Bluetooth usa perfil A2DP (música) vs. HSP/HFP (chamada, pior qualidade) — a troca
  automática errada é o sintoma clássico.
