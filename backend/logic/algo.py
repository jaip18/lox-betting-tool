from database import SessionLocal
from models import NBAPlayer, NBAPlayerGamelogs, NBAPlayerProps, NBATeamOdds

db = SessionLocal()

players = db.query(NBAPlayer).all()



db.close()



