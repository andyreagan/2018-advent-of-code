from setuptools import setup
from Cython.Build import cythonize

setup(
    # ext_modules=cythonize("helloworld.pyx")
    ext_modules=cythonize("cached_fixed.pyx")
)
