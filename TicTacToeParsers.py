from flask_restplus import reqparse

class TicTacToeParsers:

    @staticmethod
    def gameParser():
        parser = reqparse.RequestParser()
        parser.add_argument('game_move', type=int, help='Choose this place', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9] )
        return parser

    @staticmethod
    def gameStartParser():
        parser = reqparse.RequestParser()
        parser.add_argument('game_piece', type=str,
                            help='You can either choice X or O'
                            , choices=["o", "x", "O", "X"])
        return parser