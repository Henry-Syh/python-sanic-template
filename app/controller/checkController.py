from sanic import Blueprint, Request

from myUtility.sanic.jwt import JWT, jwt_protected
from myUtility.sanic.response import response_successful
from myUtility.responseCode import rCodeEnum

checkBp = Blueprint("check", url_prefix="/check")


@checkBp.get("/")
async def check(request: Request):
    token = await JWT("Henry", request).createAccessToken()
    result = {"my": "check", "token": token}
    return await response_successful(rCode=rCodeEnum.rCode0001, msg=result, data=result)


@checkBp.post("/")
async def check_post(request: Request):
    token = await JWT("Henry", request).createAccessToken()
    result = {"my": "check", "token": token}
    return await response_successful(rCode=rCodeEnum.rCode0001, msg=result, data=result)


@checkBp.get("/auth")
async def check_JWT(request):
    result = await JWT("Henry", request).isTokenValid()
    return await response_successful(rCode=rCodeEnum.rCode0001, msg=result, data=result)


@checkBp.get("/protected")
@jwt_protected
async def check_JWT_protect(request, token, *args, **kwargs):
    return await response_successful(rCode=rCodeEnum.rCode0001, data=token)
