📦 Installation Guide for NEUROPIA (E-LAB-10)

## Quick Install (PyPI)

```bash
pip install neuropia-engine
```

Install from Source

```bash
git clone https://github.com/gitdeeper11/NEUROPIA.git
cd NEUROPIA
pip install -e .
```

Verify Installation

```python
import neuropia
print(neuropia.__version__)  # 1.0.0
print(neuropia.__doi__)      # 10.5281/zenodo.20092199
```

```bash
python bin/unified_control.py --regime full_fusion_plant --steps 100 --verbose
```

---

Requirements

Package Version Required
Python ≥ 3.11
torch ≥ 2.4.0
numpy ≥ 2.0.0
scipy ≥ 1.14.0
cuFFT (optional) For GPU acceleration

---

Platform Support

Platform Support
Linux ✅ Fully tested
macOS ✅ Compatible
Windows ✅ Compatible
Termux (Android) ✅ Compatible
NVIDIA Jetson Orin ✅ TensorRT supported
Xilinx Versal FPGA ✅ Planned (v2.0)

---

Docker Installation

```bash
docker pull gitdeeper11/neuropia:latest
docker run --rm neuropia --help
```

---

Uninstall

```bash
pip uninstall neuropia-engine
```

---

For issues, open a ticket on GitHub/GitLab.
