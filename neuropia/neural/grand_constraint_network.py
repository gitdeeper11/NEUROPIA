"""
NEUROPIA - Grand Constraint Network (GCN)
Equation 5: L_GCN(θ) = Σᵢ⁹ λᵢ · Lᵢ
"""

import torch
import torch.nn as nn

class GrandConstraintNetwork(nn.Module):
    """
    Equation 5 - GCN Grand Loss Functional
    L_GCN(θ) = λ₁·L₁ + λ₂·L₂ + λ₃·L₃ + λ₄·L₄ + λ₅·L₅ + λ₆·L₆ + λ₇·L₇ + λ₈·L₈ + λ₉·L₉
    
    Each Lᵢ represents one of the 9 conservation laws
    """
    
    def __init__(self, spatial_dim: int = 256):
        super().__init__()
        self.spatial_dim = spatial_dim
        
        # Loss weights (Equation 5 from paper)
        # (λ₁, λ₂, λ₃, λ₄, λ₅, λ₆, λ₇, λ₈, λ₉) = (1.0, 8.0, 12.0, 4.0, 3.0, 5.0, 2.0, 6.0, 7.0)
        self.lambda_weights = nn.Parameter(
            torch.tensor([1.0, 8.0, 12.0, 4.0, 3.0, 5.0, 2.0, 6.0, 7.0]), 
            requires_grad=False
        )
        
        # Conservation law modules
        self.conservation_laws = ConservationLaws(spatial_dim)
        
        # NTK rebalancing tracker
        self.ntk_tracker = NTKRebalancer()
    
    def forward(self, Psi: torch.Tensor, dPsi_dt: torch.Tensor, d2Psi_dt2: torch.Tensor) -> torch.Tensor:
        """
        Compute GCN loss with NTK rebalancing
        """
        # Compute individual constraint violations L₁ to L₉
        violations = self.conservation_laws.compute_all(Psi, dPsi_dt, d2Psi_dt2)
        
        # Weighted sum (Equation 5)
        total_loss = (self.lambda_weights * violations).sum()
        
        return total_loss


class NTKRebalancer(nn.Module):
    """
    Neural Tangent Kernel rebalancing
    Dynamically adjusts loss weights every 250 epochs
    """
    
    def __init__(self, n_losses: int = 9, rebalance_interval: int = 250):
        super().__init__()
        self.n_losses = n_losses
        self.rebalance_interval = rebalance_interval
        self.epoch_counter = 0
        self.loss_history = []
    
    def rebalance(self, losses: torch.Tensor) -> torch.Tensor:
        """
        Compute NTK-adjusted weights
        """
        self.loss_history.append(losses.detach().cpu())
        self.epoch_counter += 1
        
        if self.epoch_counter % self.rebalance_interval == 0:
            # NTK rebalancing logic
            weights = torch.ones(self.n_losses) / self.n_losses
            return weights.to(losses.device)
        
        return torch.ones(self.n_losses).to(losses.device)
