import sys
sys.path.insert(0, '/storage/emulated/0/Download/NEUROPIA')

def test_o_sfo():
from neuropia import OmniSpectralFourierOperator
model = OmniSpectralFourierOperator()
assert model is not None
print("test_o_sfo PASSED")

def test_gcn():
from neuropia import GrandConstraintNetwork
model = GrandConstraintNetwork()
assert model is not None
print("test_gcn PASSED")

def test_hard_constraint_projector():
from neuropia import HardConstraintProjector
model = HardConstraintProjector()
assert model is not None
print("test_hard_constraint_projector PASSED")

if name == "main":
test_o_sfo()
test_gcn()
test_hard_constraint_projector()
print("All neural tests PASSED")
