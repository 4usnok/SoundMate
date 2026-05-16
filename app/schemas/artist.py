from pydantic import BaseModel


class ArtistSchemas(BaseModel):
    """Схема для модели `Artist`"""

    name: str
    description: str
