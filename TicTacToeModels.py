from flask_restplus import  fields

class TicTacToeModels:

    @staticmethod
    def gameInformationModel(api):
        game_information = api.model('Game Information', {
            'game_move': fields.Integer(required=True, description='Game move', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9])
        })
        return game_information

    @staticmethod
    def gameStartModel(api):
        game_start = api.model('Start Game', {
            'game_piece': fields.String(required=True, description='O or X', choices=["o", "x"])
        })
        return game_start
