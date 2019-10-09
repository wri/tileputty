# Tile Putty

This tool helps to upload Vector and Raster tile caches(PBF/ MVT, PNG and JPG format) to AWS S3.
Directory structure on S3 follows this schema:

`layer_name/version/format/option/z/x/y`

## Installation

`pip install tileputty`

## Dependencies and Requirements

This tool uses boto3 to upload files to S3.
You will need to have write permission to the S3 bucket and you AWS credential in an accessible location,
either as [environment varibales](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variables)
or in a [shared credential file](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#shared-credentials-file).

## Usage

Command Line Interface
```bash
Usage: tileputty [OPTIONS] TILE_CACHE

  TILE_CACHE: path to local tile cache

Options:
  --bucket TEXT    AWS Bucket
  --layer TEXT     Dataset Name
  --version TEXT   Dataset Version ID
  --option TEXT    Dataset Version ID
  --ext TEXT       Tile Cache format
  --update_latest  Update latest file in root folder with latest version
                   number
  --help           Show this message and exit.
```

Python
```python
from tileputty.upload_tiles import upload_tiles

tile_cache = "/path/to/tilecache/root"
layer = "mylayer"
version = "v1.0"
bucket = "mybucket"
option = "default"
ext = "png"
update_latest = False

upload_tiles(
    tile_cache,
    layer,
    version,
    bucket=bucket,
    option=option,
    ext=ext,
    update_latest=update_latest,
)
```