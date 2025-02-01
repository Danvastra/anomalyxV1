from setuptools import setup, find_packages

setup(
    name="setup",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "python-nmap", 
    ],
    python_requires='>=3.6',  #Python 3.6 atau lebih tinggi
    author="Danvertt",
    author_email=" - ",
    description="This package to install what is required, before running the tool program.",
    long_description_content_type="text/markdown",
    url="https://github.com/username/repository",
)

