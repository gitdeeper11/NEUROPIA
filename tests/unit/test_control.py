import sys
sys.path.insert(0, '/storage/emulated/0/Download/NEUROPIA')

def test_ufr():
from neuropia import UnifiedFluxResolver
model = UnifiedFluxResolver()
assert model is not None
print("test_ufr PASSED")

def test_tracker():
from neuropia import UnifiedStateTracker
model = UnifiedStateTracker()
assert model is not None
print("test_tracker PASSED")

if name == "main":
test_ufr()
test_tracker()
print("All control tests PASSED")
