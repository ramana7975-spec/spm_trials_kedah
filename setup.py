"""
Setup configuration for SPM Trials Kedah project
"""

from setuptools import setup, find_packages

setup(
    name="spm_trials_kedah",
    version="0.1.0",
    description="Solutions for SPM 2025 Trial Exam - Kedah",
    author="SPM Solutions Team",
    author_email="ramana7975@gmail.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "sympy>=1.12",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
        "jupyter>=1.0.0",
        "ipython>=8.12.0",
        "mpmath>=1.3.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
