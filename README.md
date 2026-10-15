# Linux Manual — Knowledge Base + Learning Path + Lab + Troubleshooting

> Base de conhecimento Linux multi-distribuição: manual → curso → laboratório → referência → guia de diagnóstico.
> Idioma principal: **português**. Termos técnicos mantidos em inglês quando não há tradução consagrada.

## Três modos de uso

| Modo | Caminho | Entrada |
|------|---------|---------|
| **LEARN** | Fundamentos → intermediário → avançado | `01-fundamentos/` → `27-automacao/` |
| **SOLVE** | Sintoma → diagnóstico → causa → solução | `19-troubleshooting/` + `*/troubleshooting/` |
| **BUILD** | Laboratório → projeto → sistema real | `29-labs/` → `28-projetos/` |

## Estrutura (híbrida — decisão FASE 0)

- **Eixos de conteúdo (§3):** `01-...` até `33-...` (33 pastas numeradas).
- **Tipos de uso (§13):** dentro de cada eixo `01–27`: `learn/` · `reference/` · `troubleshooting/`.
- **Transversais:** `28-projetos/` · `29-labs/` · `30-cheatsheets/` · `31-diagrams/` · `32-glossary/` · `33-distributions/` · `19-troubleshooting/`.
- Detalhe: `00-governanca/ARQUITETURA.md`.

```text
01-fundamentos/
├── learn/            # conceito → mecanismo → exemplo
├── reference/        # sintaxe, ficheiros, tabelas
└── troubleshooting/  # sintoma → hipótese → diagnóstico → correção
```

Relações entre conteúdos (exemplo):

```text
Permissões (05)
   ↓
Utilizadores e Grupos
   ↓
Filesystem (04)
   ↓
ACL
   ↓
Segurança (13)
```

## Regras absolutas

1. **Precisão > quantidade.** Conceito antes do comando.
2. **Nunca assumir comando universal.** Toda diferença Debian / Arch / Fedora / openSUSE / Alpine / Void / NixOS deve ser explicitada (ver `00-governanca/MATRIZ-DISTRIBUICOES.md`).
3. **Não publicar sem verificar.** Loop por tópico: RESEARCH → DEFINE → DESIGN → WRITE → VERIFY → TEST → CROSS-DISTRO CHECK → REVIEW → PUBLISH.
4. **Segurança primeiro.** Comando destrutivo exige alerta, condição de reversão e alternativa mais segura.
5. **Parar e perguntar** diante de arquitetura ambígua, informação conflitante, dependência de versão ou risco elevado. Não inventar.

## Metadados

Todo documento em `learn/`, `reference/`, `29-labs/` e `30-cheatsheets/` deve ter front-matter YAML conforme `00-governanca/METADADOS.md`. Documentos sem metadados falham no CI (`scripts/validate.py`).

## Como começar

- Iniciante: `01-fundamentos/learn/` → `02-terminal/` → `03-comandos/` → `04-filesystem/` → `05-permissoes/`.
- Diagnóstico: `19-troubleshooting/README.md`.
- Prática: `29-labs/README.md`.
- Referência rápida: `30-cheatsheets/`.
- Compatibilidade: `33-distributions/`.

## Cobertura da documentação

> Fonte canónica: `ROADMAP.md`. Resumo de 2026-10-15: **3/33 eixos com conteúdo
> completo e testado** (`01`: 6 docs, `02`: 3 docs, `03`: 3 docs); restantes eixos
> com README de escopo (objetivo, pré-requisitos, documentos planeados) e conteúdo
> por escrever. Nenhum esqueleto é apresentado como documentação.

| Fase | Eixos | Estado |
|------|-------|--------|
| FASE 2 — Fundamentos | `01-fundamentos` | complete (6 docs, tested) |
| FASE 3 — Terminal + comandos | `02-terminal`, `03-comandos` | complete (3+3 docs, tested) |
| FASE 4 — Filesystem/permissões/processos | `04`, `05`, `06` | READMEs de escopo; conteúdo planned |
| FASE 5 — Shell + pacotes | `07`, `08` | idem |
| FASE 6 — Systemd + boot + storage | `09`, `10`, `11` | idem |
| FASE 7 — Networking + segurança | `12`, `13` | idem |
| FASE 8 — Kernel/drivers/perf.+gráficos/áudio | `14`, `15`, `18`, `16`, `17` | idem |
| FASE 9 — Troubleshooting | `19` | índice por sintoma planeado |
| FASE 10 — Dev→DevOps | `20`–`27` | READMEs de escopo; conteúdo planned |
| FASE 11 — Labs e projetos | `28`, `29` | formatos e catálogo planeados |
| FASE 12 — Refs/diagramas/glossário/distros | `30`, `31`, `32`, `33` | idem |

## Publicado

- Cobertura acima + `00-governanca/` (5 docs vigentes). Este README é frontispício:
  regras, estrutura, modos de uso e estado — o conteúdo didático vive nos eixos.

## Estado do projeto

Ver `ROADMAP.md`. Nenhum módulo está marcado `complete` apenas por existir ficheiro — só após `planned → researching → writing → verifying → tested → reviewed → complete`.

## Contribuição

Ver `CONTRIBUTING.md` e `00-governanca/CONVENCOES.md`.
