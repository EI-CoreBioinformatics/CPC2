# coding: utf-8
from setuptools import setup, find_packages
from setuptools.extension import Extension
from distutils.extension import Extension
from codecs import open
from os import path
import glob
import re
import sys
import subprocess as sp


here = path.abspath(path.dirname("__file__"))

# with open(path.join(here, "DESCRIPTION.md"), encoding="utf-8") as description:
# 	description = long_description = description.read()

name="CPC2"
version = "2.0"

if sys.version_info.major != 3:
	raise EnvironmentError("""minos is a python module that requires python3, and is not compatible with python2. Also, it is now 2020 and support for 2.x has ceased.""")

cmd = "cd CPC2/libs/libsvm/libsvm-3.18 && make clean && make"
print("Unpacking and building libsvm...", end="", flush=True)
sp.check_output(cmd, shell=True, stderr=sp.STDOUT)
print(" done.")

requirements = [line.rstrip() for line in open("requirements.txt", "rt")]

setup(
	name=name,
	python_requires=">=3.6",
	version=version,
	# description=description,
	# long_description=long_description,
	author="Yu-Jian Kang",
	author_email="gaog@mail.cbi.pku.edu.cn",
	classifiers=[
		"Topic :: Scientific Engineering :: Bio/Informatics",
		"Operating System :: POSIX :: Linux",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9"
	],
	zip_safe=False,
	keywords="gene annotation",
	packages=find_packages(exclude=["test"]),
	scripts=[
		script for script in glob.glob("bin/slurm/*_sub")
	],
    install_requires=requirements,
	entry_points={
		"console_scripts": [
			"CPC2=CPC2.__init__:main",
		]
	},
	package_data={
		"CPC2.data": ["*"],
		"CPC2.libs": ["*", "*/*", "*/*/*", "*/*/*", "*/*/*/*"],
		"minos.etc": ["*.json", "*.yaml", "*.def", "test/*"],
		"minos.dependencies": ["*.sh", "container_defs/*"]
	},
	include_package_data=True,
)
