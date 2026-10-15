# Networking

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar rede no Linux: endereços IP e rotas, DNS, ferramentas (`ip`, `ss`, `ping`,
`curl`, `resolvectl`), NetworkManager vs. systemd-networkd, e diagnóstico por camadas
(física → IP → DNS → aplicação) em vez de "reiniciar a rede".

## Pré-requisitos

- `03-comandos` e `06-processos` (serviços de rede são processos).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/ip-rotas-e-dns.md` | learn | CIDR, gateway, tabelas de rota, resolução de nomes |
| `learn/networkmanager-e-systemd-networkd.md` | learn | Os dois gestores, `nmcli` vs. ficheiros `.network`, netplan (Ubuntu) |
| `reference/ip-ss-ping-curl.md` | reference | Tabelas: `ip`, `ss`, `ping`, `curl`, `resolvectl`, `nmcli` |
| `troubleshooting/sem-rede-ou-dns-falha.md` | troubleshooting | Sem IP? sem rota? sem DNS? sem Internet? — isolar a camada |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Continua em `13-seguranca`
(firewall, SSH) e `25-servidores` (serviços expostos).

## Notas técnicas do eixo

- `ip` (iproute2) substitui `ifconfig`/`route`/`netstat` legados — os tópicos ensinam
  `ip` e `ss`, mencionando os legados só para leitura de tutoriais antigos.
- Ubuntu Server usa netplan (YAML que gera config); Fedora usa NetworkManager;
  Alpine usa `/etc/network/interfaces` — nunca assumir um só.
- `systemd-resolved` com stub `127.0.0.53` confunde diagnósticos de DNS; o
  troubleshooting ensina a distinguir stub, servidor real e VPN.
