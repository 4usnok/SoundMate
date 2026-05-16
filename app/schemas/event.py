from pydantic import BaseModel


class EventSchemas(BaseModel):
    """Схема для модели `Event`"""

    title: str
    description: str
    name_org: str
