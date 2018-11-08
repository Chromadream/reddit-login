import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reddit_login",
    version="1.0.0",
    author="Jonathan Nicholas",
    author_email="Jonathan.Nicholas@protonmail.com",
    description="Reddit login flow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chromadream/reddit-login",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
