# Docker

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar Docker no Linux: imagens vs. contentores, volumes, redes, `Dockerfile` e
`compose` — com alternativas rootless e a fronteira clara entre "Docker" (produto) e
"contentores" (conceito do eixo 23).

## Pré-requisitos

- `01-fundamentos` (kernel vs. userland), `04-filesystem` e `12-networking`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/docker-essencial.md` | learn | Imagem/camada/contentor, volumes, redes, `Dockerfile`, compose |
| `reference/dockerfile-e-compose.md` | reference | Instruções, boas práticas de camadas, compose essencial |
| `troubleshooting/contentor-nao-sobe.md` | troubleshooting | Daemon parado, permissão `docker.sock`, porta ocupada, imagem/arquitetura |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Preferir rootless ou grupo
`docker` consciente (equivale a root); registos e limites de recursos desde o início.

## Notas técnicas do eixo

- Socket `/run/docker.sock` = root: qualquer utilizador no grupo `docker` tem
  privilégio total efetivo — tratar como `sudo` sem palavra-passe.
- `latest` não é versão: fixar tags/digests em compose de anything sério.
- Dados em volumes/named volumes, nunca só na camada escrita do contentor
  (efémera por desenho).
