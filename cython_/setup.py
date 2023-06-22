import os
import shutil
from distutils.core import setup

from Cython.Build import cythonize

m = os.getenv("MODULE")
t = os.getenv("TYPED", "") in ("1", "True", "true", "TRUE")

if t:
    src, dst = f"../{m}/impl.pyx", f"{m}_typed.pyx"
else:
    src, dst = f"../{m}/impl.py", f"{m}.pyx"

shutil.copy2(src, dst)
setup(ext_modules=cythonize(dst))
os.remove(dst)
