# Troubleshooting

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ser a enciclopédia transversal de diagnóstico: do sintoma à causa raiz em qualquer
eixo, com o método único do projeto (sintoma → hipóteses → evidências → diagnóstico →
causa → correção → validação → prevenção) e um índice por sintoma que aponta para os
diagnósticos locais de cada eixo — sem duplicar conteúdo.

## Pré-requisitos

- Método aplicável após `01–03`; poder total após os eixos 04–18.

## Documentos planeados

| Documento | Tipo | Âmbito |
|-----------|------|--------|
| `sintomas/sistema-nao-arranca.md` | sintoma | Aponta `10-boot` + `11-storage` |
| `sintomas/sem-rede.md` | sintoma | Aponta `12-networking` + `13-seguranca` |
| `sintomas/disco-cheio.md` | sintoma | Aponta `11-storage` + `04-filesystem` |
| `diagnosticos/primeiros-5-minutos.md` | diagnóstico | Checklist universal: `uptime`, `df`, `free`, `ss`, `journalctl` |
| `solucoes/recuperacao-com-live-usb.md` | solução | `chroot`, remontar, reinstalar bootloader |

Os documentos referencia os eixos (`../10-boot/...`) em vez de copiar procedimentos.

## Como usar

Entrada pelo sintoma (`sintomas/`), método em `diagnosticos/`, reparo em `solucoes/`.
Cada entrada nova exige: sintomas observáveis exatos, ≥2 hipóteses, comandos de
evidência somente leitura primeiro, e validação que prove a resolução.

## Notas técnicas do eixo

- Nunca "comando mágico sem diagnóstico": a correção vem depois da causa provada.
- Correções destrutivas (reinstalar bootloader, `fsck` em montado) exigem live USB,
  backup e o bloco de alerta completo.
- Este eixo não substitui os `troubleshooting/` locais — agrega e encaminha.
