from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "machine_efficiency_prediction",
    version="0.1",
    author = "DEV",
    packages=find_packages(),
    install_requires = requirements,
)