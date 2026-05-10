# Contributing to NEUROPIA (E-LAB-10)

Thank you for your interest in contributing to **NEUROPIA**!

## How to Contribute

### 1. Report Bugs
- Use GitHub/GitLab Issues
- Include: Python version, OS, domains active, steps to reproduce
- Label: `bug`

### 2. Suggest Features
- Open an issue with label `enhancement`
- Describe the use case and expected behavior
- New domain couplings are welcome

### 3. Submit Code Changes

#### Prerequisites
```bash
pip install -e .[dev]
pre-commit install
```

Development Workflow

```bash
git clone https://github.com/YOUR_USERNAME/NEUROPIA
cd NEUROPIA
git checkout -b feature/your-feature-name
pytest tests/ -v
git commit -m "feat: add domain coupling"
git push origin feature/your-feature-name
```

4. Update Documentation

· Edit README.md, docs/, or docstrings
· Ensure make docs builds successfully

Code Style

· Python: PEP 8 (use black)
· Type hints: Required for all public functions
· Docstrings: Google style

Testing Requirements

· All tests must pass: pytest tests/ -v
· Coverage should not decrease: pytest --cov=neuropia
· New features require tests
· All 9 conservation laws must be enforced

Commit Convention

Type Description
feat New feature
fix Bug fix
docs Documentation
test Testing
refactor Code refactor
perf Performance improvement

Questions?

Open an issue or email: gitdeeper@gmail.com

---

Thank you for contributing to unified multi-physics dissipation control! 🧠
