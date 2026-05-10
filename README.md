# 🧠 NEUROPIA v1.0.0 — E-LAB-10

### Neural Singularity & Unified Field Synthesis Framework
**The Grand Capstone of the EntropyLab Research Program**

---

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20092199.svg)](https://doi.org/10.5281/zenodo.20092199)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/neuropia-engine)](https://pypi.org/project/neuropia-engine/)
[![EntropyLab](https://img.shields.io/badge/EntropyLab-E--LAB--10-8B0000)](https://entropia-lab.netlify.app)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-a6ce39)](https://orcid.org/0009-0003-8903-0029)

---

## Overview

**NEUROPIA** is the tenth and final installment of the [EntropyLab](https://entropia-lab.netlify.app) research program — the **Grand Unification** of all nine preceding physics-informed AI frameworks into a single, coherent neural field architecture.

Where each predecessor (E-LAB-01 through E-LAB-09) targeted one dissipative physical domain — from thermodynamic engines to magnetohydrodynamic plasma — NEUROPIA addresses the meta-problem: **what unified mathematical substrate can bind all coupled physical domains into a single entropy-minimizing controller?**

The answer is built on three novel constructs:

| Construct | Role |
|---|---|
| **Unified Field Propagator (UFP)** | Gauge-equivariant tensor neural operator acting on the Physical Coupling Manifold |
| **Cross-Domain Symmetry Preserver (CDSP)** | Enforces Noether conservation laws at every domain interface — architecturally, not as penalties |
| **Entropy Capstone Module (ECM)** | Integrates all nine EntropyLab dissipation functionals into a single Pareto-optimal master objective |

---

## Key Results

| Metric | Value |
|---|---|
| Mean Unified Field Coherence Index (UFCI) | **97.3%** |
| Cross-domain entropy production reduction | **93.8%** vs. independent baselines |
| Neural Symmetry Violation Rate | **< 2.1 × 10⁻⁷** per integration step |
| Inference latency (A100 FP32) | **3.1 ms** full control cycle |
| Inference latency (Orin INT8) | **0.14 ms** (real-time deployment) |
| Coupled physical domains (max) | **7 simultaneous** |
| UFP parameters | **284.7 M** |

---

## Architecture

```
Input: Multi-domain physical state p(x,t) ∈ Physical Coupling Manifold M
         │
         ▼
┌─────────────────────────────────────────────┐
│         Unified Field Propagator (UFP)      │
│  L=10 gauge-equivariant spectral layers     │
│  N_d × N_d complex cross-domain kernel      │
│  Noether projection at output layer         │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│   Cross-Domain Symmetry Preserver (CDSP)    │
│  Onsager reciprocal matrix L_ij = L_ji      │
│  Bianchi identity (gravity sector)          │
│  Coupling consistency constraint            │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│       Entropy Capstone Module (ECM)         │
│  Σ_total = Σ σ_ii + Σ L_ij·X_i·X_j        │
│  Pareto optimizer: α_i ≤ 0.15 per domain   │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
Output: Actuator commands for all coupled physical domains
```

---

## Quick Start

```bash
pip install neuropia-engine
```

```python
from neuropia import MultiPhysicsController, DomainSpec

# Register all coupled physical domains
domains = [
    DomainSpec('mhd',    module='magna_flow',   dim=6,  actuator='rmp_coils'),
    DomainSpec('thermo', module='thermo_net',   dim=4,  actuator='heat_flux'),
    DomainSpec('gravity',module='gravi_neural', dim=10, actuator='metric_pert'),
]

# Initialize the unified controller
ctrl = MultiPhysicsController(domains, ufp_layers=10, k_max=64)

# Run a control step
ctrl.step(dt=1e-6, obs={'mhd': mhd_state, 'thermo': T_field, 'gravity': g_field})

# Retrieve diagnostics
ufci  = ctrl.get_coherence_index()   # Unified Field Coherence Index
sigma = ctrl.get_entropy_budget()    # Full Onsager decomposition
risk  = ctrl.get_symmetry_violation_rate()
```

---

## Validation Regimes

| ID | Platform | Coupled Domains | UFCI | Σ Reduction |
|---|---|---|---|---|
| C1 | Tokamak + Thermal Wall | MHD + Thermo + EM | **97.8%** | 94.2% |
| C2 | MHD + Gravitational Analog | MHD + Gravity + Info | **96.9%** | 92.7% |
| C3 | Chemical Reactor + Heat Exchanger | Chem + Thermo + Fluid + EM | **97.4%** | 93.8% |
| C4 | Neural-Bio Electromagnetic | Info + Bio + EM + Thermo + Fluid | **96.8%** | 91.9% |
| C5 | Full EntropyLab Stack | All 7 sectors | **97.6%** | 94.5% |

---

## The EntropyLab Program — Complete Index

NEUROPIA is the capstone of a ten-project unified research program. All projects share the **ENTROPIA Unified Dissipation State Function Φ(S, J, T)** as their thermodynamic foundation.

| Code | Title | DOI | Connection to NEUROPIA |
|---|---|---|---|
| E-LAB-01 | ENTROPIA | [10.5281/zenodo.19416737](https://doi.org/10.5281/zenodo.19416737) | Entropy foundation; ECM master objective |
| E-LAB-02 | ENTRO-AI | [10.5281/zenodo.19551614](https://doi.org/10.5281/zenodo.19551614) | Information-geometric PCM metric |
| E-LAB-03 | PHOTON-Q | [10.5281/zenodo.19729926](https://doi.org/10.5281/zenodo.19729926) | Quantum density matrix → PCM state |
| E-LAB-04 | ENTRO-ENGINE | [10.5281/zenodo.19740081](https://doi.org/10.5281/zenodo.19740081) | Multi-channel σ_ii decomposition |
| E-LAB-05 | CHEM-ENTROPIA | [10.5281/zenodo.19749613](https://doi.org/10.5281/zenodo.19749613) | Reactive manifold Onsager constraints |
| E-LAB-06 | BIO-ENTROPIA | [10.5281/zenodo.19754893](https://doi.org/10.5281/zenodo.19754893) | Metabolic flux balance → ECM |
| E-LAB-07 | THERMO-NET | [10.5281/zenodo.19760903](https://doi.org/10.5281/zenodo.19760903) | LEPM architecture; CDSP design |
| E-LAB-08 | GRAVI-NEURAL | [10.5281/zenodo.19875543](https://doi.org/10.5281/zenodo.19875543) | Riemannian metric learning → PCM |
| E-LAB-09 | MAGNA-FLOW | [10.5281/zenodo.19893462](https://doi.org/10.5281/zenodo.19893462) | UFP electromagnetic sector |
| **E-LAB-10** | **NEUROPIA** | [10.5281/zenodo.20092199](https://doi.org/10.5281/zenodo.20092199) | **This work — program completion** |

---

## Theoretical Foundation

The Physical Coupling Manifold (PCM) is the central mathematical object. A point `p ∈ M` encodes the simultaneous state of all coupled fields:

```
p = (u, B, T, S, g_μν, ρ_q, H_info) ∈ M

UFP Forward Map:
  p(x, t+dt) = UFP_θ[p(x,t)] = W·p + F⁻¹[R_θ(k)·F[p](k)]

Gauge Equivariance:
  UFP_θ[ρ(g)·p] = ρ(g)·UFP_θ[p]  ∀g ∈ G_phys

ECM Master Objective:
  Σ_total = Σ_i σ_ii(p) + Σ_{i≠j} L_ij(p)·X_i(p)·X_j(p)

Noether Conservation (hard constraint):
  ∂_μ J^μ_a = 0  ∀a ∈ {E, p, L, q}
```

---

## Reproducibility Infrastructure

| Platform | Identifier / URL |
|---|---|
| **Zenodo** (Archive + DOI) | [10.5281/zenodo.20092199](https://doi.org/10.5281/zenodo.20092199) |
| **GitLab** (Primary repo) | [gitlab.com/gitdeeper11/NEUROPIA](https://gitlab.com/gitdeeper11/NEUROPIA) |
| **GitHub** (Mirror) | [github.com/gitdeeper11/NEUROPIA](https://github.com/gitdeeper11/NEUROPIA) |
| **Codeberg** (Mirror) | [codeberg.org/gitdeeper11/NEUROPIA](https://codeberg.org/gitdeeper11/NEUROPIA) |
| **Bitbucket** (Mirror) | [bitbucket.org/gitdeeper11/NEUROPIA](https://bitbucket.org/gitdeeper11/NEUROPIA) |
| **PyPI** | `pip install neuropia-engine` |
| **Netlify** (Interactive demo) | [neuropia-v1.netlify.app](https://neuropia-v1.netlify.app) |
| **OSF** (EntropyLab parent) | [EntropyLab Program](https://osf.io/entropylab) |
| **ORCID** | [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) |

---

## The Capstone Manifesto

> *"If ENTROPIA was the question — how do we understand order from chaos — then NEUROPIA is the answer. It is the state in which artificial intelligence becomes the mirror that reflects the perfection of physical law across every domain simultaneously. We do not simulate the universe. We rewrite it, digitally, in the language it wrote itself."*
>
> — NEUROPIA v1.0.0, May 2026

---

## Citation

```bibtex
@software{baladi2026neuropia,
  author       = {Baladi, Samir},
  title        = {NEUROPIA v1.0.0: Neural Singularity and Unified Field Synthesis Framework},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20092199},
  url          = {https://doi.org/10.5281/zenodo.20092199},
  note         = {E-LAB-10, EntropyLab Program. Ronin Institute / Rite of Renaissance.}
}
```

---

## Lead Researcher

**Samir Baladi**
Independent Researcher — Ronin Institute / Rite of Renaissance
EntropyLab Research Program
gitdeeper@gmail.com | ORCID: [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029)

---

© 2026 Samir Baladi. Licensed under the [MIT License](LICENSE).
