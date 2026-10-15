# DevOps

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a ponte dev→prod no Linux: CI (pipelines que testam o que os tópicos ensinam),
infraestrutura como código (conceitos, Ansible intro), observabilidade (logs, métricas)
— sem vender ferramenta específica como "o DevOps".

## Pré-requisitos

- `21-git`, `22-docker`, `25-servidores` e `07-shell`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/ci-e-iac.md` | learn | Pipeline mínimo (lint→test→build), idempotência, declarativo vs. imperativo |
| `reference/pipelines-e-ansible.md` | reference | Estágios comuns, inventário/playbook mínimo, segredos (vault/vars encriptadas) |
| `troubleshooting/pipeline-falha.md` | troubleshooting | Falha flaky vs. real, cache, runner sem dependência, segredo ausente |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Exemplos executáveis localmente
(`act` ou runner local) antes de qualquer serviço externo.

## Notas técnicas do eixo

- Segredos nunca em git em claro: variáveis de ambiente do CI ou cofre; exemplo com
  segredo hardcoded é proibido.
- Idempotência primeiro: reaplicar sem mudar nada deve dar "ok, sem alterações".
- Pipeline que só corre no final não protege nada: falhar cedo (lint+testes rápidos
  nos primeiros estágios).
