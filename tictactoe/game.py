from typing import Deque, List
from collections import deque
from models.player import Player
from models.board import Board
from models.playing_piece.piece import PieceType


class TicTacToeGame:
    players: Deque[Player]
    game_board: Board

    def __init__(self, size: int, players: List[Player]) -> None:
        self.game_board = Board(size)
        self.players = deque()
        for player in players:
            self.players.append(player)

    
    def start_game(self) -> str:

        no_winner = True
        while no_winner:

            # take out the player whose turn is and also put the player in the list back
            player_turn = self.players.popleft()

            # get the free space from the board
            self.game_board.print_board()
            freeSpaces =  self.game_board.get_free_cells()
            if len(freeSpaces) == 0:
                no_winner = False
                continue

            # read the user input
            s = input(f"Player:{player_turn.name} Enter row,column: ")
            values = s.split(',')
            row = int(values[0])
            col = int(values[1])

            # place the piece
            piece_added_successfully = self.game_board.add_piece(row,col, player_turn.playing_piece)
            if not piece_added_successfully:
                # player can not insert the piece into this cell, player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue
            
            self.players.append(player_turn)

            winner = self.is_there_winner(row, col, player_turn.playing_piece.piece_type)
            if winner:
                return player_turn.name

        return "tie"
    

    def is_there_winner(self, row: int, column: int, piece_type: PieceType) -> bool:

        rowMatch = True
        columnMatch = True
        diagonalMatch = True
        antiDiagonalMatch = True

        # need to check in row
        for i in range(self.game_board.size):
            if self.game_board.board[row][i] == None or self.game_board.board[row][i].piece_type != piece_type:
                rowMatch = False

        # need to check in column
        for i in range(self.game_board.size):
            if self.game_board.board[i][column] == None or self.game_board.board[i][column].piece_type != piece_type:
                columnMatch = False

        # need to check diagonals
        i, j = 0, 0
        while i<self.game_board.size:
            if self.game_board.board[i][j] == None or self.game_board.board[i][j].piece_type != piece_type:
                diagonalMatch = False
            i += 1
            j += 1

        # need to check anti-diagonals
        i, j = 0, self.game_board.size - 1
        while i < self.game_board.size:
            if self.game_board.board[i][j] == None or self.game_board.board[i][j].piece_type != piece_type:
                antiDiagonalMatch = False
            i += 1
            j -= 1

        return rowMatch or columnMatch or diagonalMatch or antiDiagonalMatch
