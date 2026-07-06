# SilaDeneb Light Client -- Networking

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=2 -->

- [Networking](#networking)
  - [The gossip domain: gossipsub](#the-gossip-domain-gossipsub)
    - [Topics and messages](#topics-and-messages)
      - [Global topics](#global-topics)
        - [Modified `light_client_finality_update`](#modified-light_client_finality_update)
        - [Modified `light_client_optimistic_update`](#modified-light_client_optimistic_update)
  - [The Req/Resp domain](#the-reqresp-domain)
    - [Messages](#messages)
      - [GetLightClientBootstrap](#getlightclientbootstrap)
      - [LightClientUpdatesByRange](#lightclientupdatesbyrange)
      - [GetLightClientFinalityUpdate](#getlightclientfinalityupdate)
      - [GetLightClientOptimisticUpdate](#getlightclientoptimisticupdate)

<!-- mdformat-toc end -->

## Networking

The
[Capella light client networking specification](../../capella/light-client/p2p-interface.md)
is extended to exchange [SilaDeneb light client data](./sync-protocol.md).

### The gossip domain: gossipsub

#### Topics and messages

##### Global topics

###### Modified `light_client_finality_update`

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Message SSZ type                    |
| ------------------------------------------------------ | ----------------------------------- |
| `GENESIS_FORK_VERSION`                                 | n/a                                 |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientFinalityUpdate`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientFinalityUpdate` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientFinalityUpdate`   |

###### Modified `light_client_optimistic_update`

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Message SSZ type                      |
| ------------------------------------------------------ | ------------------------------------- |
| `GENESIS_FORK_VERSION`                                 | n/a                                   |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientOptimisticUpdate`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientOptimisticUpdate` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientOptimisticUpdate`   |

### The Req/Resp domain

#### Messages

##### GetLightClientBootstrap

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Response SSZ type              |
| ------------------------------------------------------ | ------------------------------ |
| `GENESIS_FORK_VERSION`                                 | n/a                            |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientBootstrap`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientBootstrap` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientBootstrap`   |

##### LightClientUpdatesByRange

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Response chunk SSZ type     |
| ------------------------------------------------------ | --------------------------- |
| `GENESIS_FORK_VERSION`                                 | n/a                         |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientUpdate`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientUpdate` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientUpdate`   |

##### GetLightClientFinalityUpdate

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Response SSZ type                   |
| ------------------------------------------------------ | ----------------------------------- |
| `GENESIS_FORK_VERSION`                                 | n/a                                 |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientFinalityUpdate`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientFinalityUpdate` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientFinalityUpdate`   |

##### GetLightClientOptimisticUpdate

<!-- sil_consensus_specs: skip -->

| `fork_version`                                         | Response SSZ type                     |
| ------------------------------------------------------ | ------------------------------------- |
| `GENESIS_FORK_VERSION`                                 | n/a                                   |
| `ALTAIR_FORK_VERSION` through `BELLATRIX_FORK_VERSION` | `altair.LightClientOptimisticUpdate`  |
| `CAPELLA_FORK_VERSION`                                 | `capella.LightClientOptimisticUpdate` |
| `SILA_DENEB_FORK_VERSION` and later                         | `sila_deneb.LightClientOptimisticUpdate`   |
