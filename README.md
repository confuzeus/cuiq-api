# cuiq-api
Quickly build a tiny api with Flask and Docker

## Quick start

Make and activate a virtual environment:

```shell
virtualenv venv
source venv/bin/activate
```

Install pip requirements:

```shell
pip install -r requirements.txt -r requirements-dev.txt
```

Run app by typing `make`.

## Configuration

To configure the api, copy *appconfig.example.ini* to
*appconfig.ini*. All all your settings in there and they
will be available in the `app_config` object.

## License and Copyright

License is MIT.

Copyright 2022 Josh Michael Karamuth
