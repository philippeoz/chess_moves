from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from backend.core.models import Knight


class IntegrationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_simple_possible_moves(self):
        expected_data = [
            {
                "from_position": "Na1", "to_position": "Nb3",
                "next_turn": [
                {"from_position": "Nb3", "to_position": "Na5"},
                {"from_position": "Nb3", "to_position": "Nc5"},
                {"from_position": "Nb3", "to_position": "Na1"},
                {"from_position": "Nb3", "to_position": "Nc1"},
                {"from_position": "Nb3", "to_position": "Nd4"},
                {"from_position": "Nb3", "to_position": "Nd2"}
                ]
            },
            {
                "from_position": "Na1", "to_position": "Nc2",
                "next_turn": [
                {"from_position": "Nc2", "to_position": "Nb4"},
                {"from_position": "Nc2", "to_position": "Nd4"},
                {"from_position": "Nc2", "to_position": "Na3"},
                {"from_position": "Nc2", "to_position": "Na1"},
                {"from_position": "Nc2", "to_position": "Ne3"},
                {"from_position": "Nc2", "to_position": "Ne1"}
                ]
            }
        ]

        payload = {
            "position": "Na1"
        }

        response = self.client.post(
            reverse('possible-moves'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.data)

    def test_get_simple_possible_moves_with_turns(self):
        expected_data = [
            {'from_position': 'Na1', 'to_position': 'Nb3', 'next_turn': [
                    {'from_position': 'Nb3', 'to_position': 'Na5'},
                    {'from_position': 'Nb3', 'to_position': 'Nc5'},
                    {'from_position': 'Nb3', 'to_position': 'Na1'},
                    {'from_position': 'Nb3', 'to_position': 'Nc1'},
                    {'from_position': 'Nb3', 'to_position': 'Nd4'},
                    {'from_position': 'Nb3', 'to_position': 'Nd2'}
                ]
            },
            {'from_position': 'Na1', 'to_position': 'Nc2', 'next_turn': [
                    {'from_position': 'Nc2', 'to_position': 'Nb4'},
                    {'from_position': 'Nc2', 'to_position': 'Nd4'},
                    {'from_position': 'Nc2', 'to_position': 'Na3'},
                    {'from_position': 'Nc2', 'to_position': 'Na1'},
                    {'from_position': 'Nc2', 'to_position': 'Ne3'},
                    {'from_position': 'Nc2', 'to_position': 'Ne1'}
                ]
            }
        ]

        payload = {
            "position": "Na1",
            "turns": 2
        }

        response = self.client.post(
            reverse('possible-moves'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.data)
    
    def test_get_simple_possible_moves_with_bigger_board(self):
        expected_data = [
            {
                "from_position": "Nj10",
                "to_position": "Ni8",
                "next_turn": [
                {"from_position": "Ni8", "to_position": "Nh10"},
                {"from_position": "Ni8", "to_position": "Nj10"},
                {"from_position": "Ni8", "to_position": "Nh6"},
                {"from_position": "Ni8", "to_position": "Nj6"},
                {"from_position": "Ni8", "to_position": "Ng9"},
                {"from_position": "Ni8", "to_position": "Ng7"}
                ]
            },
            {
                "from_position": "Nj10",
                "to_position": "Nh9",
                "next_turn": [
                {"from_position": "Nh9","to_position": "Ng7"},
                {"from_position": "Nh9","to_position": "Ni7"},
                {"from_position": "Nh9","to_position": "Nf10"},
                {"from_position": "Nh9","to_position": "Nf8"},
                {"from_position": "Nh9","to_position": "Nj10"},
                {"from_position": "Nh9","to_position": "Nj8"}
                ]
            }
        ]

        payload = {
            "position": "Nj10",
            "board_size": 10
        }

        response = self.client.post(
            reverse('possible-moves'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.data)