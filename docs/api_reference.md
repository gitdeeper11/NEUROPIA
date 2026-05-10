
API Reference

UnifiedStateTracker

Main controller class for NEUROPIA.

Methods

· step(dt, multi_obs) - Single control step
· get_neuropia_efficiency() - Returns eta_NEUROPIA
· get_unified_safety_margin() - Returns lambda_min - lambda_safe

NeuropiaEngine

High-level API for NEUROPIA.

Methods

· run_control_campaign(duration_ms, **kwargs) - Run full control campaign
· load_weights(path) - Load pre-trained weights

Example

```python
from neuropia import UnifiedStateTracker, NeuropiaEngine

tracker = UnifiedStateTracker(spatial_dim=256, k_max=96)
engine = NeuropiaEngine(regime='full_fusion_plant')
```

