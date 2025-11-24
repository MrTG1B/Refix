"""
RefiX - AI-Powered Text Enhancement Tool
Setup configuration for installation and packaging.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text(encoding="utf-8").strip().split('\n')

setup(
    name="refix",
    version="2.0.0",
    author="MrTG1B",
    author_email="",
    description="AI-Powered Text Enhancement Tool using Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrTG1B/Refix",
    project_urls={
        "Bug Tracker": "https://github.com/MrTG1B/Refix/issues",
        "Documentation": "https://github.com/MrTG1B/Refix#readme",
        "Source Code": "https://github.com/MrTG1B/Refix",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "refix=APP:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.ico", "*.md", ".env.example"],
    },
    keywords="ai text-enhancement gemini productivity automation",
    license="MIT",
)
