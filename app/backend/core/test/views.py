from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from backend.core.models import Knight


class IntegrationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_simple_possible_moves(self):
        expected_data = [
            {'from_position': 'Na1', 'to_position': 'Nb3'},
            {'from_position': 'Na1', 'to_position': 'Nc2'}
        ]

        payload = {
            "position": "Na1"
        }

        response = self.client.post(
            reverse('possible-moves'), payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(expected_data, response.data)
