# Permissões

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar quem pode ler, escrever e executar cada ficheiro: notação octal e simbólica,
donos e grupos, `umask`, ACLs, atributos estendidos — e como `sudo` delega privilégio
sem partilhar a palavra-passe de root.

## Pré-requisitos

- `01-fundamentos` e `04-filesystem` (hierarquia, inodes).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/permissoes-octais-e-simbolicas.md` | learn | `rwx`, `chmod 755` vs. `u+x`, donos e grupos |
| `learn/umask-acl-e-sudo.md` | learn | `umask`, `setfacl`/`getfacl`, `sudo` e `sudoers` |
| `reference/chmod-chown.md` | reference | Tabelas de modos, opções recursivas, armadilhas |
| `troubleshooting/permissao-negada.md` | troubleshooting | `Permission denied`: dono, modo, ACL, contexto MAC |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Eixos ligados: `04-filesystem`
(onde se aplica), `13-seguranca` (SELinux/AppArmor, SSH) e `25-servidores`
(permissões de conteúdo web).

## Notas técnicas do eixo

- `chmod -R 777 /` destrói a segurança do sistema e é praticamente irreversível —
  os tópicos ensinam o modo mínimo necessário, nunca o máximo cómodo.
- `umask` típica `022` (ficheiros `644`); `027` em ambientes partilhados.
- Em Fedora/RHEL, `Permission denied` com modo correto sugere contexto SELinux
  (`ls -Z`); em Debian/Ubuntu, sugere grupo/`sudo` — o troubleshooting distingue.
