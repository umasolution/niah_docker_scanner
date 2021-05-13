import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "evaScanner",
    version = "1.0.0",
    author = "Jayesh Patel",
    author_email = "jay.net.in@gmail.com",
    scripts = ['/usr/local/bin/niah-docker'],
    description = ("Find the open source vulnerabilities to get more details eva.io"),
    license = "MIT",
    keywords = "vulnerability scanner, sca software composition analysis",
    url = "http://packages.python.org/eva",
    packages=['src'],
    #long_description=read('README.md'),
    #long_description_content_type='text/markdown',
    classifiers=[
	"Programming Language :: Python :: 3.7",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
    ],
    install_requires=[
	'setuptools==44.1.1',
	'docker==4.4.1',
	'tqdm',
	'requests',
	'termcolor',
	'prettytable',
	'pexpect',
	'semantic_version',
	'pyfiglet',
	'glob2',
	'ptyprocess',
	'PyGithub',
    ],
    python_requires='>=3.7'
)
