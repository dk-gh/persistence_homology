from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = False

setup(ext_modules=cythonize('cy_src_sparse_matrix.pyx', annotate=False))
