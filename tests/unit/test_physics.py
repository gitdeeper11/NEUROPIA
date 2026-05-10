import sys
sys.path.insert(0, '/storage/emulated/0/Download/NEUROPIA')

def test_entropy_production():
from neuropia import UnifiedEntropyProduction
model = UnifiedEntropyProduction()
assert model is not None
print("test_entropy_production PASSED")

def test_stress_energy():
from neuropia import GeneralizedStressEnergyTensor
model = GeneralizedStressEnergyTensor()
assert model is not None
print("test_stress_energy PASSED")

def test_conservation_laws():
from neuropia import ConservationLaws
model = ConservationLaws()
assert model is not None
print("test_conservation_laws PASSED")

if name == "main":
test_entropy_production()
test_stress_energy()
test_conservation_laws()
print("All physics tests PASSED")
