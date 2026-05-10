"""Unit tests for NEUROPIA physics layer"""

import pytest
import torch
from neuropia.physics.unified_entropy_production import UnifiedEntropyProduction
from neuropia.physics.generalized_stress_energy import GeneralizedStressEnergyTensor

def test_entropy_production():
    """Test Equation 9 - Unified Entropy Production Rate"""
    model = UnifiedEntropyProduction()
    Psi = torch.randn(32, 64, 64, 64)
    dPsi_dt = torch.randn(32, 64, 64, 64)
    
    result = model(Psi, dPsi_dt)
    assert result is not None
    assert result.shape == torch.Size([])  # scalar

def test_stress_energy():
    """Test Equation 7 - Generalized Stress-Energy Tensor"""
    model = GeneralizedStressEnergyTensor(spatial_dim=64)
    Psi = torch.randn(32, 64, 64, 64)
    
    T_munu, lambda_min = model(Psi)
    assert T_munu is not None
    assert lambda_min is not None

def test_conservation_laws():
    """Test 9 conservation laws"""
    from neuropia.physics.conservation_laws import ConservationLaws
    model = ConservationLaws(spatial_dim=64)
    Psi = torch.randn(32, 64, 64, 64)
    
    violation = model(Psi)
    assert violation is not None
    assert violation.shape == torch.Size([])
