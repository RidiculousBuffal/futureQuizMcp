import asyncio
import os

import dotenv
import httpx
from backend.model.Result import Result

limits = httpx.Limits(max_connections=100, max_keepalive_connections=20)
timeout = httpx.Timeout(None, connect=5.0)  # 设置时间限制
dotenv.load_dotenv()


class FutureQuizClient:
    BASE_URL = os.getenv('APP_URL')

    def _getHeader(self, apikey):
        return {
            "apikey": apikey
        }

    async def checkAPIKeyValid(self, apikey):
        async with httpx.AsyncClient(verify=False, timeout=timeout, limits=limits) as client:
            resp = await client.post(url=f"{self.BASE_URL}/apiKey/checkapikey", headers=self._getHeader(apikey))
            return Result(**resp.json())

    async def getSelfInfo(self,apikey):
        async with httpx.AsyncClient(verify=False, timeout=timeout, limits=limits) as client:
            resp = await client.get(url=f"{self.BASE_URL}/mcpproxy/getMyInfo", headers=self._getHeader(apikey))
            return Result(**resp.json())

    async def getMyQuizzes(self,apikey):
        async with httpx.AsyncClient(verify=False, timeout=timeout, limits=limits) as client:
            resp = await client.get(url=f"{self.BASE_URL}/mcpproxy/getMyQuizes", headers=self._getHeader(apikey))
            return Result(**resp.json())
if __name__=="__main__":
    f = FutureQuizClient()
    async def main():
        data = await f.getMyQuizzes("AK-F9ppqdkZeC6gngYcvDrKDDV1zsSLa6uEBtnS")
        print(data)
    asyncio.run(main())