"""Unit tests for NEUROPIA control layer"""

import pytest
import torch
from neuropia.control.unified_flux_resolver import UnifiedFluxResolver

def test_ufr():
    """Test Equation 8 - UFR Control Objective"""
    model = UnifiedFluxResolver(n_components=32)
    
    Psi = torch.randn(32, 64, 64, 64)
    lambda_min = torch.randn(64, 64, 64)
    
    F_ctrl = model(Psi, lambda_min)
    assert F_ctrl is not None
    assert F_ctrl.shape[-1] == 2  # F_ctrl has 2 components
