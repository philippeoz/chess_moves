from django.test import TestCase

from backend.core.models import Knight


class KnightModelTest(TestCase):

    def test_position_from_and_to_algebraic_notation(self):
        """
        Go test with corners:
            - Algebraic positions: 'Na8', 'Nh8', 'Na1', 'Nh1'
            - Matrix positions: (0, 0), (7, 0), (0, 7), (7, 7)
        """
        algebraic_corners = ['Na8', 'Nh8', 'Na1', 'Nh1']
        matrix_corners = [(0, 0), (7, 0), (0, 7), (7, 7)]
        for algebraic, matrix in zip(algebraic_corners, matrix_corners):
            self.assertEqual(
                Knight.position_from_algebraic_notation(algebraic),
                matrix
            )

            self.assertEqual(
                Knight.position_to_algebraic_notation(matrix),
                algebraic
            )
    
    def test_possible_moves_from_position(self):
        """
        Testing with two corners: 'Na8', 'Nh8'
        """
        expected_moves_from_Na8 = ['Nb6', 'Nc7']
        expected_moves_from_Nh8 = ['Nf7', 'Ng6']
        expected_moves_from_Na8.sort()
        expected_moves_from_Nh8.sort()
        
        moves_from_Na8 = list(Knight.possible_moves_from_position('Na8'))
        moves_from_Nh8 = list(Knight.possible_moves_from_position((7,0)))
        moves_from_Na8.sort()
        moves_from_Nh8.sort()

        self.assertEqual(moves_from_Na8, expected_moves_from_Na8)
        self.assertEqual(moves_from_Nh8, expected_moves_from_Nh8)
    
    def test_moves_tree_from_position(self):
        """
        testing with two turns from position Na8
        """
        expected_result = [
            {
                'from_position': 'Na8',
                'to_position': 'Nb6',
                'next_turn': [
                    {'from_position': 'Nb6', 'to_position': 'Na8'},
                    {'from_position': 'Nb6', 'to_position': 'Nc8'},
                    {'from_position': 'Nb6', 'to_position': 'Na4'},
                    {'from_position': 'Nb6', 'to_position': 'Nc4'},
                    {'from_position': 'Nb6', 'to_position': 'Nd7'},
                    {'from_position': 'Nb6', 'to_position': 'Nd5'}
                ]
            },
            {
                'from_position': 'Na8',
                'to_position': 'Nc7',
                'next_turn': [
                    {'from_position': 'Nc7', 'to_position': 'Nb5'},
                    {'from_position': 'Nc7', 'to_position': 'Nd5'},
                    {'from_position': 'Nc7', 'to_position': 'Na8'},
                    {'from_position': 'Nc7', 'to_position': 'Na6'},
                    {'from_position': 'Nc7', 'to_position': 'Ne8'},
                    {'from_position': 'Nc7', 'to_position': 'Ne6'}
                ],
            }
        ]

        result = Knight.moves_tree_from_position('Na8', turns=2)

        self.assertEqual(
            expected_result, result
        )
