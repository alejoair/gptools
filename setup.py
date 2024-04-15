from setuptools import setup, find_packages

setup(
    name="gptools",
    version="0.1.0",
    description="A collection of tools for GPT models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="AlejoAir",
    author_email="example@example.com",
    url="https://github.com/alejoair/gptools",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
