from TicTacToeGameEngine import TicTacToeGame
from TicTacToeDataBase import Game
import uuid

firstPlayerID = str(uuid.uuid4())
secondPlayerID = str(uuid.uuid4())
game = Game(firstPlayer=firstPlayerID,
                    secondPlayer=secondPlayerID,
                    gamePlan='000000000',
                    currentPlayer=firstPlayerID)

engine = TicTacToeGame()

game.gamePlan = '000XXX000'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = 'XXX000000'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '000000XXX'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = 'X00X00X00'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '0X00X00X0'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '00X00X00X'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = 'X000X000X'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '00X0X0X00'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '000OOO000'
t = engine.haveWeGotAWinner(game)

game.gamePlan = 'OOO000000'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '000000OOO'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = 'O00O00O00'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '0O00O00O0'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '00O00O00O'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = 'O000O000O'
t = engine.haveWeGotAWinner(game)
print(t)

game.gamePlan = '00O0O0O00'
t = engine.haveWeGotAWinner(game)
print(t)
