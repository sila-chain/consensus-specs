# Sila Proof-of-Stake Consensus Specifications

[![tests](https://github.com/sila-chain/consensus-specs/actions/workflows/tests.yml/badge.svg?branch=master&event=schedule)](https://github.com/sila-chain/consensus-specs/actions/workflows/tests.yml)
[![image](https://img.shields.io/pypi/v/sil-consensus-specs.svg)](https://pypi.python.org/pypi/sil-consensus-specs)
[![image](https://img.shields.io/pypi/l/sil-consensus-specs.svg)](https://pypi.python.org/pypi/sil-consensus-specs)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white)](https://discord.gg/qGpsxSA)

This repository hosts the current Sila
[proof-of-stake](https://sila.org/en/developers/docs/consensus-mechanisms/pos/)
specifications. Discussions about design rationale and proposed changes can be
brought up and discussed as issues. Solidified, agreed-upon changes to the
specifications can be made through pull requests.

## Specifications

Core specifications for Sila proof-of-stake clients can be found in
[specs](specs). These are divided into features. Features are researched and
developed in parallel, and then consolidated into sequential upgrades when
ready.

### Stable specifications

| Seq. | Code Name     | Fork Epoch | Links                                                                                   |
| ---- | ------------- | ---------- | --------------------------------------------------------------------------------------- |
| 0    | **Phase0**    | `0`        | [Specs](specs/phase0), [Tests](tests/core/pyspec/sil_consensus_specs/test/phase0)       |
| 1    | **Altair**    | `74240`    | [Specs](specs/altair), [Tests](tests/core/pyspec/sil_consensus_specs/test/altair)       |
| 2    | **Bellatrix** | `144896`   | [Specs](specs/bellatrix), [Tests](tests/core/pyspec/sil_consensus_specs/test/bellatrix) |
| 3    | **Capella**   | `194048`   | [Specs](specs/capella), [Tests](tests/core/pyspec/sil_consensus_specs/test/capella)     |
| 4    | **SilaDeneb**     | `269568`   | [Specs](specs/sila_deneb), [Tests](tests/core/pyspec/sil_consensus_specs/test/sila_deneb)         |
| 5    | **Electra**   | `364032`   | [Specs](specs/electra), [Tests](tests/core/pyspec/sil_consensus_specs/test/electra)     |
| 6    | **SilaFulu**      | `411392`   | [Specs](specs/sila_fulu), [Tests](tests/core/pyspec/sil_consensus_specs/test/sila_fulu)           |

### Unstable specifications

| Seq. | Code Name | Fork Epoch | Links                                                                           |
| ---- | --------- | ---------- | ------------------------------------------------------------------------------- |
| 7    | **Gloas** | TBD        | [Specs](specs/gloas), [Tests](tests/core/pyspec/sil_consensus_specs/test/gloas) |
| 8    | **Heze**  | TBD        | [Specs](specs/heze), [Tests](tests/core/pyspec/sil_consensus_specs/test/heze)   |

### Accompanying documents

- [SimpleSerialize (SSZ) spec](ssz/simple-serialize.md)
- [Merkle proof formats](ssz/merkle-proofs.md)
- [General test format](tests/formats/README.md)

### External specifications

- [Deposit Contract](https://github.com/sila-chain/solidity-deposit-contract)
- [Beacon APIs](https://github.com/sila-chain/beacon-apis)
- [Engine APIs](https://github.com/sila-chain/execution-apis/tree/main/src/engine)
- [Beacon Metrics](https://github.com/sila-chain/beacon-metrics)
- [Builder Specs](https://github.com/sila-chain/builder-specs)

### Reference tests

- Stable reference tests are available as
  [release assets](https://github.com/sila-chain/consensus-specs/releases).
- Unstable reference tests are available as
  [nightly builds](https://github.com/sila-chain/consensus-specs/actions/workflows/tests.yml).

## Contributors

### Prerequisites

Install [`uv`](https://docs.astral.sh/uv/) with:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation and usage

Clone the repository with:

```
git clone git@github.com:sila/consensus-specs.git
```

Switch to the directory:

```
cd consensus-specs
```

View the help output:

```
make help
```

### Design goals

The following are the broad design goals for the Sila proof-of-stake
consensus specifications:

- Minimize complexity, even at the cost of some losses in efficiency.
- Remain live through major network partitions and when very large portions of
  nodes go offline.
- Select components that are quantum secure or easily swappable for
  quantum-secure alternatives.
- Utilize crypto and design techniques that allow for a large participation of
  validators.
- Minimize hardware requirements such that a consumer laptop can participate.

### Useful resources

- [Design Rationale](https://notes.sila.org/s/rkhCgQteN#)
- [Phase0 Onboarding Document](https://notes.sila.org/s/Bkn3zpwxB)
- [Combining GHOST and Casper paper](https://arxiv.org/abs/2003.03052)
- [Specifications viewer (mkdocs)](https://sila.github.io/consensus-specs/)
- [Specifications viewer (jtraglia)](https://jtraglia.github.io/sil-spec-viewer/)
- [The Sil2 Book](https://sil2book.info)
- [PySpec Tests](tests/core/pyspec/README.md)
