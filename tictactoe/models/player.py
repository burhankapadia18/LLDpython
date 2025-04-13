from .playing_piece.piece import Piece

class Player():
    name: str
    playing_piece: Piece
    
    def __init__(self,name: str, playing_piece: Piece) -> None:
        self.name = name
        self.playing_piece = playing_piece