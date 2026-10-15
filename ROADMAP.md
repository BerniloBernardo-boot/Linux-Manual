# ROADMAP

> Estado oficial de progresso. Regra: nunca marcar `complete` apenas porque o ficheiro foi criado.
> Ciclo por módulo: `planned → researching → writing → verifying → tested → reviewed → complete`.

## Legenda

- `[x]` complete (publicado + testado + revisado)
- `[~]` em progresso (com fase indicada)
- `[ ]` planned

## FASE 1 — Estrutura principal

- [x] FASE 0 — Auditoria (repositório vazio confirmado em 2026-10-15)
- [x] Arquitetura híbrida definida (`00-governanca/ARQUITETURA.md`)
- [x] Sistema de metadados (`00-governanca/METADADOS.md`)
- [x] Matriz de distribuições (`00-governanca/MATRIZ-DISTRIBUICOES.md`)
- [x] Convenções (`00-governanca/CONVENCOES.md`)
- [x] Templates (tópico / lab / troubleshooting)
- [x] CI de validação (`scripts/validate.py` + `.github/workflows/validate.yml`)
- [x] FASE 2A — Auditoria técnica dos 2 primeiros tópicos (4 correções, 2026-10-15)
- [x] FASE 2B — Política de verificação (`00-governanca/VERIFICACAO.md`, esquema `verification:`, validador atualizado, 2 tópicos migrados)
- [x] Esqueleto 01–33 + README por módulo

## FASEs 2–12 — Conteúdo

```text
ROADMAP
├── [x] FASE 2  Fundamentos (01) — concluída: 6 documentos (4 learn + 1 reference + 1 troubleshooting), todos tested
├── [~] FASE 3  Terminal + comandos (02 e 03 complete)
├── [ ] FASE 4  Filesystem + permissões + processos (04, 05, 06)
├── [ ] FASE 5  Shell + pacotes (07, 08)
├── [ ] FASE 6  Systemd + boot + storage (09, 10, 11)
├── [ ] FASE 7  Networking + segurança (12, 13)
├── [ ] FASE 8  Kernel + drivers + performance (14, 15, 18) + gráficos/áudio (16, 17)
├── [ ] FASE 9  Troubleshooting (19)
├── [ ] FASE 10 Desenvolvimento + Git + Docker + containers + virt + servidores + DevOps + automação (20–27)
├── [ ] FASE 11 Labs e projetos (28, 29)
└── [ ] FASE 12 Cheatsheets + diagramas + glossário (30, 31, 32) + distribuições (33)
```

### Detalhe por módulo

| Módulo | Estado | Responsável | Notas |
|--------|--------|-------------|-------|
| 01-fundamentos | complete (6 docs, todos `verification: tested`; revisão: 2A/2D/2E + Fase D) | — | eixo fechado |
| 02-terminal | complete (3 docs, todos `verification: tested`) | — | eixo fechado 2026-10-15 |
| 03-comandos | complete (3 docs, todos `verification: tested`) | — | eixo fechado 2026-10-15 |
| 04-filesystem | planned | — | |
| 05-permissoes | planned | — | |
| 06-processos | planned | — | |
| 07-shell | planned | — | |
| 08-pacotes | planned | — | matriz apt/pacman/dnf/zypper/apk/xbps/nix |
| 09-systemd | planned | — | incluir alternativas sem systemd |
| 10-boot | planned | — | |
| 11-storage | planned | — | |
| 12-networking | planned | — | |
| 13-seguranca | planned | — | |
| 14-kernel | planned | — | |
| 15-drivers | planned | — | |
| 16-graficos | planned | — | |
| 17-audio | planned | — | |
| 18-performance | planned | — | |
| 19-troubleshooting | planned | — | metodologia sintoma→prevenção |
| 20-desenvolvimento | planned | — | |
| 21-git | planned | — | |
| 22-docker | planned | — | |
| 23-containers | planned | — | |
| 24-virtualizacao | planned | — | |
| 25-servidores | planned | — | |
| 26-devops | planned | — | |
| 27-automacao | planned | — | |
| 28-projetos | planned | — | |
| 29-labs | planned | — | |
| 30-cheatsheets | planned | — | |
| 31-diagrams | planned | — | Mermaid validado |
| 32-glossary | planned | — | |
| 33-distributions | planned | — | |

## FASE 13 — Auditoria final

- [ ] Links, comandos, referências, Mermaid, YAML, metadados, duplicação, nomenclatura — tudo verde no CI.
