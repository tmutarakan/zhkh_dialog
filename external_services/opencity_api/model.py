from typing import Optional

from pydantic import BaseModel, UUID4


class Error(BaseModel):
    code: int
    message: str
    data: str = None


class ErrorAPIResponse(BaseModel):
    id: UUID4
    jsonrpc: str
    error: Error


# Авторизация в ИС Открытый Нижнекамск (token.create)
class CreateTokenParams(BaseModel):
    login: str
    password: str


class CreateToken(BaseModel):
    """Авторизация в ИС Открытый Нижнекамск

    jsonrpc - Версия jsonrpc. Допустимые значения: ["2.0"]

    method - Наименование метода. Допустимые значения: ["token.create"]

    id - UUID – универсальный уникальный идентификатор. Генерируется на
    стороне внешнего сервиса.

    params - Параметры запроса
    """
    jsonrpc: str = "2.0"
    method: str = "token.create"
    id: UUID4
    params: CreateTokenParams


class CreateTokenResultReturn(BaseModel):
    """
    refresh_token - Токен обновления

    token - Токен
    """
    refresh_token: str
    token: str


class CreateTokenReturn(BaseModel):
    """
    id - UUID – универсальный уникальный идентификатор

    jsonrpc - Версия jsonrpc

    result - Тело ответа
    """
    id: UUID4
    jsonrpc: str
    result: CreateTokenResultReturn


# Поиск улицы в ИС Открытый Нижнекамск (opencity.gis.street.index)
class SearchStreetFilter(BaseModel):
    name: dict


class SearchStreetParams(BaseModel):
    filter: SearchStreetFilter


class SearchStreet(BaseModel):
    """Поиск улицы в ИС Открытый Нижнекамск

    jsonrpc - Версия jsonrpc. Допустимые значения: ["2.0"]

    method - Наименование метода.
    Допустимые значения: ["opencity.gis.street.index"]

    id - UUID – универсальный уникальный идентификатор. Генерируется на
    стороне внешнего сервиса.

    params - Параметры запроса
    """
    jsonrpc: str = "2.0"
    method: str = "opencity.gis.street.index"
    id: UUID4
    params: SearchStreetParams


class SearchStreetItemReturn(BaseModel):
    id: int
    name: str
    fiasId: Optional[UUID4] = None
    cityId: Optional[int] = None
    typeId: Optional[int] = None
    settlementId: Optional[int] = None


class SearchStreetResultReturn(BaseModel):
    items: list[SearchStreetItemReturn]
    total: int


class SearchStreetReturn(BaseModel):
    jsonrpc: str
    result: SearchStreetResultReturn
    id: UUID4


# Поиск дома в ИС Открытый Нижнекамск (opencity.gis.house.index)
class SearchHouseFilter(BaseModel):
    street: dict
    houseNumber: dict


class SearchHouseParams(BaseModel):
    filter: SearchHouseFilter


class SearchHouse(BaseModel):
    """Поиск дома в ИС Открытый Нижнекамск

    jsonrpc - Версия jsonrpc. Допустимые значения: ["2.0"]

    method - Наименование метода.
    Допустимые значения: ["opencity.gis.house.index"]

    id - UUID – универсальный уникальный идентификатор. Генерируется на
    стороне внешнего сервиса.

    params - Параметры запроса
    """
    jsonrpc: str = "2.0"
    method: str = "opencity.gis.house.index"
    id: UUID4
    params: SearchHouseParams


class SearchHouseItemReturn(BaseModel):
    id: int
    streetId: int
    number: str
    buildingNumber: str
    lat: str
    lng: str
    streetName: str
    controlId: int


class SearchHouseResultReturn(BaseModel):
    items: list[SearchHouseItemReturn]
    total: int


class SearchHouseReturn(BaseModel):
    jsonrpc: str
    result: SearchHouseResultReturn
    id: UUID4


# Поиск квартиры в ИС Открытый Нижнекамск (opencity.gis.flat.index)
class SearchFlatFilter(BaseModel):
    street: dict
    houseNumber: dict
    number: dict


class SearchFlatParams(BaseModel):
    filter: SearchFlatFilter


class SearchFlat(BaseModel):
    """Поиск квартиры в ИС Открытый Нижнекамск

    jsonrpc - Версия jsonrpc. Допустимые значения: ["2.0"]

    method - Наименование метода.
    Допустимые значения: ["opencity.gis.flat.index"]

    id - UUID – универсальный уникальный идентификатор. Генерируется на
    стороне внешнего сервиса.

    params - Параметры запроса
    """
    jsonrpc: str = "2.0"
    method: str = "opencity.gis.flat.index"
    id: UUID4
    params: SearchFlatParams


class SearchFlatItemReturn(BaseModel):
    id: int
    porch: str
    number: str
    stage: int
    typeId: int
    houseId: int
    houseNumber: str
    buildingNumber: str
    streetId: int
    streetName: str
    controlId: int


class SearchFlatResultReturn(BaseModel):
    items: list[SearchFlatItemReturn]
    total: int


class SearchFlatReturn(BaseModel):
    jsonrpc: str
    result: SearchFlatResultReturn
    id: UUID4


# Проверка привязки лицевого счёта к адресу
class CheckPersonalAccountFilter(BaseModel):
    flatId: dict
    number: dict


class CheckPersonalAccountParams(BaseModel):
    filter: CheckPersonalAccountFilter


class CheckPersonalAccount(BaseModel):
    jsonrpc: str = "2.0"
    method: str = "opencity.flat.account.count"
    id: UUID4
    params: CheckPersonalAccountParams


class CheckPersonalAccountReturn(BaseModel):
    jsonrpc: str
    result: int
    id: UUID4


# Создание заявки в ИС Открытый Нижнекамск (opencity.issue.create)
class IssueCreateData(BaseModel):
    nameApplicant: str
    personalAccountNumber: str
    service: int
    text: str
    buildingNumber: str
    flatNumber: str
    houseNumber: str
    phone: str
    street: str
    fileIds: list


class IssueCreateParams(BaseModel):
    data: IssueCreateData


class IssueCreate(BaseModel):
    """Создание заявки в ИС Открытый Нижнекамск

    jsonrpc - Версия jsonrpc. Допустимые значения: ["2.0"]

    method - Наименование метода.
    Допустимые значения: ["opencity.issue.create"]

    id - UUID – универсальный уникальный идентификатор. Генерируется на
    стороне внешнего сервиса.

    params - Параметры запроса
    """
    jsonrpc: str = "2.0"
    method: str = "opencity.issue.create"
    id: UUID4
    params: IssueCreateParams


class IssueCreateProviderReturn(BaseModel):
    providerId: int
    providerName: str


class IssueCreateResultReturn(BaseModel):
    id: int
    number: str
    isInTime: bool
    problemId: int
    state: str
    type: str
    serviceName: str
    trackerId: int
    parentServiceId: int
    parentServiceName: str
    userId: int
    nameApplicant: str
    phoneApplicant: str
    serviceId: int
    text: str
    latitude: str
    longitude: str
    standardDate: int
    standardDateLeft: int
    personalAccountNumber: int
    flatNumber: str
    houseNumber: str
    buildingNumber: str
    streetName: str
    activeStatusTime: int
    timestamp: int
    isInTimeProvider: bool
    isInTimeControl: bool
    provider: list[IssueCreateProviderReturn]
    controlId: int
    controlName: str
    viewed: bool
    year: str
    title: str


class IssueCreateReturn(BaseModel):
    jsonrpc: str
    result: IssueCreateResultReturn
    id: UUID4


# Отключения
class BlackoutSort(BaseModel):
    field: str
    desc: str


class BlackoutFilter(BaseModel):
    houseId: dict


class BlackoutParams(BaseModel):
    filter: BlackoutFilter
    limit: int = 20
    offset: int = 0
    sort: list[BlackoutSort]


class Blackout(BaseModel):
    jsonrpc: str = "2.0"
    method: str = "opencity.interrupt.index"
    id: UUID4
    params: BlackoutParams
