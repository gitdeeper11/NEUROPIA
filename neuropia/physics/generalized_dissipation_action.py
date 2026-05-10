"""
NEUROPIA - Generalized Dissipation Action (Equation 2.1)
S[Ψ] = ∫∫∫∫∫∫∫∫∫ [ ½(∂Ψ/∂t)ᵀ G (∂Ψ/∂t) - V[Ψ] - Φ(S,J,T) ] dV dt
"""

import torch
import torch.nn as nn

class GeneralizedDissipationAction(nn.Module):
    """
    Equation 2.1 - Generalized Dissipation Action
    S[Ψ] = ∫∫∫∫∫∫∫∫∫ [ ½(∂Ψ/∂t)ᵀ G (∂Ψ/∂t) - V[Ψ] - Φ(S,J,T) ] dV dt
    
    G: Generalized Metric Tensor encoding inertia structure
    V: Conservative inter-domain coupling potential
    Φ: ENTROPIA Unified Dissipation State Function
    """
    
    def __init__(self, spatial_dim: int = 256, n_components: int = 32):
        super().__init__()
        self.spatial_dim = spatial_dim
        self.n_components = n_components
        
        # Generalized Metric Tensor G (learnable)
        self.G = nn.Parameter(torch.eye(n_components) * 0.1)
        
        # Conservative potential MLP
        self.potential_net = nn.Sequential(
            nn.Linear(n_components, 256),
            nn.GELU(),
            nn.Linear(256, 256),
            nn.GELU(),
            nn.Linear(256, 1)
        )
    
    def kinetic_term(self, dPsi_dt: torch.Tensor) -> torch.Tensor:
        """½(∂Ψ/∂t)ᵀ G (∂Ψ/∂t)"""
        return 0.5 * torch.einsum('...i,ij,...j->...', dPsi_dt, self.G, dPsi_dt)
    
    def conservative_potential(self, Psi: torch.Tensor) -> torch.Tensor:
        """V[Ψ] - conservative inter-domain coupling potential"""
        return self.potential_net(Psi)
    
    def dissipation_function(self, Psi: torch.Tensor, entropy_production: torch.Tensor) -> torch.Tensor:
        """Φ(S,J,T) - ENTROPIA Unified Dissipation State Function"""
        # Based on E-LAB-01: Φ = α·S + β·J²/T + γ·(∂J/∂t)²
        return entropy_production
    
    def forward(self, Psi: torch.Tensor, dPsi_dt: torch.Tensor, entropy_production: torch.Tensor) -> torch.Tensor:
        """
        Compute Generalized Dissipation Action
        """
        kinetic = self.kinetic_term(dPsi_dt)
        potential = self.conservative_potential(Psi)
        dissipation = self.dissipation_function(Psi, entropy_production)
        
        action = (kinetic - potential - dissipation).mean()
        return action
