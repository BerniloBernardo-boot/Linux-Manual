# Labs

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Praticar com as mãos em ambiente descartável: cada lab segue o formato obrigatório
(objetivo → pré-requisitos → ambiente → execução → verificação → falha intencional →
diagnóstico → correção → cleanup → desafio), com variantes por distribuição quando
houver diferença.

## Pré-requisitos

- O eixo correspondente ao tema do lab; ambiente descartável (VM, contentor, dir temporário).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `guiados/lab-permissoes.md` | lab | `chmod`/`chown`/`umask`/ACL com verificação e falha intencional |
| `guiados/lab-rede.md` | lab | IP, rotas, DNS e diagnóstico por camadas |
| `guiados/lab-systemd.md` | lab | Unit + timer próprios, journal, falha e recuperação |
| `falha-intencional/catalogo.md` | catálogo | Falhas seguras para treinar diagnóstico (sempre reversíveis) |

Ver template em `templates/lab.md` (secção de evidência obrigatória quando testado).

## Como usar

Executar por ordem dentro de cada lab; o cleanup não é opcional (prova que sabe
desfazer). Falha intencional só em ambiente descartável, nunca no sistema real.

## Notas técnicas do eixo

- Falha intencional ≠ dano: cada lab declara o blast radius e o rollback antes.
- Labs que precisem de 2 máquinas/VMs declaram-no nos pré-requisitos (não se finge
  rede com uma só máquina).
