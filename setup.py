"""
Ajakanga-ContamRisk: Heavy Metal Contamination & Risk Assessment Framework
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="Ajakanga-ContamRisk",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Heavy metal contamination and risk assessment at Ajakanga Dumpsite, Ibadan, Nigeria",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/Ajakanga-ContamRisk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Scientific/Engineering :: GIS",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest>=7.2.0", "pytest-cov>=4.0.0", "black>=23.0.0", "flake8>=6.0.0"],
        "gis": ["geopandas>=0.13.0", "rasterio>=1.3.0", "folium>=0.14.0"],
    },
)
