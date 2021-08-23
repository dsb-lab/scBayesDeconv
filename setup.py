import sys

try:
    from skbuild import setup
except ImportError:
    print('Please update pip, you need pip 10 or greater,\n'
          ' or you need to install the PEP 518 requirements in pyproject.toml yourself', file=sys.stderr)
    raise
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="scBayesDec",
    version="0.2",
    description="A gaussian deconvolution package",
    author='Gabriel Torregrosa Cortes',
    author_email="g.torregrosa@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=['scBayesDec', 'scBayesDec/nestedsamplernorm', 'scBayesDec/mcmcsamplernorm', 'scBayesDec/nestedsamplergamma', 'scBayesDec/mcmcsamplergamma', 'scBayesDec/shared_functions'],
    package_dir={'': 'src'},
    cmake_install_dir='src/scBayesDec',
    python_requires = ">=3.5",
    install_requires = ["numpy>=1.17.5","scipy>=1.5.0","dynesty>=0.9.7","pandas>=0.25.0"]
)
