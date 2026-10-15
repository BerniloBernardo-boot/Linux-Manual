# Containers

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar os mecanismos, não a marca: namespaces, cgroups, capabilities, seccomp e
imagens OCI — e as alternativas (Podman, LXC/systemd-nspawn), para que "Docker"
deixe de ser magia.

## Pré-requisitos

- `06-processos` (cgroups intro), `22-docker` e `04-filesystem`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/namespaces-e-cgroups.md` | learn | Isolamento (mnt/pid/net/uts) + limites (cpu/memória), `unshare` |
| `reference/podman-e-lxc.md` | reference | Podman rootless, `podman`≅`docker` CLI, LXC vs. app containers |
| `troubleshooting/isolamento-falha.md` | troubleshooting | Permissão negada, rede do contentor, DNS, limites OOM |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Demonstrações com `unshare`
sem privilégio quando possível; o resto documenta requisitos de privilégio.

## Notas técnicas do eixo

- Contentor ≠ VM: partilha o kernel do host (ver tópico 1 de fundamentos) —
  `uname -r` dentro é o do host.
- Podman rootless (`podman` sem daemon) evita o problema do socket root do Docker.
- `--privileged` desliga quase todo o isolamento: proibido como exemplo padrão,
  só com justificativa e alternativa (`--cap-add` mínima).
