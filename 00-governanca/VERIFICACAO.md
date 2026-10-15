# POLÍTICA DE VERIFICAÇÃO E PUBLICAÇÃO

> Aprovada na FASE 2B (2026-10-15). Vale para todos os tópicos presentes e futuros.
> Princípio: **testes automatizados ≠ validação técnica**. O CI (`scripts/validate.py`)
> prova estrutura; a verdade técnica prova-se com fontes + execução registada.

## 1. Estados de verificação (`verification:`)

Campo obrigatório nos metadados. Valores exatos:

| Estado | Significado | Quando usar |
|--------|-------------|-------------|
| `not-verified` | Ainda não verificado | Rascunho, conteúdo importado sem revisão |
| `documented` | Sustentado por documentação oficial, **sem** teste prático declarado | Afirmações verificadas em fontes primárias; nenhum output apresentado como observado |
| `partially-tested` | Parte dos exemplos foi executada e registada | Alguns outputs reais, resto documentado/não testado (cada exemplo rotulado) |
| `tested` | Todos os exemplos com output foram executados e registados | Exige `test_env:`, `test_date:` e secção `Evidência de teste` |

Regras:

1. **Nunca** usar `verified: true` como prova genérica de qualidade. O campo booleano
   `verified:` está **descontinuado** (ver `METADADOS.md`); o estado canónico é `verification:`.
2. Se `verified:` ainda estiver presente (legado), deve ser consistente:
   `verified: true` ⟺ `verification: tested`. Inconsistência falha no CI.
3. Não marcar compatibilidade com uma distribuição sem evidência suficiente:
   sem execução nessa distro, o máximo permitido é `documented` com a fonte citada,
   e a célula da tabela deve dizer "documentada, não executada aqui" (ou equivalente).
4. Proibir regressão: um documento `tested` que receba exemplos novos sem execução
   desce para `partially-tested` até os novos exemplos serem executados.

## 2. Registo de cada teste

Todo documento `partially-tested` ou `tested` deve conter:

- Metadados: `test_env:` (distro + versão + kernel + arquitetura, ex.:
  `"Omarchy 4.0.4 (base Arch, kernel 7.2.5-3-omarchy, x86_64)"`) e
  `test_date:` (`AAAA-MM-DD` da execução).
- No corpo, uma subsecção `### Evidência de teste` (dentro de `## 7. Exemplos`
  ou secção equivalente do template) com tabela:

| Comando / procedimento | Resultado esperado | Resultado observado | Estado |
|------------------------|--------------------|---------------------|--------|
| `getconf _POSIX_VERSION` | edição suportada | `200809` | executado 2026-10-15 |

- Condições de reprodução e limitações (ex.: "só testado com `/bin/sh -> bash`;
  `dash`/`ash` não executados") declaradas no corpo, não só nos metadados.

## 3. Cinco dimensões de validação (não confundir)

| Dimensão | O que prova | Como |
|----------|-------------|------|
| Estrutural | Metadados, links, Mermaid, nomenclatura | `scripts/validate.py` + CI (automático) |
| Factual | Afirmações sustentadas por fontes primárias | Revisão humana contra kernel.org, GNU, Open Group/POSIX, docs das distros |
| Prática | Exemplos executam e outputs são reais | Execução em ambiente registado (§2); nunca inventar outputs |
| Cross-distro | Diferenças Debian/Arch/Fedora/openSUSE/Alpine/Void/NixOS corretas | Tabela por tópico; sem execução, só `documented` + fonte |
| Segurança | Nada inseguro/destrutivo sem aviso | `risk:` + bloco `> ⚠️` com reversão e alternativa (§4) |

## 4. Regras para comandos, privilégios e rollback

1. Comandos destrutivos (`rm -rf`, `dd`, `mkfs`, fork-bomb, `chmod -R 777 /`, escrita em
   `/dev/`, `parted/mkfs` em disco) ou `risk: alto/destrutivo`: obrigatório bloco
   `> ⚠️ Alerta` com (a) o que pode quebrar, (b) como desfazer / rollback,
   (c) alternativa mais segura, (d) pré-condições (backup, ambiente descartável, não-produção).
2. Nunca instruir operação como root quando `sudo`/utilizador normal basta.
   Quando root for necessário, dizê-lo explicitamente e justificar.
3. Exemplos de inspeção primeiro: diagnóstico sempre começa por comandos somente-leitura.
4. Exemplos **não testados** devem ser rotulados (`não testado`, `teórico`, `a confirmar`)
   e **não** podem apresentar bloco de "saída esperada" como se observado.
   Saída observada só com execução registada (§2).

## 5. Regras para referências oficiais

1. Preferir fontes primárias: kernel.org, docs.kernel.org, GNU, Open Group/POSIX
   (pubs.opengroup.org), manuais e docs oficiais das distros.
2. URLs integralmente escritos; **não inventar URLs**. Cada URL das Referências deve
   ter sido aberto na data de publicação/revisão (`last_reviewed:`).
3. Distinguir norma (POSIX/SUS), convenção (filosofia Unix, FHS) e implementação
   (cada distro). Suporte declarado (`getconf`) ≠ conformidade integral/certificação.
4. Informação sensível: não publicar segredos, tokens, chaves, dados pessoais reais
   nem nomes de hosts/clientes. Hostnames locais de teste são aceitáveis.

## 6. Critérios de publicação (todos obrigatórios)

- [ ] `python3 scripts/validate.py` verde (0 erros).
- [ ] `verification:` reflete o estado real; `tested`/`partially-tested` têm
      `test_env:`, `test_date:` e `Evidência de teste`.
- [ ] Cada afirmação técnica relevante: fonte primária citada **ou** execução registada.
- [ ] Nenhuma compatibilidade com distro afirmada sem evidência (§1.3).
- [ ] Comandos destrutivos/privilegiados conformes §4.
- [ ] Sem links internos quebrados; Mermaid válido e funcional (não decorativo).
- [ ] `ROADMAP.md`, README do módulo e `INDICE.md` atualizados pelo estado real;
      nunca `complete` só por existir ficheiro.

## 7. Critérios de bloqueio (qualquer um bloqueia a publicação)

1. Validador com erros.
2. Erro técnico crítico/alto sem correção (perda de dados, segurança, conceito errado).
3. Output apresentado como observado sem execução registada.
4. Compatibilidade com distro afirmada sem evidência.
5. Comando destrutivo sem alerta + reversão + alternativa.
6. URL inventado ou não aberto / referência que não sustenta a afirmação.
7. Exemplos copiados sem compreensão do efeito (causa/consequência/mecanismo ausentes).

## 8. Integração com o CI

O CI (`.github/workflows/validate.yml`) executa `scripts/validate.py`, que verifica:
metadados (campos obrigatórios, `verification:` válido, `test_env:`/`test_date:`
quando exigidos, consistência do legado `verified:`), links internos, Mermaid,
fences, kebab-case e títulos duplicados. A revisão factual, prática, cross-distro
e de segurança continua humana — o CI não a substitui.
