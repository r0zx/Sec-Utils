from setuptools import setup, find_packages

setup(
    name="sec-utils",
    version="0.1.0",
    description="CLI pentesting utility toolkit",
    author="r0zx",
    author_email="dhimanyatin4@gmail.com",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "sec-utils=secutils.cli:run",
        ],
    },
)
