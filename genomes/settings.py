# settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ...existing code...

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

print(f"STATIC_ROOT: {STATIC_ROOT}")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ...existing code...
print(f"STATIC_ROOT: {STATIC_ROOT}")# ...existing code...
print(f"STATIC_ROOT: {STATIC_ROOT}")

# ...existing code...
