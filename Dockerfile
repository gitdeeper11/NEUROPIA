# NEUROPIA (E-LAB-10) Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install -e .

ENTRYPOINT ["python", "bin/unified_control.py"]
CMD ["--help"]
