#!/usr/bin/env python3

"""NEUROPIA Upload v1.0.0 - PyPI"""

import requests
import hashlib
import os
import glob

TOKEN = ""

print("="*60)
print("🧠 NEUROPIA v1.0.0 Upload - PyPI")
print("="*60)

# قراءة README.md
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    print(f"📄 README.md: {len(readme)} حرف")
except FileNotFoundError:
    readme = "NEUROPIA: Neural Singularity and Unified Field Synthesis Framework"
    print("📄 README.md غير موجود، استخدام الوصف الافتراضي")

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ لا توجد ملفات توزيع. جاري بناء الحزمة...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 الملفات:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 رفع: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'neuropia-engine',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'NEUROPIA: Neural Singularity and Unified Field Synthesis Framework',
        'home_page': 'https://neuropia-v1.netlify.app',
        'requires_python': '>=3.11',
        'keywords': 'unified-field, entropy-minimization, multi-physics, neural-operator, pinn, gauge-equivariant, noether-conservation, onsager-reciprocity, entropic-gravity, pci, processing-capacity-index'
    }

    # رفع الملف
    with open(filepath, 'rb') as f:
        response = requests.post(
            'https://upload.pypi.org/legacy/',
            files={'content': (filename, f, 'application/octet-stream')},
            data=data,
            auth=('__token__', TOKEN),
            timeout=60,
            headers={'User-Agent': 'NEUROPIA-Uploader/1.0'}
        )

    print(f"   الحالة: {response.status_code}")

    if response.status_code == 200:
        print("   ✅✅✅ نجاح!")
    else:
        print(f"   ❌ خطأ: {response.text[:300]}")

print("\n" + "="*60)
print("🔗 https://pypi.org/project/neuropia-engine/1.0.0/")
print("="*60)
