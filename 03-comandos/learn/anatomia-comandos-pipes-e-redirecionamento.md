---
title: "Anatomia de comandos, pipes e redirecionamento"
category: learn
level: basico
prerequisites:
  - "02-terminal/learn/o-terminal-pty-e-o-shell"
distributions:
  - universal
requires:
  - "terminal, PTY e shell"
related:
  - "03-comandos/reference/comandos-e-redirecionamento"
  - "03-comandos/troubleshooting/comando-falhou-ou-saiu-vazio"
  - "07-shell/learn/bash-e-posix-sh"
commands:
  - type
  - man
  - ls
  - echo
  - printf
  - sort
  - head
  - wc
  - cat
risk: baixo
verification: tested
test_env: "Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64), bash 5.3.15"
test_date: "2026-10-15"
last_reviewed: "2026-10-15"
---

# Anatomia de comandos, pipes e redirecionamento

## 1. O que é?

Todo comando segue a mesma anatomia:

```text
comando  [-opções]  [--opções-longas]  [operandos]
ls       -l         --human-readable   /etc
```

- **Opções** (flags) modificam o comportamento (`-l`, `--help`).
- **Operandos** são os alvos (ficheiros, texto, números).
- O shell separa tudo por espaços **antes** de executar — por isso `meu ficheiro`
  sem aspas vira dois operandos (ver §8).

E todo comando fala por **3 canais**: `stdin` (0, entrada), `stdout` (1, saída normal),
`stderr` (2, erros). **Redirecionar** é trocar esses canais de/para ficheiros;
**pipe** (`|`) é ligar o `stdout` de um ao `stdin` do outro. A norma POSIX define a
linguagem (cap. 2, Shell Command Language — ver Referências).

## 2. Por que existe?

Separar canais e compor programas é a filosofia Unix em ação (tópico 2): em vez de um
programa gigante "listar-ordenar-filtrar-guardar", encadeiam-se peças —
`ls | sort | head > lista.txt` — cada uma fazendo uma coisa bem. O código de saída
(`$?`: 0 = sucesso) permite ao shell e a scripts decidir o passo seguinte.

## 3. Como funciona?

```mermaid
flowchart LR
    subgraph CMD["comando"]
        direction TB
        I["stdin (0)"]
        O["stdout (1)"]
        E["stderr (2)"]
    end
    F["ficheiro / terminal"] -->|"< redireciona"| I
    O -->|"> / >> redireciona"| F
    E -->|"2> redireciona"| F2["ficheiro de erros"]
    O -->|"| I2["stdin do próximo"]
```

Ordem do shell (POSIX §2.1): lê → parte em tokens → expansões → **aplica
redirecionamentos** → executa (função, embutido ou programa) → recolhe o estado de
saída. Redirecionar com `>` **trunca primeiro**: `comando > ficheiro` esvazia o
ficheiro mesmo que o comando falhe depois.

Três naturezas de comando (`type` revela):

| Natureza | Exemplo aqui | Onde vive |
|----------|--------------|-----------|
| Programa externo | `ls` → `/usr/bin/ls` | Disco, via `PATH` |
| Embutido do shell | `echo`, `cd`, `test`, `printf` | Dentro do `bash` (mais rápido, sem `fork`) |
| Função/alias | definidos pelo utilizador | Sessão atual |

## 4. Onde fica no sistema?

| Pergunta | Resposta |
|----------|----------|
| Que tipo é? | `type <nome>` (ex.: `ls is /usr/bin/ls`, `echo is a shell builtin`) |
| Ajuda rápida? | `<comando> --help` (ex.: `ls --help` → `Usage: ls [OPTION]...`) |
| Manual? | `man <comando>` (aqui: `man1/ls.1.gz`, `man1/printf.1.gz`); `man 1p` = POSIX (nem sempre instalado) |
| Info GNU? | `info <comando>` (aqui: `info (GNU texinfo) 7.3`) |
| Código de saída do último? | `echo $?` |

## 5. Quando usar? / Quando NÃO usar?

- **Use pipes** para transformar texto em cadeia; **`>` para criar**, **`>>` para
  acrescentar**, **`2>` para capturar erros** separadamente; **`<<<'texto'`**
  (here-string) para alimentar stdin sem ficheiro.
- **NÃO use** `>` quando quer preservar (use `>>` ou `set -o noclobber`);
  **NÃO confie** em `$?` de um pipe sem `pipefail` — por omissão é só o estado do
  **último** comando (ver Exemplos: `false | true` dá 0!).

## 6. Sintaxe

```bash
comando > ficheiro        # stdout para ficheiro (TRUNCA)
comando >> ficheiro       # stdout acrescenta
comando 2> erros.txt      # stderr para ficheiro
comando > tudo.txt 2>&1   # stdout+stderr juntos
comando < entrada.txt     # stdin vindo de ficheiro
cat <<< 'texto'           # here-string: texto como stdin
a | b | c                 # stdout de cada um → stdin do seguinte
echo $?                   # estado do último comando/pipe
```

Todos somente leitura/gestão própria; o único risco é `>` truncar (ver §10).

## 7. Exemplos

Exemplo 1 — natureza dos comandos e ajuda:

```bash
type ls echo cd test printf
ls --help | head -n 3
```

Saída esperada (exemplo real, executado em 2026-10-15 — Omarchy/Arch x86_64):

```text
ls is /usr/bin/ls
echo is a shell builtin
cd is a shell builtin
test is a shell builtin
printf is a shell builtin
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.
```

Leitura: `ls` é programa externo; os restantes vivem dentro do shell. `--help` é a
primeira ajuda (rápida); `man` é a completa.

Exemplo 2 — redirecionamento e os dois canais:

```bash
echo ola > t.txt && cat t.txt
echo mundo >> t.txt && cat t.txt
ls /naoexiste > out.txt 2> err.txt; echo "rc=$?"
cat err.txt
```

Saída esperada (mesmo ambiente, real, em `/tmp/opencode/cmd`):

```text
ola
ola
mundo
rc=2
ls: cannot access '/naoexiste': No such file or directory
```

Leitura: `>` criou, `>>` acrescentou; o erro foi para `err.txt` (não para o terminal)
e o estado é `2` (falha) — `out.txt` ficou vazio. Prova de que stdout e stderr são
canais independentes.

Exemplo 3 — pipes e composição:

```bash
printf 'b\na\nc\n' | sort | head -n 2
ls /usr/bin | wc -l
```

Saída esperada (mesmo ambiente, real):

```text
a
b
3577
```

Leitura: `printf → sort → head` transforma o fluxo sem ficheiros temporários;
`/usr/bin` tem 3577 entradas aqui. Pipes movem texto, não ficheiros.

Exemplo 4 — o estado que mente (e a correção):

```bash
cat <<< 'via-stdin'
false | true; echo "pipe=$?"
set -o pipefail; false | true; echo "pipe=$?"
```

Saída esperada (mesmo ambiente, real, bash 5.3):

```text
via-stdin
pipe=0
pipe=1
```

Leitura: here-string alimenta stdin sem ficheiro. `false | true` devolve **0**
(sucesso!) porque `$?` é só o último; com `set -o pipefail` devolve **1**. Nota:
`pipefail` e `PIPESTATUS` são extensão bash — **não POSIX** (script portátil: teste
cada etapa ou evite pipes com falhas silenciosas; ver tópico 2).

### Evidência de teste

Ambiente: Omarchy 4.0.4 (base Arch, x86_64), bash 5.3.15, 2026-10-15. Todos os
exemplos com output foram executados em `/tmp/opencode/cmd` (descartável); nenhum
output foi inventado.

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `type ls echo cd test printf` | naturezas | externo; 4 builtins | executado |
| `ls --help`, `man -w`, `info --version` | ajuda disponível | `Usage:…`, `man1/*.1.gz`, texinfo 7.3 | executado |
| `>` / `>>` / `2>` + `$?` | truncar/acrescentar/separar | `ola` → `ola+mundo`; `rc=2`, erro em `err.txt` | executado |
| `printf \| sort \| head`; `ls \| wc -l` | composição | `a b`; `3577` | executado |
| here-string; `false\|true` ± pipefail | `via-stdin`; `0` vs `1` | idêntico | executado |
| `man 1p`, `dash`, BusyBox | — | — | **não executados** |

Limitações: `t.txt/out.txt/err.txt` criados em dir temporário e descartáveis;
comportamento POSIX-estrito (`dash`) não testado.

## 8. Erros comuns

| Erro | Causa | Correção |
|------|-------|----------|
| `comando > importante.txt` esvaziou o ficheiro | `>` trunca **antes** de executar | `>>` para acrescentar; `set -o noclobber` como rede |
| "O comando não mostrou erro nenhum" | Erro foi para o terminal misturado, ou stdout foi filtrado | Separar: `2> erros.txt`; ler os dois canais |
| `false \| true` passa num `if` | `$?` é só o último do pipe | `set -o pipefail` (bash) ou testar etapas |
| `cat ficheiro com espaços` falha | Shell parte por espaços | Aspas: `cat "meu ficheiro"` |
| `which` diz uma coisa, `type` outra | `which` é externo e ignora builtins/aliases | Preferir `type` / `command -v` |

## 9. Diagnóstico

Comando falhou ou saiu vazio? Pergunta-guia: **qual canal, qual etapa, qual estado?**

```bash
type <comando>              # existe? builtin ou externo?
<comando> > out.txt 2> err.txt; echo "rc=$?"  # separar canais + estado
printf ... | etapa1 | etapa2  # testar cada etapa isolada
set -o pipefail             # (bash) estado honesto do pipe
```

- `command not found` → `PATH` ou pacote ausente (ver `08-pacotes`).
- Saída vazia + `rc=0` → escreveu no outro canal ou o filtro removeu tudo.
- Pipe "ok" mas resultado errado → falha silenciosa no meio (pipefail a confirma).

## 10. Segurança

`risk: baixo`, com uma ressalva real: **`>` destrói conteúdo** — nunca redirecione
para ficheiros que não pode perder (`> /etc/passwd` seria catastrófico; nem teste).
Regras: confirmar o alvo com `ls` antes, preferir `>>`, usar `noclobber` em sessões
interativas arriscadas, e diagnósticos sempre separando `2>` (erros não se escondem).

## 11. Performance

Pipes evitam ficheiros temporários (menos I/O em disco); cada etapa é um processo
(`fork+exec` nos externos, zero nos builtins — outra razão para `printf` embutido
em vez de `echo` externo em loops). Milhares de `cat file | grep x` pagam um processo
a mais por iteração — detalhe em `18-performance`.

## 12. Diferenças entre distribuições

Anatomia e operadores são **universais** (POSIX + bash em todo o lado). Divergências:

| Família | Notas | Evidência |
|---------|-------|-----------|
| Arch (base deste teste) | coreutils GNU completos; `man-db` + `texinfo`; 3577 entradas em `/usr/bin` | **executada aqui** |
| Debian/Ubuntu | `man` por omissão; `info` nem sempre instalado | documentada, não executada aqui |
| Alpine/BusyBox | `ls`/`sort` com menos flags; sem `info`; `man` opcional | documentada, não executada aqui |
| Todas | `command -v`, `>`, `>>`, `2>`, `\|`, `$?` funcionam em qualquer `sh` POSIX | norma (tópico 2) |

Detalhe por família em `33-distributions`.

## 13. Exercício

1. Execute `type` em 5 comandos à sua escolha e separe builtins de externos.
2. Reproduza o Exemplo 2 num diretório temporário e explique cada ficheiro resultante.
3. Execute `false | true; echo $?` e depois com `set -o pipefail`. Explique a diferença.

## 14. Desafio

Sem instalar nada: um script faz `grep ERRO app.log | head -n 5 > resumo.txt` e o
`resumo.txt` sai vazio com `rc=0`, embora `app.log` contenha "ERRO". Liste 3 causas
possíveis em canais/etapas diferentes e o comando que distingue cada uma. (Resposta
esperada: "ERRO" está no stderr da app que gerou o log? `grep` case-sensitive vs.
"erro"? `head` fechou o pipe — testar `grep -c`, `grep -i`, separar `2>`.)

## 15. Referências oficiais

- POSIX.1-2024, Shell Command Language (tokens, redirecionamento §2.7, estado §2.8) — https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html
- `man 1 bash` (secção REDIRECTION) + `man 1 ls` — ajuda local.
