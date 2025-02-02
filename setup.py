from setuptools import setup, find_packages
from d2lbook import __version__

requirements = [
   'jupyter',
   'regex',
   'sphinx==5.2.0',
   'recommonmark',
   'nbformat',
   'nbconvert',
   'sphinxcontrib-bibtex<2.0.0',
   'pybtex-apa-style',
   'mu-notedown',
   'mxtheme>=0.3.16',
   'sphinxcontrib-svg2pdfconverter',
   'numpydoc',
   'awscli',
   'gitpython',
   'sphinx_autodoc_typehints==1.10.1',
   'astor',
   'yapf',
   'fasteners',
   'isort',
   'anyio==3.7.1',
   'h11==0.12.0'
]

setup(
    name='d2lbook',
    version=__version__,
    install_requires=requirements,
    setup_requires=['sphinx>=2.2.1'],
    python_requires='>=3.8',
    author='D2L Developers',
    author_email='d2l.devs@gmail.com',
    url='https://book.d2l.ai',
    description="Create an online book with Jupyter Notebooks and Sphinx",
    license='Apache-2.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={'d2lbook':['config_default.ini', 'upload_doc_s3.sh', 'upload_github.sh']},
    entry_points={
        'console_scripts': [
            'd2lbook = d2lbook.main:main',
        ]
    },
)
