from sqlalchemy import Column, Integer, String


class AddressModel(Base):
    """Модель для информации об адресе проведения"""

    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String(100))
    region = Column(String(100))
    country = Column(String(100))
