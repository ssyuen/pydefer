import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydefer", # Replace with your own username
    version="0.0.2",
    author="Samuel Yuen",
    author_email="samuel.s.yuen@gmail.com",
    description="Implements a Go-like defer function.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ssyuen/pydefer",
    packages=['pydefer'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
