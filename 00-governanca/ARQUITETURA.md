# ARQUITETURA DO CONTEÚDO

> Decisão FASE 0 (2026-10-15): **híbrida**. Resolve o conflito entre §3 (33 pastas numeradas) e §13 (8 pastas por tipo de uso).

## Decisão

- **Eixos (§3) são o esqueleto físico:** `01-...` a `33-...` na raiz.
- **Tipos (§13) são visões lógicas**, implementadas como:
  - subpastas `learn/`, `reference/`, `troubleshooting/` dentro de cada eixo `01–27`;
  - pastas transversais `28-projetos/`, `29-labs/`, `30-cheatsheets/`, `31-diagrams/`, `32-glossary/`, `33-distributions/`, `19-troubleshooting/`;
  - metadados `category:` + índices gerados (futuro: script que monta trilhas LEARN/SOLVE/BUILD a partir do YAML).

## Mapa físico

```text
00-governanca/          # arquitetura, metadados, matriz, convenções (não é conteúdo Linux)
01-fundamentos/ ... 27-automacao/
│   ├── learn/              # Learning
│   ├── reference/          # Reference
│   └── troubleshooting/    # Troubleshooting (sintoma local do eixo)
19-troubleshooting/     # enciclopédia transversal (sintoma → prevenção)
28-projetos/           # Projects (guiados, livres)
29-labs/               # Labs (objetivo → cleanup → desafio)
30-cheatsheets/        # Cheatsheets (referência rápida, com risco sinalizado)
31-diagrams/           # Diagrams (Mermaid funcional)
32-glossary/           # Glossary
33-distributions/      # Distributions (matriz + particularidades por família)
templates/ scripts/ tools/ .github/
```

## Relações obrigatórias (evitar páginas isoladas)

Cada documento `learn/` deve preencher `requires:` (pré-requisitos) e `related:` (próximos passos).
Exemplo canônico:

```text
Permissões (05)
   ↓
Utilizadores & Grupos
   ↓
Filesystem (04)
   ↓
ACL
   ↓
Segurança (13)
```

Outras cadeias a respeitar ao escrever:

- Terminal (02) → Comandos (03) → Shell (07) → Automação (27)
- Pacotes (08) → Systemd (09) → Boot (10) → Storage (11)
- Networking (12) → Segurança (13) → Servidores (25)
- Kernel (14) → Drivers (15) → Performance (18)
- Git (21) → Docker (22) → Containers (23) → DevOps (26)

## Regras

1. Nada de páginas órfãs: todo `learn/` tem ao menos um `requires` ou `related`.
2. Conceito universal explicado uma vez; diferenças por distro vão em tabela + `33-distributions/`.
3. `19-troubleshooting/` referencia eixos, não duplica conteúdo.
4. `29-labs/` referencia `learn/` + `reference/` correspondentes.
