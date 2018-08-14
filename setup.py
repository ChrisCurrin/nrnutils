#!/usr/bin/env python

from distutils.core import setup

setup(
    name="nrnutils",
    version="0.3.1",
    py_modules=['nrnutils'],
    author = "Andrew P. Davison",
    author_email = "andrewpdavison@gmail.com",
    description = "Some tools for use with the NEURON simulator (http://www.neuron.yale.edu/neuron/)",
    license = "CeCILL http://www.cecill.info",
    keywords = "computational science neuroscience simulation",
    url = "https://bitbucket.org/apdavison/nrnutils",
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'License :: Other/Proprietary License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering'],
)
