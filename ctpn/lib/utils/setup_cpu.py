import os
from distutils.core import setup
from distutils.extension import Extension
from os.path import join as pjoin

import numpy as np
from Cython.Distutils import build_ext
from Cython.Build import cythonize


try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()


setup(
    ext_modules=cythonize(["bbox.pyx","cython_nms.pyx"]),
include_dirs=[np.get_include()]
)