import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pemtest",
    version="0.0.2",
    author="Turkunov",
    author_email="yaturkunov@gmail.com",
    description="\"Parameters Elimination Method\" Goodness-Of-Fit test for normality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turkunov/pem-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)