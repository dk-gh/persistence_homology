from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = False

# python3 setup.py build_ext -i

setup(
    ext_modules=cythonize('cy_src_sparse_matrix.pyx',
                          annotate=False,
                          language_level=3
                          )
    )
