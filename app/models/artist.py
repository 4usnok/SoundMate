from sqlalchemy import Column, Integer, Text, String


class ArtistModel(Base):
    """Модель для информации об артистах"""

    __tablename__ = "artist"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150))
    description = Column(Text(300))
