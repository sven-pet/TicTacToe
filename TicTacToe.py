from flask import Flask
from flask_restplus import Resource, Api
from TicTacToeParsers import *
from TicTacToeModels import *
from TicTacToeBaseDatabase import db
from TicTacToeGameEngine import TicTacToeGame

'''
1. One user creates a new game. Do this with 
2. User selects X or O
3. User gets unique url to the game
4. User can invite other player by sending the game url
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlalchemy_example.db'
db.init_app(app)
api = Api(app)
#app.app_context().push()
with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    db.create_all()


@api.route('/tictactoe/create')
class TicTacToe(Resource):

    @api.expect(TicTacToeModels.gameStartModel(api), validate=True)
    def post(self):
        parser = TicTacToeParsers.gameStartParser()
        args = parser.parse_args(strict=True)
        game = TicTacToeGame()
        result = game.createGame(db, args)
        return result,200

@api.route('/tictactoe/<int:gameid>')
class TicTacToe(Resource):
    def get(self,gameid):
        game = TicTacToeGame()
        result = game.getGame(db,gameid)
        return result,200

@api.route('/tictactoe')
class TicTacToe(Resource):
    def get(self):
        game = TicTacToeGame()
        result = game.getAllGames(db)
        return result,200

@api.route('/tictactoe/<int:gameid>/<string:player>')
class TicTacToe(Resource):

    @api.expect(TicTacToeModels.gameInformationModel(api), validate=True)
    def put(self,gameid,player):
        parser = TicTacToeParsers.gameParser()
        args = parser.parse_args(strict=True)
        game = TicTacToeGame()
        result = game.putGame(db, gameid,player,args)
        return result, 201

if __name__ == '__main__':
    app.run(debug=True)
