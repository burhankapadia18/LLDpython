from models.player import Player
from models.playing_piece.piece_o import PieceO
from models.playing_piece.piece_x import PieceX
from game import TicTacToeGame


def main():
    # creating 2 Players
    cross_piece = PieceX()
    player1 = Player("Player1", cross_piece)
    noughts_piece = PieceO()
    player2 = Player("Player2", noughts_piece)
    
    game = TicTacToeGame(3, [player1, player2])
    print("game winner is: " + game.start_game())


if __name__ == "__main__":
    main()