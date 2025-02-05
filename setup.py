import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
README = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="custom_logger",
    version="0.1.4",
    packages=find_packages(),
    author="Aluan Luiz Maturi Horschutz",
    description="Uma ferramenta flexível para gerenciamento de logs",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/AluanLuiz/CustomLogger",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8, <4",
    install_requires=[],
    zip_safe=False,
)