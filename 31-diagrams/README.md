# Diagrams

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Explicar funcionamento com diagramas Mermaid que renderizam: boot, kernel, processos,
filesystem, permissões, systemd, networking, DNS, contentores, storage — diagrama que
só decora não entra.

## Pré-requisitos

- O eixo correspondente (diagrama ilustra o mecanismo já ensinado).

## Documentos planeados

| Documento | Escopo |
|-----------|--------|
| `boot.md` | Firmware → bootloader → kernel → init |
| `rede-e-dns.md` | Camadas, resolução de nomes, firewall |
| `contentores.md` | Namespaces, cgroups, imagem vs. contentor |
| `storage.md` | Partição → filesystem → montagem → subvolume |

Cada diagrama exige `category: diagram`, Mermaid válido (o CI valida fence + tipo) e
legenda que diga o que o diagrama prova.

## Como usar

Ligados a partir dos tópicos `learn/`; este eixo é galeria + fonte única (evita o
mesmo diagrama copiado em 3 tópicos).

## Notas técnicas do eixo

- `flowchart`/`sequenceDiagram` conforme o caso; `flowchart TB/LR` legível em ecrã
  pequeno; sem HTML excessivo nos rótulos.
