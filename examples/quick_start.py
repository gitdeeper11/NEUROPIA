#!/usr/bin/env python3
"""NEUROPIA Quick Start Example"""

import sys
sys.path.insert(0, '/storage/emulated/0/Download/NEUROPIA')

def main():
    from neuropia import UnifiedStateTracker, NeuropiaEngine
    
    print("=" * 50)
    print("NEUROPIA Quick Start")
    print("=" * 50)
    
    tracker = UnifiedStateTracker(spatial_dim=32, k_max=16)
    
    multi_obs = {
        'u_field': [1.0, 0.5, 0.2],
        'B_field': [0.8, 0.3, 0.1],
        'T_field': 0.9,
        'rho_q': [0.7, 0.6, 0.5, 0.4]
    }
    
    next_state = tracker.step(dt=1e-6, multi_obs=multi_obs)
    eta = tracker.get_neuropia_efficiency()
    
    print(f"State vector length: {len(next_state)}")
    print(f"UFCI: {eta:.1%}")
    
    engine = NeuropiaEngine(regime='full_fusion_plant')
    result = engine.run_control_campaign()
    
    print(f"Mean Efficiency: {result.mean_efficiency:.1%}")
    print(f"Dissipation Reduction: {result.dissipation_reduction:.1%}")
    print(f"Instability Suppression: {result.instability_suppression:.1f}x")
    print("=" * 50)
    return 0

if __name__ == "__main__":
    exit(main())
