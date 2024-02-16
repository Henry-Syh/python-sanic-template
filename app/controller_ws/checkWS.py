import asyncio

from sanic import Blueprint, Request, Websocket

ws_chkBP = Blueprint("ws_chk", url_prefix="/wsCheck")


@ws_chkBP.websocket("/echo")
async def chkEcho(request: Request, ws: Websocket):
    """terminal -> wscat -c ws://127.0.0.1:8001/pj_name/ws/v1/wsCheck/echo"""
    data = "hello!"
    print("Sending: " + data)

    count = 0
    while True:
        await ws.send(data)
        # data = await ws.recv()
        await asyncio.sleep(1)
        print(f"Received_{count}_{data}")
        count = count + 1
