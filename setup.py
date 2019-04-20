from setuptools import setup, find_packages
from d2l_book import __version__

requirements = [
    'jupyter'
]

setup(
    name='d2l-book',
    version=__version__,
    install_requires=requirements,
    python_requires='>=3.4',
    author='Mu Li',
    author_email='muli.cmu@google.com',
    url='https://book.d2l.ai',
    description="Create an online book with Jupyter Notebooks and Sphinx",
    license='Apache-2.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'd2l-book = d2l_book.main:main',
        ]
    },
)
