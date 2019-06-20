#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "python>=3.6",
    "tensorflow",
    "numpy",
    "matplotlib",
    "seaborn",
    "jupyter",
    "nltk",
    "gensim",
    "theano",
    "pytest",
    "pip:",
    "git+https://github.com/brain-score/brain-score.git@e97478f",
    "git+https://github.com/brain-score/result_caching.git",
    "pillow",
    "llist",
    "git+https://github.com/mschrimpf/skip-thoughts.git@7d46c14",
    "git+https://github.com/mschrimpf/lm_1b.git@dd4061b",
    "nbsvm",
    "git+https://github.com/williamrainer/OpenNMT-py.git@cdc8f37",
    # TODO: replace pip torchtext with  pip install git+https://github.com/pytorch/text.gitCollecting git+https://github.com/pytorch/text.git
]

test_requirements = [
    "pytest",
]

setup(
    name='neural-nlp',
    version='0.1.0',
    description="Can artificial neural networks capture language processing in the human brain?",
    long_description=readme,
    author="Martin Schrimpf",
    author_email='msch@mit.edu',
    url='https://github.com/mschrimpf/neural-nlp',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='computational neuroscience, human language, '
             'machine learning, deep neural networks, recursive neural networks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)