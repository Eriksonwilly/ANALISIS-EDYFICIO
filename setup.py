#!/usr/bin/env python3
"""
Setup script para CONSORCIO DEJ - Análisis Estructural
"""

from setuptools import setup, find_packages

setup(
    name="consorcio-dej-analisis-estructural",
    version="1.0.0",
    description="Aplicación de análisis estructural para CONSORCIO DEJ",
    author="CONSORCIO DEJ",
    author_email="contacto@consorciodej.com",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=1.5.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "plotly>=5.0.0",
        "reportlab>=3.6.0",
        "openpyxl>=3.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
) 