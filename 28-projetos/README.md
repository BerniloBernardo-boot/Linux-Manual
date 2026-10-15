# Projetos

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Transformar conhecimento em sistemas reais: projetos guiados (passo a passo com
verificação) e livres (briefing + critérios de aceitação), do laboratório ao serviço
em produção caseira — com desenho, implementação, hardening e documentação.

## Pré-requisitos

- Eixos 01–18 conforme o projeto; `29-labs` como treino prévio.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `guiados/servidor-caseiro.md` | projeto guiado | NAS+media+backup: desenho, implementação, hardening,-docs |
| `guiados/homelab-monitorizado.md` | projeto guiado | Métricas e logs com alertas (quando algo cai, saber porquê) |
| `livres/briefings.md` | projetos livres | 5+ briefings com critérios de aceitação verificáveis |

Cada projeto exige: desenho prévio, backup, hardening (`13-seguranca`), e
documentação do que foi feito (diagrama + procedimentos de recuperação).

## Como usar

`29-labs/` treina a técnica; aqui constrói-se o sistema. Revisão obrigatória antes de
expor à Internet (checklist de `13-seguranca` + `25-servidores`).

## Notas técnicas do eixo

- Projeto sem recuperação documentada é hobby, não sistema: cada guiado termina com
  "se este disco morrer, faço X".
- Âmbito fechado e testável: um projeto = um serviço bem feito, não dez a meio.
