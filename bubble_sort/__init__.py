import importlib
import os


name = "bubble_sort"


nums = [int(n) for n in os.getenv("ARG_1").split(",")]
length = len(nums)


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


def main():
    return f"{length}", alg, (nums,)
