import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='py-getch and cprint',
    version='1.0.1',
    description='Portable getch() for Python. And -- printing in colour in Python',
    long_description=__doc__,
    author='Joe Esposito and Erwan Vasseure',
    author_email='joe@joeyespo.com',
    url='https://github.com/thetechrobo/install-palc-plus',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    zip_safe=False,
    entry_points={},
)
