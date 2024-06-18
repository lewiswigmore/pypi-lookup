from setuptools import setup, find_packages

setup(
    name="Pypi-lookup",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "vt-py",
    ],
    entry_points={
        "console_scripts": [
            "iplookup=iplookup.cli:main",
        ],
    },
)
