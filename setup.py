from setuptools import setup
import os
import sys


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


extra = {}
requirements = [],
tests_require = []

# In case we use python3
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name="pycheddar",
    version="0.9.3",
    packages=['pycheddar'],
    install_requires=requirements,
    author="Jason Ford",
    author_email="jason@jason-ford.com",
    url="https://github.com/jasford",
    description="A Python wrapper for CheddarGetter.",
    long_description=read('README.markdown'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    **extra
)
