# Desenvolvimento

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar a toolchain de compilação no Linux: GCC/Clang, `make`, headers e `*-dev`,
`pkg-config`, depuração com `gdb`/`strace`/`ltrace` — e a diferença entre "falta o
programa" e "falta o ambiente de compilação".

## Pré-requisitos

- `03-comandos`, `07-shell` e `08-pacotes`.

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/toolchain-gcc-make.md` | learn | Compilar C: pré-processar, compilar, ligar; `Makefile` mínimo |
| `reference/compilar-e-depurar.md` | reference | Tabelas: `gcc`/`clang`, `make`, `gdb`, `strace`, `pkg-config`, pacotes `-dev` |
| `troubleshooting/falta-header-ou-biblioteca.md` | troubleshooting | `fatal error: foo.h`, `cannot find -lfoo`: que pacote traz o ficheiro |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Compilar como utilizador normal
em diretório próprio; `sudo make install` é proibido nos exemplos (usar prefixo local
ou pacote da distro).

## Notas técnicas do eixo

- Erro de header em falta resolve-se no gestor (`base-devel` no Arch, `build-essential`
  no Debian, `Development Tools` no Fedora) — nunca copiando `.h` avulso.
- `strace -e trace=file` revela ficheiros que um build/prog tenta abrir; `gdb` com
  símbolos (`-g`) em vez de adivinhar.
- Código da Internet compila-se depois de ler o `README`/licença, nunca por pipe
  (`curl … | sh` é proibido como exemplo).
