import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="k4a",
    version="1.1.0",
    author="The HexOps Authors",
    author_email="stephen.gutekanst@gmail.com",
    description="Python 3 bindings for the Azure Kinect SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hexops/Azure-Kinect-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)