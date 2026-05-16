from sqlalchemy import Column, Integer, String, Float, Date


class VenueModel(Base):
    """Информация об месте проведения"""

    __tablename__ = "venue"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Float)
    date = Column(Date)
    time = Column(Date)
