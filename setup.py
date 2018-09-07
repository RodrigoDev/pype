from pathlib import Path

from setuptools import setup, find_packages

setup(
    name="pype",
    version=0.1,
    packages=find_packages(),
    url="https://github.com/RodrigoDev/pype",
    license="MIT",
    author="Rodrigo Carneiro",
    author_email="rodrigo_carneiro@mail.com",
    description="Dead simple python data pipeline.",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(),
    classifiers=[
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">= 3.5",
)