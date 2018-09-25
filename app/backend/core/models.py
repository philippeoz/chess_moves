from django.db import models

from django.conf import settings

from string import ascii_uppercase, ascii_lowercase


class ChessPiece(models.Model):
    """Model definition for ChessPiece."""
    ALGEBRAIC_NOTATION = ''
    MOVES = ()

    CHESS_PIECES = [
        'K', # King
        'Q', # Queen
        'N', # Knight
        'B', # Bishop
        'R', # Rook
        'P', # Pawn
    ]

    class Meta:
        """Meta definition for ChessPiece."""

        verbose_name = 'ChessPiece'
        verbose_name_plural = 'ChessPieces'
        abstract = True

    def __str__(self):
        """Unicode representation of ChessPiece."""
        pass

    @classmethod
    def position_from_algebraic_notation(cls, algebraic_position):
        """
        This method translate simple algebric position notation to
        matrix notation.
        
            >>> # Be5 (bishop on e5)
            >>> ChessPiece.translate_from_algebraic_notation('Be5')
            >>> (4, 3)
        """
        algebraic_position = algebraic_position.upper()

        if not isinstance(
                algebraic_position, str) or len(algebraic_position) < 3:
            raise Exception('Invalid position.')
        if algebraic_position[0] not in cls.CHESS_PIECES:
            raise Exception('Invalid Chess Piece.')
        return (
            ascii_uppercase.index(algebraic_position[1]),
            settings.BOARD_SIZE - int(algebraic_position[2:])
        )
    
    @classmethod
    def position_to_algebraic_notation(cls, matrix_position):
        """
        This method translate simple matrix position notation to
        algebraic notation.
        
            >>> # (4, 3) (Bishop on e5)
            >>> Bishop.translate_from_algebraic_notation('Be5')
            >>> 'Be5'
        """
        if not isinstance(matrix_position, tuple) \
                or len(matrix_position) != 2:
            raise Exception('Please, use a tuple with len == 2.')
        
        col, line = matrix_position
        if matrix_position[0] < len(ascii_lowercase):
            col = ascii_lowercase[col]
        line = settings.BOARD_SIZE - line
        return f"{cls.ALGEBRAIC_NOTATION}{col}{line}"

    @classmethod
    def possible_moves_from_position(cls, position):
        """
        This method returns all possible simple moves from specific position

            >>> # Knight possible moves pro position 'Nd4'
            >>> list(Knight.possible_moves_from_position('Nd4'))
            >>> ['Nc6', 'Ne6', 'Nc2', 'Ne2', 'Nb5', 'Nb3', 'Nf5', 'Nf3']
        """

        if isinstance(position, str):
            position = cls.position_from_algebraic_notation(position)
        
        col_position, row_position = position

        for col_move, row_move in cls.MOVES:
            col, row = col_position + col_move, row_position + row_move
            if settings.BOARD_SIZE > col >= 0 <= row < settings.BOARD_SIZE:
                yield cls.position_to_algebraic_notation((col, row))
    
    @classmethod
    def moves_tree_from_position(cls, position, turns=1):
        if isinstance(position, str):
            position = cls.position_from_algebraic_notation(position)

        moves = [
            {
                'from': cls.position_to_algebraic_notation(position),
                'to': move
            } for move in list(cls.possible_moves_from_position(position))
        ]
        if turns > 1:
            for move in moves:
                move['next_turn'] = cls.moves_tree_from_position(
                    cls.position_from_algebraic_notation(move['to']),
                    turns=turns - 1
                )
        return moves


class Knight(ChessPiece):
    """Model definition for Knight."""
    ALGEBRAIC_NOTATION = 'N'
    MOVES = (
        (-1, -2), (1, -2), # back
        (-1, 2), (1, 2), # front
        (-2, -1), (-2, 1), # left
        (2, -1), (2, 1), # right
    )

    class Meta:
        """Meta definition for Knight."""

        verbose_name = 'Knight'
        verbose_name_plural = 'Knights'
        abstract = True

    def __str__(self):
        """Unicode representation of Knight."""
        pass
