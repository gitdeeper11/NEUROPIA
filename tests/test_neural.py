"""Unit tests for NEUROPIA neural layer"""

import pytest
import torch
from neuropia.neural.omni_spectral_fourier_operator import OmniSpectralFourierOperator

def test_o_sfo():
    """Test Equation 3 and 4 - O-SFO Forward Map"""
    model = OmniSpectralFourierOperator(
        n_components=32,
        n_modes=64,
        n_layers=8,
        hidden_channels=256,
        spatial_dim=64
    )
    
    Psi = torch.randn(32, 64, 64, 64)
    output = model(Psi)
    
    assert output is not None
    assert output.shape == Psi.shape

def test_gcn():
    """Test Equation 5 - GCN Grand Loss Functional"""
    from neuropia.neural.grand_constraint_network import GrandConstraintNetwork
    model = GrandConstraintNetwork(spatial_dim=64)
    
    Psi = torch.randn(32, 64, 64, 64)
    dPsi_dt = torch.randn(32, 64, 64, 64)
    d2Psi_dt2 = torch.randn(32, 64, 64, 64)
    
    loss = model(Psi, dPsi_dt, d2Psi_dt2)
    assert loss is not None
    assert loss.shape == torch.Size([])
