# MATRIZ DE DISTRIBUIÇÕES

> Nunca escrever "execute este comando" sem especificar família. Conceito universal uma vez; diferenças em tabela.

## Famílias cobertas

| Família | Distros | Package manager | Init padrão | Observação |
|---------|---------|-----------------|-------------|------------|
| Debian | Debian, Ubuntu, Mint, Pop!_OS, Ubuntu Server | `apt` / `apt-get` | systemd | stable; `sudo` por padrão no Ubuntu |
| Arch | Arch, Manjaro, EndeavourOS, CachyOS | `pacman` (+ AUR) | systemd | rolling release |
| Fedora/RHEL | Fedora, RHEL, Rocky, AlmaLinux | `dnf` (`yum` legado) | systemd | SELinux enforcing por padrão |
| openSUSE | Tumbleweed, Leap | `zypper` (+ YaST) | systemd | Tumbleweed rolling, Leap stable |
| Alpine | Alpine | `apk` | OpenRC | musl + BusyBox; container mínimo |
| Void | Void Linux | `xbps` (`xbps-install`) | runit | sem systemd por padrão |
| NixOS | NixOS | `nix` / `nixos-rebuild` | systemd | configuração declarativa `/etc/nixos/` |
| Kali | Kali Linux | `apt` | systemd | foco pentest; não usar como desktop diário |

## Template de tabela por tópico

```markdown
| Família | Comando/Ferramenta | Observação |
|---------|--------------------|------------|
| Debian/Ubuntu | `apt install htop` | ... |
| Arch | `pacman -S htop` | ... |
| Fedora/RHEL | `dnf install htop` | ... |
| openSUSE | `zypper install htop` | ... |
| Alpine | `apk add htop` | ... |
| Void | `xbps-install -S htop` | ... |
| NixOS | `nix-env -iA nixpkgs.htop` | modelo diferente, declarativo |
```

## Dimensões que sempre verificar

package manager · init system · filesystem padrão · localização de configs ·
ferramentas admin · firewall (`ufw` vs `firewalld` vs `nftables` vs `iptables`) ·
networking (`NetworkManager` vs `systemd-networkd` vs `/etc/network/interfaces`) ·
bootloader · serviços · política de atualização · rolling vs stable · modelo de configuração.

## Exemplos de armadilhas

- `apt` não existe no Arch; `pacman -Syu` não existe no Debian.
- `systemctl` não funciona em Void/OpenRC nem em containers sem systemd — documentar alternativa (`service`, `rc-service`, `runit`).
- Caminhos: `netplan` (Ubuntu Server) vs `/etc/NetworkManager/` vs `/etc/systemd/network/`.
- Firewall: Ubuntu `ufw` (frontend), Fedora `firewalld`, Alpine/OpenWrt `nftables` direto.
