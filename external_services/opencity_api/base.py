from json import dumps, JSONEncoder
from typing import Any
from uuid import UUID

from aiohttp import ClientResponse, ClientSession, ClientTimeout


class UUIDEncoder(JSONEncoder):
    def default(self, o) -> str | Any:
        if isinstance(o, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return o.hex
        return JSONEncoder.default(self, o)


async def post_request(
    url: str,
    data: dict,
    headers = None
) -> ClientResponse:
    if headers is None:
        headers: dict[str, str] = {"Content-Type": "application/json"}
    async with ClientSession(timeout=ClientTimeout(connect=600, sock_read=1200)) as session:
        return await session.post(
            url=url, data=dumps(data, ensure_ascii=False, cls=UUIDEncoder), headers=headers
        )
