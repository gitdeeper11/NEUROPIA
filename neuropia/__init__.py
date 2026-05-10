"""NEUROPIA: Neural Cognitive Field Unification for Cross-Domain Dissipative Intelligence"""

__version__ = "1.0.0"
__doi__ = "10.5281/zenodo.20092199"
__author__ = "Samir Baladi"
__license__ = "MIT"
__email__ = "gitdeeper@gmail.com"

from neuropia.tracker.unified_state_tracker import UnifiedStateTracker, NeuropiaEngine
from neuropia.physics.unified_entropy_production import UnifiedEntropyProduction, GeneralizedStressEnergyTensor, ConservationLaws
from neuropia.neural.omni_spectral_fourier_operator import OmniSpectralFourierOperator, HardConstraintProjector
from neuropia.control.unified_flux_resolver import UnifiedFluxResolver

__all__ = [
    "UnifiedStateTracker",
    "NeuropiaEngine",
    "UnifiedEntropyProduction",
    "GeneralizedStressEnergyTensor",
    "ConservationLaws",
    "OmniSpectralFourierOperator",
    "HardConstraintProjector",
    "UnifiedFluxResolver",
    "__version__",
    "__doi__",
]
