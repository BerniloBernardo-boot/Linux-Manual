# SISTEMA DE METADADOS

Todo documento importante (`learn/`, `reference/`, `29-labs/`, `30-cheatsheets/`) deve começar com front-matter YAML válido:

```yaml
---
title: "Permissões octais e simbólicas"
category: learn
level: basico
prerequisites:
  - "04-filesystem/learn/inodes-e-hierarquia"
distributions:
  - universal
requires:
  - "usuarios-e-grupos"
related:
  - "05-permissoes/reference/chmod-chown"
  - "13-seguranca/learn/acl"
commands:
  - chmod
  - chown
  - umask
risk: medio
verification: partially-tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64)"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---
```

## Campos

| Campo | Obrigatório | Valores / formato |
|-------|-------------|-------------------|
| `title` | sim | string, título exato do documento |
| `category` | sim | `learn` \| `reference` \| `troubleshooting` \| `lab` \| `cheatsheet` \| `diagram` \| `project` \| `glossary` |
| `level` | sim | `basico` \| `intermediario` \| `avancado` |
| `prerequisites` | não | lista de slugs/caminhos |
| `distributions` | sim | lista; `universal` ou subset de `debian, ubuntu, arch, fedora, rhel, opensuse, alpine, void, nixos, kali` |
| `requires` | não | lista de conceitos prévios |
| `related` | não | lista de documentos seguintes |
| `commands` | não | lista de comandos abordados |
| `risk` | sim | `baixo` \| `medio` \| `alto` \| `destrutivo` |
| `verification` | sim | `not-verified` \| `documented` \| `partially-tested` \| `tested` (ver `VERIFICACAO.md`) |
| `test_env` | se `partially-tested`/`tested` | string: distro + versão + kernel + arquitetura |
| `test_date` | se `partially-tested`/`tested` | `AAAA-MM-DD` da execução |
| `last_reviewed` | sim | `AAAA-MM-DD` |

> Campo `verified:` (booleano) **descontinuado na FASE 2B**: foi substituído por
> `verification:`. Se ainda presente num documento antigo, deve ser consistente
> (`verified: true` ⟺ `verification: tested`); documentos migrados já não o usam.

## Regras

1. `risk: alto/destrutivo` exige bloco `> ⚠️ Alerta` no corpo com reversão e alternativa segura.
2. `verified: true` só após executar exemplos e cross-distro check.
3. `distributions` nunca vazio; se universal, escrever `universal` e detalhar diferenças no corpo quando existirem.
4. O CI (`scripts/validate.py`) falha se: YAML inválido, campo obrigatório ausente, valor fora do enum, data inválida.
