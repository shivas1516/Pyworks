from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Pyworks",
    version="0.1.0",
    author="SIVASUBRAMANIAM",
    author_email="shivasubramaniam1516@gmail.com.com",
    description="A versatile Python library with utilities for QR code manipulation, password generation, URL shortening, calculator and other python utilities in upcoming relase. This Library main coffues on learnings in python ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shivas1516/Pyworks.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "qrcode",
        "pyzbar",
        "math"
    ],
)
