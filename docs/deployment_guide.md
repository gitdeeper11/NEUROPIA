
Deployment Guide

PyPI Deployment

```bash
python -m build
twine upload dist/*
```

Docker Deployment

```bash
docker build -t neuropia:latest .
docker run neuropia:latest --regime full_fusion_plant
```

Netlify Deployment

```bash
cd Netlify/
netlify deploy --prod
```

FPGA Deployment (TensorRT)

```bash
python -m neuropia.export_tensorrt --precision int8 --target versal
```

