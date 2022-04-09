from datetime import date

import orjson
from pydantic import BaseModel, conint


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class ORJSONConfig:
    json_loads = orjson.loads
    json_dumps = orjson_dumps


class Rating(BaseModel):
    id: int
    user_id: int
    book_id: int
    rate: int
    updated: date

    class Config(ORJSONConfig):
        pass


class CreateOrUpdateRating(BaseModel):
    user_id: int
    book_id: int
    rate: conint(ge=1, le=5)  # type: ignore

    class Config(ORJSONConfig):
        pass
