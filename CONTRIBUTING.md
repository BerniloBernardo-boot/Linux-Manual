# CONTRIBUTING

## Princípio

> Se remover este conteúdo o utilizador perde uma capacidade importante? Se não, não adicionar.
> Otimize para **competência adquirida**, não para quantidade.

## Antes de escrever — perguntas obrigatórias

1. Isso aumenta a capacidade de entender, administrar, diagnosticar ou construir sistemas Linux?
2. Ensina **causa** ou só dá solução pronta?
3. O comando funciona em quais distribuições? Testado contra a matriz?
4. Depende de `systemd`? Existe alternativa sem `systemd`?
5. Pode quebrar o sistema? Como desfazer? Existe modo mais seguro?
6. É duplicação? Deveria ser referência em vez de cópia?
7. Exemplo é seguro para copiar? Iniciante consegue seguir sem criar falha de segurança?
8. Como verificar que a solução funcionou?

Se qualquer resposta for "não sei", pare e pesquise na documentação oficial. Não invente.

## Loop de produção (obrigatório por tópico)

```text
RESEARCH → DEFINE → DESIGN → WRITE → VERIFY → TEST → CROSS-DISTRO CHECK → REVIEW → PUBLISH
```

- **RESEARCH:** consultar documentação oficial (man pages, Arch Wiki, docs Debian/Fedora/openSUSE/Alpine/Void/NixOS). Registrar em `Referências oficiais`.
- **DEFINE:** escopo exato do que será ensinado.
- **DESIGN:** estrutura + exemplos + exercícios + relações (`related:` nos metadados).
- **WRITE:** usar template correspondente em `templates/`.
- **VERIFY:** verificar cada comando, afirmação e caminho de ficheiro.
- **TEST:** executar exemplos quando possível; registrar ambiente (distro + versão).
- **CROSS-DISTRO CHECK:** preencher tabela Debian/Arch/Fedora/openSUSE/Alpine/Void/NixOS.
- **REVIEW:** erros, redundância, inconsistência, nomenclatura.
- **PUBLISH:** atualizar `ROADMAP.md` e índice do módulo.

## Estrutura de um tópico (17 perguntas)

Todo tópico relevante responde: o que é, por que existe, como funciona, onde fica, quando usar, quando NÃO usar, sintaxe, exemplos, saída esperada, erros comuns, diagnóstico, segurança, performance, diferenças entre distros, exercício, desafio, referências oficiais.

## Troubleshooting (formato obrigatório)

```text
Sintoma → Hipóteses → Coleta de evidências → Diagnóstico → Causa raiz → Correção → Validação → Prevenção
```

Nunca `problema → comando mágico → resolvido`.

## Laboratórios (formato obrigatório)

```text
Objetivo → Pré-requisitos → Ambiente → Execução → Verificação → Falha intencional → Diagnóstico → Correção → Cleanup → Desafio
```

Sempre com variantes por distribuição quando houver diferença.

## Diagramas

- Mermaid apenas; deve **explicar funcionamento**, não decorar.
- Todo bloco Mermaid deve renderizar (CI valida fence + sintaxe básica).

## Metadados e nomenclatura

- Ver `00-governanca/METADADOS.md` e `00-governanca/CONVENCOES.md`.
- Ficheiros: `kebab-case.md`. Pastas dos eixos: já fixas `01-...` a `33-...`.
- Português como idioma principal; comandos, saídas e nomes próprios em inglês original.

## Validação local

```bash
python3 scripts/validate.py
```

Deve passar sem erros antes de qualquer PR. O CI executa o mesmo script.

## Regra de parada

Pare e peça decisão quando encontrar: arquitetura ambígua, informação conflitante, comportamento dependente de versão, risco elevado de dano, documentação oficial contraditória ou escolha entre abordagens. Não assuma.
