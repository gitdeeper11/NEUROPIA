"""
NEUROPIA - Unified State Vector (Equation 2.2)
Ψ(r,t) = [u₁, u₂, u₃, B₁, B₂, B₃, h₀₀, h₀₁, h₀₂, h₀₃, T, q₁, q₂, q₃, φ, J₁, J₂, J₃,
          ρ₁₁, ρ₁₂, ρ₂₁, ρ₂₂, c₁, c₂, c₃, c₄, J_met₁, J_met₂, J_met₃, J_met₄, ρ_I, S_AI, F₁, F₂]ᵀ
32 components organized into 9 domain blocks
"""

import torch
import numpy as np
from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class UnifiedStateVector:
    """
    Unified State Vector Ψ(r,t) - 32 components
    Based on Equation 2.2 from NEUROPIA Research Paper
    """
    # Domain Block 1: Fluid Mechanics (components 1-3)
    u: torch.Tensor  # velocity field u(r,t)
    
    # Domain Block 2: Magnetodynamics (components 4-6)
    B: torch.Tensor  # magnetic field B(r,t)
    
    # Domain Block 3: Gravitational (components 7-10)
    h_metric: torch.Tensor  # metric perturbation h_μν(r,t)
    
    # Domain Block 4: Thermal (components 11-12)
    T: torch.Tensor  # temperature
    q: torch.Tensor  # heat flux
    
    # Domain Block 5: Electrochemical (components 13-14)
    phi: torch.Tensor  # electrochemical potential
    J: torch.Tensor   # current density
    
    # Domain Block 6: Quantum Coherence (components 15-18)
    rho_quantum: torch.Tensor  # density matrix ρ_ij (4 real dof)
    
    # Domain Block 7: Chemical Reactive (components 19-22)
    c: torch.Tensor   # species concentrations c_k (×4)
    
    # Domain Block 8: Biological Metabolic (components 23-26)
    J_met: torch.Tensor  # metabolic flux J_met (×4)
    
    # Domain Block 9: Cognitive / Information (components 27-30)
    rho_I: torch.Tensor  # information density
    S_AI: torch.Tensor   # AI entropy
    
    # Domain Block 10: Control Actuation (components 31-32)
    F_ctrl: torch.Tensor  # external control field
    
    def to_tensor(self) -> torch.Tensor:
        """Convert to 32-component tensor"""
        return torch.cat([
            self.u.flatten(), self.B.flatten(), self.h_metric.flatten(),
            self.T.flatten(), self.q.flatten(), self.phi.flatten(),
            self.J.flatten(), self.rho_quantum.flatten(), self.c.flatten(),
            self.J_met.flatten(), self.rho_I.flatten(), self.S_AI.flatten(),
            self.F_ctrl.flatten()
        ])
    
    @classmethod
    def from_tensor(cls, tensor: torch.Tensor, spatial_dim: int):
        """Create from 32-component tensor"""
        idx = 0
        n = spatial_dim ** 3
        return cls(
            u=tensor[idx:idx+3*n].reshape(3, spatial_dim, spatial_dim, spatial_dim),
            B=tensor[idx+3*n:idx+6*n].reshape(3, spatial_dim, spatial_dim, spatial_dim),
            h_metric=tensor[idx+6*n:idx+10*n].reshape(4, spatial_dim, spatial_dim, spatial_dim),
            T=tensor[idx+10*n:idx+11*n].reshape(1, spatial_dim, spatial_dim, spatial_dim),
            q=tensor[idx+11*n:idx+14*n].reshape(3, spatial_dim, spatial_dim, spatial_dim),
            phi=tensor[idx+14*n:idx+15*n].reshape(1, spatial_dim, spatial_dim, spatial_dim),
            J=tensor[idx+15*n:idx+18*n].reshape(3, spatial_dim, spatial_dim, spatial_dim),
            rho_quantum=tensor[idx+18*n:idx+22*n].reshape(4, spatial_dim, spatial_dim, spatial_dim),
            c=tensor[idx+22*n:idx+26*n].reshape(4, spatial_dim, spatial_dim, spatial_dim),
            J_met=tensor[idx+26*n:idx+30*n].reshape(4, spatial_dim, spatial_dim, spatial_dim),
            rho_I=tensor[idx+30*n:idx+31*n].reshape(1, spatial_dim, spatial_dim, spatial_dim),
            S_AI=tensor[idx+31*n:idx+32*n].reshape(1, spatial_dim, spatial_dim, spatial_dim),
            F_ctrl=tensor[idx+32*n:idx+34*n].reshape(2, spatial_dim, spatial_dim, spatial_dim)
        )
