from sqlalchemy import Column, Integer, String
from TicTacToeBaseDatabase import db

class Game(db.Model):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    firstPlayer = Column(String(50), unique=True)
    secondPlayer = Column(String(50), unique=True)
    gamePlan = Column(String(9))
    currentPlayer = Column(String(50), unique=True)
    winner = Column(String(50), unique=True)

    def __repr__(self):
        return '<Game %r>' % (self.id)