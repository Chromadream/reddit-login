import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reddit_login",
    version="1.0.0",
    author="Jonathan Nicholas",
    author_email="Jonathan.Nicholas@protonmail.com",
    description="Requests-only basic login flow for Reddit",
    install_requires=["requests>=2.20.0"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chromadream/reddit-login",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
    ],
)
