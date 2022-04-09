from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status

from app.depends import check_token
from app.models import Rating as RatingDB
from app.serializers import Rating, CreateOrUpdateRating


router = APIRouter(
    prefix="/api/v1/ratings", tags=["ratings"], dependencies=[Depends(check_token)]
)


@router.get("/{user_id}/{book_id}", response_model=Rating)
async def get_rating(user_id: int, book_id: int):
    rating = await RatingDB.objects.get_or_none(user_id=user_id, book_id=book_id)

    if rating is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return rating


@router.post("/", response_model=Rating)
async def create_or_update_rating(data: CreateOrUpdateRating):
    rating, is_created = await RatingDB.objects.get_or_create(
        _defaults={**data.dict(), "updated": date.today()},
        user_id=data.user_id,
        book_id=data.book_id,
    )

    if is_created:
        return rating

    rating.rate = data.rate
    rating.updated = date.today()

    return await rating.update()


healtcheck_router = APIRouter(tags=["healthcheck"])


@healtcheck_router.get("/healthcheck")
async def healthcheck():
    return "Ok!"
