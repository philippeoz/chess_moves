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
        moves_from_Na8 = ['Nb6', 'Nc7']
        moves_from_Nh8 = ['Nf7', 'Ng6']
        
        self.assertEqual(
            list(Knight.possible_moves_from_position('Na8')).sort(),
            moves_from_Na8.sort()
        )

        # Test with a tuple
        self.assertEqual(
            list(Knight.possible_moves_from_position((7, 0))).sort(),
            moves_from_Na8.sort()
        )
    
    def test_moves_tree_from_position(self):
        """
        testing with two turns from position Na8
        """
        expected_result = [
            {
                'from': 'Na8',
                'to': 'Nb6',
                'next_turn': [
                    {'from': 'Nb6', 'to': 'Na8'},
                    {'from': 'Nb6', 'to': 'Nc8'},
                    {'from': 'Nb6', 'to': 'Na4'},
                    {'from': 'Nb6', 'to': 'Nc4'},
                    {'from': 'Nb6', 'to': 'Nd7'},
                    {'from': 'Nb6', 'to': 'Nd5'}
                ]
            },
            {
                'from': 'Na8',
                'to': 'Nc7',
                'next_turn': [
                    {'from': 'Nc7', 'to': 'Nb5'},
                    {'from': 'Nc7', 'to': 'Nd5'},
                    {'from': 'Nc7', 'to': 'Na8'},
                    {'from': 'Nc7', 'to': 'Na6'},
                    {'from': 'Nc7', 'to': 'Ne8'},
                    {'from': 'Nc7', 'to': 'Ne6'}
                ],
            }
        ]

        result = Knight.moves_tree_from_position('Na8')

        def get_key_value_lists(dict_list):
            for move in expected_result:
                next_turn = move.get('next_turn', None)
                if next_turn is not None:
                    next_turn = get_key_value_lists(
                        move.pop('next_turn')
                    )
                else:
                    next_turn = []
                yield (
                    list(move.keys()).sort(),
                    list(move.values()).sort(),
                    list(next_turn).sort(),
                )

        self.assertEqual(
            list(get_key_value_lists(expected_result)).sort(),
            list(get_key_value_lists(result)).sort()
        )
