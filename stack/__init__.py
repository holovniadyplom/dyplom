import importlib
import os
from typing import Callable

name = "stack"


if os.getenv("CYTHON") in ("1", "True", "true", "TRUE"):
    m = os.getenv("MODULE")
    t = os.getenv("TYPED", "") in ("1", "True", "true", "TRUE")

    work_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if t:
        alg = importlib.import_module(f"cython_.{m}_typed", package=work_dir).alg
    else:
        alg = importlib.import_module(f"cython_.{m}", package=work_dir).alg

else:
    from .impl import alg


def main() -> tuple[str, Callable, tuple]:
    n = int(os.getenv("ARG_1"))
    return f"{n}", alg, (n,)
