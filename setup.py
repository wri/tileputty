from setuptools import setup

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Tile Putty",
    version="0.1.0",
    description="Tool to upload a tile cache to AWS S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wri/tileputty",
    packages=["tileputty"],
    author="Thomas Maschler",
    author_email="thomas.maschler@wri.org",
    license="MIT",
    install_requires=["boto3~=1.9.245", "click~=7.0", "parallelpipe~=0.2.6"],
    entry_points={"console_scripts": ["tileputty=tileputty.upload_tiles:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)