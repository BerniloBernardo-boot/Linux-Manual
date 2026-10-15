# CONVENÇÕES

## Ficheiros e pastas

- Eixos fixos: `01-fundamentos/` ... `33-distributions/` (não renomear sem decisão registrada).
- Subpastas: `learn/`, `reference/`, `troubleshooting/` (minúsculas).
- Ficheiros de conteúdo: `kebab-case.md` (ex.: `chmod-chown.md`).
- Cada eixo tem `README.md` com: objetivo, pré-requisitos, mapa `learn → reference → troubleshooting`, estado no roadmap.
- Imagens (quando necessárias): `assets/` dentro do eixo; caminho relativo.

## Markdown

- Título H1 único por documento (= `title:` dos metadados).
- Blocos de código com linguagem (`bash`, `text`, `mermaid`).
- Comandos destrutivos (`rm -rf`, `dd`, `mkfs`, `:(){:|:&};:`, `chmod -R 777 /`): sempre com `> ⚠️` + o que pode quebrar + como desfazer.
- Saída esperada em bloco separado ```text``` após cada exemplo principal.
- Nunca deixar link interno para ficheiro inexistente.

## Mermaid

- Apenas fences ` ```mermaid ... ``` ` com diagrama válido (graph/flowchart/sequence).
- Deve explicar funcionamento, não decorar.

## Português

- Idioma principal: português. Manter em inglês: nomes de comandos, saídas, flags, nomes próprios, termos sem tradução consagrada (`bootloader`, `pipe`, `socket`).
- Tom direto, técnico, sem superlativos.

## Estatutos de verificação

- Ver `00-governanca/VERIFICACAO.md` (canónico desde a FASE 2B).
- Resumo: `verification: not-verified | documented | partially-tested | tested`.
  `tested`/`partially-tested` exigem `test_env:`, `test_date:` e subsecção
  `### Evidência de teste` no corpo. O antigo `verified: true/false` está
  descontinuado; `verified: true` nunca foi nem é prova genérica de qualidade.
