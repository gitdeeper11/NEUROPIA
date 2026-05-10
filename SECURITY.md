# Security Policy for NEUROPIA (E-LAB-10)

## Supported Versions

| Version | Supported | Notes |
|---------|-----------|-------|
| 1.0.x   | ✅ Yes    | Current stable |
| < 1.0   | ❌ No     | Pre-release only |

## Reporting a Vulnerability

Please report via email to: gitdeeper@gmail.com

You should receive a response within 48 hours.

## Security Considerations for NEUROPIA

### O-SFO (Omni-Spectral Fourier Operator)

- Hard constraint projection applied after every layer
- Spectral kernel bounded by learnable parameters
- No unbounded control signals

### GCN (Grand Constraint Network)

- All 9 conservation laws enforced as hard constraints
- Second Law compliance (dS/dt ≥ 0)
- Cross-domain Onsager symmetry enforced

### UFR (Unified Flux Resolver)

- MPC with safety margin λ_min(T^μν_Σ) ≥ λ_safe
- Actuator limits |F_ctrl| ≤ F_max
- Watchdog timeout at 2 ms

### Physical Constraints (Hard-Enforced)

- div B = 0, div u = 0
- dH_m/dt = −2η·∫(J·B)dV
- dS/dt ≥ 0
- L_ij = L_ji
- ∇^μ G_μν = 0
- Tr(ρ) = 1, ρ ≥ 0
- Σ M_k Γ_k = 0
- J_met steady-state balance
- ∂ρ_I/∂t + ∇·J_I = σ_I

## Known Vulnerabilities (None)

No security vulnerabilities are currently known.

## Responsible Disclosure

1. Reporter notifies us privately
2. We confirm and develop fix (7-14 days)
3. Fix released with patch version
4. Public disclosure after 30 days

---

**Last updated:** May 2026
