import json
from datetime import datetime
from typing import Optional

import pytz
from fastmcp import FastMCP, Context
from pydantic import Field

from backend.Client import FutureQuizClient

mcp = FastMCP(name="futureQuiz")

f = FutureQuizClient()


@mcp.tool(description="获取当前时间")
async def get_current_time(timezone: Optional[str] = Field(description='时区名称 默认UTC', default="UTC")):
    try:
        tz = pytz.timezone(timezone) if timezone else pytz.UTC
        current_time = datetime.now(tz)
        return {
            "status": "success",
            "timezone": timezone,
            "current_time": current_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "timestamp": int(current_time.timestamp()),
        }
    except pytz.exceptions.UnknownTimeZoneError:
        return {
            "status": "error",
            "error": f"Unknown timezone: {timezone}",
            "timezone": "UTC",
            "current_time": datetime.now(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S %Z"),
            "timestamp": int(datetime.now(pytz.UTC).timestamp()),
        }


@mcp.tool(description="获取个人信息")
async def getMyInfo(ctx: Context):
    request = ctx.get_http_request()
    apikey = request.headers.get('apikey')
    res = await f.getSelfInfo(apikey)
    return json.dumps(res.model_dump(), ensure_ascii=False)


@mcp.tool(description="获取个人拥有的问卷")
async def getMyQuizzes(ctx: Context):
    request = ctx.get_http_request()
    apikey = request.headers.get('apikey')
    res = await f.getMyQuizzes(apikey)
    return json.dumps(res.model_dump(), ensure_ascii=False)
