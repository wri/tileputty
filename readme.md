# Tile Putty

This tool helps to upload Vector and Raster tile caches (PBF/ MVT, PNG and JPG format) to AWS S3.
Directory structure on S3 follows this schema:

`layer_name/version/implementation/z/x/y.format`

## Installation

`pip install tileputty`

## Dependencies and Requirements

This tool uses boto3 to upload files to S3.
You will need to have write permission to the S3 bucket and you AWS credential in an accessible location,
either as [environment variables](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variables)
or in a [shared credential file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#shared-credentials-file).

## Usage

Command Line Interface
```bash
Usage: tileputty [OPTIONS] TILE_CACHE

  TILE_CACHE: path to local tile cache

Options:
  --bucket TEXT          AWS Bucket
  --dataset TEXT         Dataset Name
  --version TEXT         Dataset Version ID
  --implementation TEXT  Tile Cache Implementation
  --help                 Show this message and exit
```

Python
```python
from tileputty.upload_tiles import upload_tiles

tile_cache = "/path/to/tilecache/root"
dataset = "mylayer"
version = "v1.0"
bucket = "mybucket"
implementation = "default"

upload_tiles(
    tile_cache,
    dataset,
    version,
    bucket=bucket,
    implementation=implementation,
)
```
