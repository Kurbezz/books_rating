from datetime import date

import ormar

from core.db import metadata, database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Rating(ormar.Model):
    class Meta(BaseMeta):
        tablename = "ratings"
        constraints = [ormar.UniqueColumns("user_id", "book_id")]

    id: int = ormar.BigInteger(primary_key=True, nullable=False)  # type: ignore
    user_id: int = ormar.BigInteger(nullable=False, index=True)  # type: ignore
    book_id: int = ormar.BigInteger(nullable=False)  # type: ignore
    rate: int = ormar.SmallInteger(minimum=1, maximum=5, nullable=False)  # type: ignore
    updated: date = ormar.Date()  # type: ignore
