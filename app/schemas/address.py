from pydantic import BaseModel


class AddressSchemas(BaseModel):
    """Схема для модели `AddressModel`"""

    id: int
    city: str
    region: str
    country: str
