from datetime import datetime

from pydantic import BaseModel


class VenueSchemas(BaseModel):
    """Схема модели `VenueModel`"""

    name: str
    price: float
    date: datetime
    time: datetime
