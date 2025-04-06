# type: ignore
from sqlalchemy import Column, Integer, String, Float
from database import Base

class PlayerProp(Base):
    __tablename__ = "player_props"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String)
    stat = Column(String)
    line = Column(Float)
    hit_count = Column(Integer)
    game_count = Column(Integer)
