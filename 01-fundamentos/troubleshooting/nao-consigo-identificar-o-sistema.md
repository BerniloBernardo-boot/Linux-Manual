---
title: "Sintoma: não consigo identificar o sistema"
category: troubleshooting
level: basico
prerequisites:
  - "01-fundamentos/learn/o-que-e-linux-kernel-vs-distribuicao"
distributions:
  - universal
requires:
  - "kernel vs. distribuição"
related:
  - "01-fundamentos/reference/inspecao-do-sistema"
commands:
  - uname
  - cat
  - getconf
  - command
  - ls
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64)"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Sintoma: não consigo identificar o sistema

## Sintoma

Sinais típicos: `cat /etc/os-release` devolve erro ou conteúdo inesperado; `lsb_release`
não existe; `uname -a` e `/etc/os-release` parecem "discordar" (ex.: kernel de uma
distro, userland de outra); tutoriais pedem a distro e nenhuma fonte confirma.

## Hipóteses (ordenadas por probabilidade)

1. Estou num **contentor**: kernel do host + userland da imagem (discordância normal).
2. Sistema **mínimo** (Alpine, netinstall, rescue): ficheiros/ferramentas auxiliares ausentes.
3. `/etc/os-release` apagado ou corrompido (raro; edição manual ou falha de atualização).
4. Estou a ler o campo errado (`PRETTY_NAME` genérico, `ID_LIKE` confundido com `ID`).

## Coleta de evidências

```bash
uname -srmo              # kernel: nunca mente sobre o kernel em execução
cat /etc/os-release      # distro do userland (pode faltar)
ls /etc/*-release /etc/*_version 2>/dev/null  # ficheiros alternativos
command -v lsb_release && lsb_release -a  # auxiliar, quando existe (somente leitura)
getconf _POSIX_VERSION   # edição POSIX declarada
```

Todos somente leitura e seguros.

## Diagnóstico (como distinguir hipóteses)

| Hipótese | Evidência que confirma | Evidência que descarta |
|----------|------------------------|------------------------|
| Contentor | `uname -r` = kernel do host, mas `/etc/os-release` = outra distro | `systemd-detect-virt` vazio + `/` montado do disco local |
| Sistema mínimo | `ID=alpine` (ou similar) + `which`/`man` ausentes | `command -v` e `cat` funcionam (são o essencial) |
| `os-release` apagado | `ls /etc/*-release` vazio + erros em ferramentas | Ficheiro existe com `ID=` legível |
| Campo errado | `ID_LIKE=arch` lido como "é Arch puro" | `ID=` é a identidade; `ID_LIKE` é só a família |

Cadeia de recurso (por ordem): `/etc/os-release` → `/etc/*-release` → `hostnamectl` →
`uname` + gestor de pacotes detetável (`command -v pacman apt dnf`) → `getconf`.

## Causa raiz

Na maioria dos casos não há avaria: **kernel e userland têm origens diferentes**
(contentor) ou o sistema é mínimo por desenho. A "discordância" é informação, não erro.
Avaria real só quando `/etc/os-release` foi alterado/apagado.

## Correção

- Caso contentor/mínimo/campo errado: **nenhuma alteração** — registar kernel
  (`uname -r`) e distro (`ID=`/`ID_LIKE=`) separadamente e seguir o procedimento da
  família correta ([inspecao-do-sistema.md](../reference/inspecao-do-sistema.md)).
- Caso `/etc/os-release` apagado: reinstalar o pacote que o fornece pelo gestor da
  distro (ex.: pacote `filesystem` em Arch, `base-files` em Debian — **documentado,
  não executado aqui**; detalhe em `08-pacotes`/`33-distributions`). Não reconstruir
  o ficheiro à mão: um `ID=` errado desorienta ferramentas.

## Validação (como confirmar que resolveu)

```bash
cat /etc/os-release && uname -srmo   # ambos respondem e fazem sentido juntos
```

Resolvido quando cada pergunta tem fonte: kernel ← `uname`, distro ← `os-release`
(ou alternativa), edição POSIX ← `getconf`. Se ainda discordarem, voltar às hipóteses:
é contentor?

## Prevenção

- Nunca editar `/etc/os-release` à mão.
- Em scripts, testar `[ -f /etc/os-release ]` antes de ler; ter fallback para
  `/etc/*-release` e `uname`.
- Documentar nos próprios procedimentos: "kernel X (host), userland Y (contentor)".

## Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), 2026-10-15.
Cadeia de recurso executada; cenário "ficheiro apagado" **não** reproduzido
(exigiria destruir `/etc/os-release` — proibido pela política §5: sem comandos
destrutivos para obter evidências).

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `uname -srmo` | kernel | `Linux 7.2.5-3-omarchy x86_64 GNU/Linux` | executado |
| `cat /etc/os-release` | `ID`/`ID_LIKE` | `ID=omarchy`, `ID_LIKE=arch` | executado |
| `ls /etc/*-release` | ficheiros presentes | `/etc/arch-release`, `/etc/lsb-release`, `/etc/os-release` (este ambiente) | executado |
| `command -v lsb_release && lsb_release -a` | auxiliar | existe; `Distributor ID: Arch`, `Release: rolling` | executado |
| Reinstalação do pacote base | — | — | **não executada** (documentada) |

Limitações: contentores reais (Docker) e sistemas mínimos não testados aqui; hipóteses
1–2 marcadas como documentadas.

## Referências oficiais

- Referência consolidada do eixo: [inspecao-do-sistema.md](../reference/inspecao-do-sistema.md)
- kernel.org — "About Linux Kernel" — https://www.kernel.org/linux.html
