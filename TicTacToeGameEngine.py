import uuid
import json
from TicTacToeDataBase import Game
from HelpFunctions import AlchemyEncoder


class TicTacToeGame:

    def getAllGames(self,db):
        game = db.session.query(Game).all()
        return json.dumps(game, cls=AlchemyEncoder)

    def createGame(self,db,args):


        firstPlayerID = str(uuid.uuid4())
        secondPlayerID = str(uuid.uuid4())
        game = Game(firstPlayer=firstPlayerID,
                    secondPlayer=secondPlayerID,
                    gamePlan='000000000',
                    currentPlayer=firstPlayerID,
                    winner = "")
        db.session.add(game)
        db.session.commit()

        return self.resultDict(game,'ok','Game Created', args['game_piece'])

    def getGame(self,db,game_id):
        game = db.session.query(Game).filter_by(id=game_id).first()
        if( game == None):
            result = {}
            result['status'] = 'nok'
            result['message'] = 'No game with that id'
            return result
        else:
            if (game.winner != ""):
                return self.resultDict(game, 'won', 'Game Won')
            return self.resultDict(game, 'ok', 'Game Returned')

    def putGame(self,db,game_id,player,args):
        game = db.session.query(Game).filter_by(id=game_id).first()

        if game.currentPlayer == player:
            move = args['game_move'] -1
            if game.gamePlan[move] == "0":
                if game.firstPlayer == player:
                    game.currentPlayer = game.secondPlayer
                    newString = list(game.gamePlan)
                    newString[move] = 'X'
                    game.gamePlan = ''.join(newString)

                else:
                    newString = list(game.gamePlan)
                    newString[move] = 'O'
                    game.gamePlan = ''.join(newString)
                    game.currentPlayer = game.firstPlayer
                db.session.commit()

                if self.haveWeGotAWinner(game):
                    game.winner = game.currentPlayer
                    db.session.commit()
                    return self.resultDict(game, 'won', 'Game Won')

                return self.resultDict(game, 'ok', 'Game Board Updated')

            else:
                return self.resultDict(game, 'nok', 'That place is already taken')
        return self.resultDict(game, 'nok', 'It is not your turn')



    def resultDict(self,game,status="ok",message="default",choosen_peice =''):
        result = {}
        result['first Player'] = game.firstPlayer
        result['second player'] = game.secondPlayer
        if (choosen_peice == 'X' or choosen_peice == 'x'):
            result['game_url'] = "http://127.0.0.1:5000/tictactoe/" + str(game.id) + "/" + game.secondPlayer
        else:
            if(choosen_peice == 'O' or choosen_peice == 'o'):
                result['game_url'] = "http://127.0.0.1:5000/tictactoe/" + str(game.id) + "/" + game.firstPlayer
        result['current_player'] = game.currentPlayer
        result['winner'] = game.winner
        result['gameboard'] = game.gamePlan
        result['status'] = status
        result['message'] = message
        return result

    def haveWeGotAWinner(self,game):
        board = str(game.gamePlan)

        if (board[0:3] == 'XXX' or
                    board[3:6] == 'XXX' or
                    board[6:9] == 'XXX' or
                    board[0] + board[3] + board[6] == 'XXX' or
                    board[1] + board[4] + board[7] == 'XXX' or
                    board[2] + board[5] + board[8] == 'XXX' or
                    board[0] + board[4] + board[8] == 'XXX' or
                    board[2] + board[4] + board[6] == 'XXX'
            ):
            return True

        if (board[0:3] == 'OOO' or
                    board[3:6] == 'OOO' or
                    board[6:9] == 'OOO' or
                    board[0] + board[3] + board[6] == 'OOO' or
                    board[1] + board[4] + board[7] == 'OOO' or
                    board[2] + board[5] + board[8] == 'OOO' or
                    board[0] + board[4] + board[8] == 'OOO' or
                    board[2] + board[4] + board[6] == 'OOO'
            ):
            return True

        return False
