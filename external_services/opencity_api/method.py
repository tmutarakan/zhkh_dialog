from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4

from aiohttp import ClientResponse

from external_services.opencity_api import model
from external_services.opencity_api.base import post_request


async def error_account(response: dict) -> model.ErrorAPIResponse:
    return model.ErrorAPIResponse(**response)


async def create_token(authentication_url: str, login: str, password: str):
    request = model.CreateToken(
        id=f"{uuid4()}",
        params=model.CreateTokenParams(
            login=login,
            password=password
        )
    )
    response: ClientResponse = await post_request(
        url=authentication_url,
        data=request.model_dump()
    )
    return await response.json()


@dataclass
class Base:
    apigate_url: str
    api_token: str

    async def _get_response(self) -> ClientResponse:
        headers: dict[str, str] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_token}"
        }
        data = self.request.model_dump()
        return await post_request(url=self.apigate_url, data=data, headers=headers)

    async def get_response(self):
        response: ClientResponse = await self._get_response()
        return await response.json()


@dataclass
class Search(Base):
    street: str | None = None
    house_number: str | None = None
    flat_number: str | None = None

    async def search_street(self):
        self.request = model.SearchStreet(
            id=f"{uuid4()}",
            params=model.SearchStreetParams(
                filter=model.SearchStreetFilter(
                    name={"$eq": self.street}
                )
            )
        )
        return await self.get_response()

    async def search_house(self):
        self.request = model.SearchHouse(
            id=f"{uuid4()}",
            params=model.SearchHouseParams(
                filter=model.SearchHouseFilter(
                    street={"$eq": self.street},
                    houseNumber={"$eq": self.house_number}
                )
            )
        )
        return await self.get_response()

    async def search_flat(self):
        self.request = model.SearchFlat(
            id=f"{uuid4()}",
            params=model.SearchFlatParams(
                filter=model.SearchFlatFilter(
                    street={"$eq": self.street},
                    houseNumber={"$eq": self.house_number},
                    number={"$eq": self.flat_number}
                )
            )
        )
        return await self.get_response()


@dataclass
class Check(Base):
    flat_id: str
    personal_account: str

    async def check_personal_account(self):
        self.request = model.CheckPersonalAccount(
            id=f"{uuid4()}",
            params=model.CheckPersonalAccountParams(
                filter=model.CheckPersonalAccountFilter(
                    flatId={"$eq": self.flat_id},
                    number={"$eq": self.personal_account}
                )
            )
        )
        return await self.get_response()


@dataclass
class Issue(Base):
    fullname: str
    personal_account: str
    service: int
    text: str
    building: str
    flat: str
    house: str
    phone: str
    street: str
    file_ids: list = field(default_factory=list)
    request: Optional[model.IssueCreate] = None

    async def create_request(self) -> None:
        self.request = model.IssueCreate(
            id=f"{uuid4()}",
            params=model.IssueCreateParams(
                data=model.IssueCreateData(
                    nameApplicant=self.fullname,
                    personalAccountNumber=self.personal_account,
                    service=self.service,
                    text=self.text,
                    buildingNumber=self.building,
                    flatNumber=self.flat,
                    houseNumber=self.house,
                    phone=self.phone,
                    street=self.street,
                    fileIds=self.file_ids
                )
            )
        )
