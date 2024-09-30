import unittest
from unittest.mock import patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src import main


class TestRealTimeTrafficNavigation(unittest.TestCase):

    def setUp(self):
        os.environ['TEST_MODE'] = '1'  # Setze die TEST_MODE-Umgebungsvariable für die Tests

    def tearDown(self):
        del os.environ['TEST_MODE']  # Entferne die TEST_MODE-Variable nach den Tests

    @patch('main.requests.get')
    def test_get_route_success(self, mock_get):
        mock_response = {
            'status': 'OK',
            'routes': [{
                'legs': [{
                    'distance': {'text': '401 km'},
                    'duration': {'text': '3 hours 44 mins'},
                    'start_address': 'Seoul, South Korea',
                    'end_address': 'Busan, South Korea',
                    'steps': [
                        {'html_instructions': 'Walk to Seoul Station'},
                        {'html_instructions': 'Take the train to Busan'}
                    ]
                }]
            }]
        }
        mock_get.return_value.json.return_value = mock_response

        route = main.get_route("Seoul, South Korea", "Busan, South Korea")
        self.assertIsNotNone(route)
        self.assertEqual(route['distance'], '401 km')
        self.assertEqual(route['duration'], '3 hours 44 mins')
        self.assertEqual(route['start_address'], 'Seoul, South Korea')
        self.assertEqual(route['end_address'], 'Busan, South Korea')

    @patch('main.requests.get')
    def test_get_route_zero_results(self, mock_get):
        mock_response = {
            'status': 'ZERO_RESULTS'
        }
        mock_get.return_value.json.return_value = mock_response

        route = main.get_route("Invalid City", "Nowhere")
        self.assertIsNone(route)

    @patch('main.requests.get')
    def test_get_route_request_denied(self, mock_get):
        mock_response = {
            'status': 'REQUEST_DENIED'
        }
        mock_get.return_value.json.return_value = mock_response

        route = main.get_route("Seoul, South Korea", "Busan, South Korea")
        self.assertIsNone(route)


if __name__ == '__main__':
    unittest.main()
