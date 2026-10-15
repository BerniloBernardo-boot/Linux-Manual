#!/usr/bin/env python3
"""Validação do Linux Manual (§18): metadados, links internos, Mermaid, nomenclatura.

Uso: python3 scripts/validate.py [--strict]
Retorna 0 se OK, 1 se houver erros.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = {"title", "category", "level", "distributions", "risk", "verification", "last_reviewed"}
CATEGORIES = {"learn", "reference", "troubleshooting", "lab", "cheatsheet", "diagram", "project", "glossary"}
LEVELS = {"basico", "intermediario", "avancado"}
RISKS = {"baixo", "medio", "alto", "destrutivo"}
VERIFICATIONS = {"not-verified", "documented", "partially-tested", "tested"}
EVIDENCE_RE = re.compile(r"^#{2,3}\s*Evidência de teste", re.IGNORECASE | re.MULTILINE)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[.*?\]\((?!http|#|mailto:)([^)]+)\)")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)

errors: list[str] = []
warnings: list[str] = []


def parse_simple_yaml(text: str) -> tuple[dict, str | None]:
    """Parser mínimo para o subset de YAML usado no front-matter (sem dependências).

    Suporta:
      chave: valor
      chave: [a, b]
      chave:
        - item
        - item
    """
    data: dict = {}
    current_list_key: str | None = None
    for i, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.strip().startswith("#"):
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if current_list_key is None:
                return {}, f"linha {i} item de lista sem chave: {line!r}"
            data[current_list_key].append(stripped[2:].strip().strip('"\''))
            continue
        if ":" not in line:
            return {}, f"linha {i} sem ':': {line!r}"
        key, val = line.split(":", 1)
        key, val = key.strip(), val.strip()
        current_list_key = None
        if val == "":
            data[key] = []
            current_list_key = key
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip('"\'') for v in inner.split(",") if v.strip()] if inner else []
        elif val.lower() in ("true", "false"):
            data[key] = val.lower() == "true"
        elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            data[key] = val[1:-1]
        else:
            data[key] = val
    return data, None


def check_markdown(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()

    # Exige front-matter apenas nas pastas de conteúdo
    needs_fm = any(s in rel for s in ("/learn/", "/reference/", "/troubleshooting/",
                                       "29-labs/", "30-cheatsheets/", "31-diagrams/",
                                       "19-troubleshooting/"))
    m = FRONTMATTER_RE.match(text)
    if needs_fm and "README.md" not in rel:
        if not m:
            errors.append(f"{rel}: sem front-matter YAML")
            return
        data, perr = parse_simple_yaml(m.group(1))
        if perr:
            errors.append(f"{rel}: YAML inválido ({perr})")
            return
        missing = REQUIRED_FIELDS - set(data)
        if missing:
            errors.append(f"{rel}: campos ausentes: {sorted(missing)}")
        if data.get("category") not in CATEGORIES:
            errors.append(f"{rel}: category inválida: {data.get('category')!r}")
        if data.get("level") not in LEVELS:
            errors.append(f"{rel}: level inválido: {data.get('level')!r}")
        if data.get("risk") not in RISKS:
            errors.append(f"{rel}: risk inválido: {data.get('risk')!r}")
        verif = data.get("verification")
        if verif not in VERIFICATIONS:
            errors.append(f"{rel}: verification inválida: {verif!r} (usar not-verified|documented|partially-tested|tested)")
        if verif in ("partially-tested", "tested"):
            if not isinstance(data.get("test_env"), str) or not data["test_env"].strip():
                errors.append(f"{rel}: verification {verif} exige test_env não vazio")
            if not DATE_RE.match(str(data.get("test_date", ""))):
                errors.append(f"{rel}: verification {verif} exige test_date AAAA-MM-DD")
            body = text[m.end():]
            if not EVIDENCE_RE.search(body):
                errors.append(f"{rel}: verification {verif} exige subsecção '### Evidência de teste' no corpo")
        # Campo legado: se presente, deve ser bool e consistente com verification
        if "verified" in data:
            if not isinstance(data["verified"], bool):
                errors.append(f"{rel}: verified legado deve ser true/false")
            elif data["verified"] != (verif == "tested"):
                errors.append(f"{rel}: verified legado inconsistente com verification {verif!r}")
        if not DATE_RE.match(str(data.get("last_reviewed", ""))):
            errors.append(f"{rel}: last_reviewed deve ser AAAA-MM-DD")
        dists = data.get("distributions", [])
        if not isinstance(dists, list) or not dists:
            errors.append(f"{rel}: distributions deve ser lista não vazia")
        if data.get("risk") in ("alto", "destrutivo") and "⚠️" not in text:
            errors.append(f"{rel}: risk alto/destrutivo sem bloco de alerta ⚠️")

    # Links internos
    for target in LINK_RE.findall(text):
        t = target.split("#")[0].strip()
        if not t:
            continue
        candidate = (path.parent / t).resolve()
        if not candidate.exists():
            errors.append(f"{rel}: link quebrado → {target}")

    # Mermaid: fence balanceado + palavra-chave de diagrama
    for block in MERMAID_RE.findall(text):
        if not re.search(r"(graph|flowchart|sequenceDiagram|classDiagram|stateDiagram|erDiagram|gantt|pie)", block):
            errors.append(f"{rel}: bloco mermaid sem tipo de diagrama reconhecível")

    if text.count("```") % 2 != 0:
        errors.append(f"{rel}: fence de código não balanceado")


def main() -> int:
    mds = sorted(ROOT.rglob("*.md"))
    # ignora .git
    mds = [p for p in mds if ".git/" not in p.as_posix()]
    for p in mds:
        check_markdown(p)

    # Nomenclatura: conteúdo em kebab-case (governança raiz e 00-governanca usam MAIÚSCULAS por convenção)
    ALLOW_UPPER = {"README.md", "CONTRIBUTING.md", "ROADMAP.md", "INDICE.md",
                   "ARQUITETURA.md", "CONVENCOES.md", "METADADOS.md", "MATRIZ-DISTRIBUICOES.md",
                   "VERIFICACAO.md"}
    for p in mds:
        name = p.stem
        if p.name in ALLOW_UPPER or p.name == "README.md":
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            errors.append(f"{p.relative_to(ROOT)}: nome fora do kebab-case")

    # Duplicação de títulos (front-matter title)
    seen: dict[str, str] = {}
    for p in mds:
        m = FRONTMATTER_RE.match(p.read_text(encoding="utf-8"))
        if m:
            data, _ = parse_simple_yaml(m.group(1))
            t = str(data.get("title", "")).strip().lower()
            if t:
                if t in seen:
                    warnings.append(f"título duplicado {t!r}: {seen[t]} ↔ {p.relative_to(ROOT)}")
                else:
                    seen[t] = p.relative_to(ROOT).as_posix()

    for w in warnings:
        print(f"WARN: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\nArquivos verificados: {len(mds)} | erros: {len(errors)} | avisos: {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
