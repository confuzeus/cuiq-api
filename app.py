import configparser
import logging
import os
import time
from pathlib import Path

from flask import Flask, request
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent

config_file = BASE_DIR / "appconfig.ini"

app_config = configparser.ConfigParser()

if config_file.is_file():
    app_config.read(config_file)

debug = os.getenv("FLASK_ENV") == "development"

app = Flask(__name__)

log_level = logging.INFO
if debug:
    log_level = logging.DEBUG

app.logger.setLevel(log_level)

cors = CORS(
    app,
    resources={r"/api/*": {"origins": "*"}},
)


@app.route("/")
def hello():
    return "cuiq"


def _mangler(data):
    time.sleep(1)
    return data


@app.route("/api", methods=["POST"])
def process_data():
    data = request.get_json()
    processed = _mangler(data)
    return processed
