from setuptools import setup, find_packages

setup(
    name="codelint",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "codelint=codelint.checker:main",
        ],
    },
    author="Aditya Gupta",
    description="A custom PEP 8 checker module",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aditya-1998k/CodeLint",  # Update this with your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)