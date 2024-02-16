import os
import sys

from emyUtility.sanic.sanicHandler import (
    CustomErrorHandler,
    TomlConfig,
    afterRespHandler,
    beforeReqHandler,
    beforeStartHandler,
)
from sanic import Sanic
from sanic.config import Config
from sanic_ext import Extend

from .main import setBlueprints


def create_app():
    if ("--dev" in sys.argv) | ("--debug" in sys.argv):
        abs_file_path = os.path.join(os.path.dirname(__file__), "../config_dev.toml")
    else:
        abs_file_path = os.path.join(os.path.dirname(__file__), "../config.toml")
    toml_config = TomlConfig(path=abs_file_path)

    app = Sanic(__name__, config=toml_config)

    app.error_handler = CustomErrorHandler()

    app.register_listener(beforeStartHandler, "before_server_start")
    app.register_middleware(beforeReqHandler, "request")
    app.register_middleware(afterRespHandler, "response")

    # active sanic
    Extend(app)

    # blueprint
    setBlueprints(app)

    # debug 不讓 response timeout
    if ("--dev" in sys.argv) | ("--debug" in sys.argv):
        Config.RESPONSE_TIMEOUT = 31536000  # a year

    return app


app = create_app()
