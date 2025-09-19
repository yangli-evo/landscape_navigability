__version__ = "0.1.0"

# user could use from src import get_P
from .utils import (
    epsilon,
    threshold_func,
    classify_epistasis,
    classify_epistasis_P_N,
    get_P,
    get_cv,
)

# control the public API
__all__ = [
    "epsilon",
    "threshold_func",
    "classify_epistasis",
    "classify_epistasis_P_N",
    "get_P",
    "get_cv",
]
