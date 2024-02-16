from sanic import Blueprint, Sanic

from .controller import checkController
from .controller_ws import checkWS


def setBlueprints(app: Sanic):

    api = Blueprint.group(
        checkController.checkBp,
        url_prefix="/pj_name/api/v1",
    )

    # for websocket api
    ws = Blueprint.group(
        checkWS.ws_chkBP,
        url_prefix="/pj_name/ws/v1",
    )

    app.blueprint(api)
    app.blueprint(ws)
