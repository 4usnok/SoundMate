from sqlalchemy import Column, Integer, String


class EventModel(Base):
    """Информация об предстоящем событии"""

    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(300))
    name_org = Column(String(100))
