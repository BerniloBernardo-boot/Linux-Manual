# Virtualização

> Estado: `planned` (ver `ROADMAP.md`).

## Objetivo

Ensinar VMs no Linux: KVM/QEMU, libvirt/`virt-manager`, quando VM vs. contentor,
snapshots, e virtualização aninhada — com a regra de alocar menos do que o host tem.

## Pré-requisitos

- `23-containers` (contraste), `11-storage` (imagens) e `12-networking` (redes virtuais).

## Documentos planeados

| Documento | Tipo | Escopo |
|-----------|------|--------|
| `learn/kvm-qemu-e-libvirt.md` | learn | Hypervisor, `libvirtd`, redes NAT/bridge, primeira VM |
| `reference/gerir-vms.md` | reference | `virsh`, snapshots, `virt-manager`, `qemu-img`, cloud-init intro |
| `troubleshooting/vm-nao-arranca.md` | troubleshooting | KVM desativado no BIOS, rede, disco, permissões do utilizador no libvirt |

## Como usar

Ordem: `learn/` → `reference/` → `troubleshooting/`. Praticar com VM descartável;
snapshot antes de qualquer experiência arriscada dentro da VM.

## Notas técnicas do eixo

- `egrep -c '(vmx|svm)' /proc/cpuinfo` diz se a CPU tem virtualização; sem isso
  (ou desativado no firmware), KVM não acelera.
- Utilizador precisa do grupo `libvirt` (ou `kvm`) — sem ele, `virsh` falha com
  permissão, não com erro de virtualização.
- VM com mais vCPU/RAM que o host degrada tudo (overcommit consciente, nunca por omissão).
