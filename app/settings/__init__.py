from .base import *
from .security import *
from .static import *
 
# Carrega um local.py caso exista (Atualmente sempre utilizo .ini)
try:
    from .local import *
except ImportError:
    pass