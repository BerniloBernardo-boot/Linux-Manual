# Performance

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a medir antes de otimizar: CPU, memória, I/O e rede com ferramentas por camada
(`top`/`htop`, `free`, `iostat`, `vmstat`, `perf` intro), e a distinguir sintoma
(lentidão) de causa (swap, I/O, processo, rede) com números, não palpites.

## Pré-requisitos

- `06-processos`, `11-storage` e `14-kernel`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/medir-antes-de-otimizar.md` | learn | Metodologia: baseline, uma variável, `time`, percentis |
| `reference/ferramentas-de-medicao.md` | reference | Tabelas por camada: CPU/mem/I/O/rede e o que cada métrica significa |
| `troubleshooting/sistema-lento.md` | troubleshooting | `load average` alta sem CPU? swap? I/O? OOM-killer? — árvore de decisão |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Regra de ouro do eixo: nenhum
tuning sem medição antes/depois; "otimizações" copiadas (`swappiness=10`, governors)
sem diagnóstico são proibidas nos exemplos.

## Notas técnicas do eixo

- `load average` alta com CPU livre = espera de I/O (estado `D`), não falta de CPU.
- Swap usado não é doença (páginas frias); doença é `swapin/out` contínuo (thrashing).
- OOM-killer (`dmesg | grep -i oom`) mata por pressão de memória — a correção é
  capacidade ou limites (cgroups/systemd), não desativar o OOM.
