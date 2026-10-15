---
title: "Sintoma: comando falhou ou saiu vazio"
category: troubleshooting
level: basico
prerequisites:
  - "03-comandos/learn/anatomia-comandos-pipes-e-redirecionamento"
distributions:
  - universal
requires:
  - "anatomia, pipes e redirecionamento"
related:
  - "03-comandos/reference/comandos-e-redirecionamento"
commands:
  - type
  - echo
  - cat
  - ls
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), bash 5.3.15"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Sintoma: comando falhou ou saiu vazio

## Sintoma

Sinais típicos: `command not found`; saída vazia com `rc=0`; ficheiro de saída vazio
ou truncado; erro visível mas "o script passou"; `grep` não acha texto visível no ficheiro.

## Hipóteses (ordenadas por probabilidade)

1. Comando inexistente ou fora do `PATH`.
2. Erro foi para o **outro canal** (stderr no terminal, stdout no ficheiro ou vice-versa).
3. `>` truncou o ficheiro antes da falha.
4. Falha silenciosa no **meio do pipe** (`$?` só vê o último).
5. Argumento partido (espaços sem aspas) ou filtro case-sensitive.

## Coleta de evidências

```bash
type <comando>                          # existe? (somente leitura)
<comando> > out.txt 2> err.txt; echo "rc=$?"  # separar canais + estado
cat out.txt err.txt                     # ler cada canal (somente leitura)
set -o pipefail                         # (bash) expor falha no meio do pipe
```

## Diagnóstico (como distinguir hipóteses)

| Hipótese | Evidência que confirma | Evidência que descarta |
|----------|------------------------|------------------------|
| Inexistente/`PATH` | `type` diz `not found` | `type` devolve caminho/builtin |
| Canal errado | `err.txt` tem o conteúdo "em falta" | ambos os ficheiros vazios |
| Truncado por `>` | `out.txt` vazio + `rc!=0` | `rc=0` com conteúdo parcial |
| Meio do pipe | `rc=0` mas resultado errado; `pipefail` muda para `!=0` | cada etapa isolada funciona |
| Argumento/filtro | `ls` mostra o ficheiro com espaços; `grep -i` acha | aspas + `-i` não mudam nada |

## Causa raiz

Quase sempre: **canal, etapa ou estado mal atribuído** — o comando fez exatamente o
pedido; o pedido é que mirava o sítio errado. Reproduzido aqui: `ls /naoexiste`
com `rc=2` e erro isolado em `err.txt` (ver evidência do tópico learn).

## Correção

- `not found`: instalar via gestor da distro ou corrigir `PATH` (detalhe em `08-pacotes`).
- Canal errado: separar `2>`; nunca juntar canais antes de diagnosticar.
- Truncado: reexecutar com `>>` após backup; `set -o noclobber` para prevenir.
- Meio do pipe: `set -o pipefail` (bash) ou testar etapas isoladas (POSIX).
- Todas reversíveis e sem escrita fora de ficheiros descartáveis.

## Validação (como confirmar que resolveu)

```bash
<comando> > out.txt 2> err.txt; echo "rc=$?"; cat out.txt err.txt
```

Resolvido quando: cada canal contém o esperado e `rc` reflete o sucesso real.
Pipes: validar com `pipefail` ligado ao menos uma vez.

## Prevenção

- Diagnóstico padrão primeiro: separar canais + `rc` sempre.
- `>>` por omissão em logs; `>` só com alvo confirmado.
- Aspas em caminhos; `grep -i` quando a caixa é incerta.

## Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, x86_64), bash 5.3.15, 2026-10-15. Hipóteses 2–4
reproduzidas de facto (`ls /naoexiste`, `false | true` ± `pipefail`); restantes por
procedimento documentado.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `ls /naoexiste > out 2> err; echo rc` | `rc=2`, erro isolado | idêntico | executado |
| `false \| true` ± `pipefail` | `0` vs `1` | idêntico | executado |
| `type` comando inexistente | `not found` | procedimento padrão (sem caso real) | documentado |

Limitações: nenhum caso real de `PATH` quebrado ou `noclobber` demonstrado.

## Referências oficiais

- Referência do eixo: [comandos-e-redirecionamento.md](../reference/comandos-e-redirecionamento.md)
- POSIX.1-2024, Shell Command Language — https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html
