import unittest
from unittest.mock import patch
from bitsearch import search_episodes

class TestBitsearch(unittest.TestCase):
    def test_search_episodes(self):
        # Mock the response from Bitsearch
        mock_response = [
            {
                'title': 'Episode 1',
                'link': 'https://example.com/episode1'
            },
            {
                'title': 'Episode 2',
                'link': 'https://example.com/episode2'
            }
        ]
        
        # Mock the Bitsearch API call
        with patch('bitsearch.search') as mock_search:
            mock_search.return_value = mock_response
            
            # Call the function to be tested
            episodes = search_episodes('gibi')
            
            # Assert the expected results
            self.assertEqual(episodes, mock_response)
            mock_search.assert_called_once_with('gibi')

if __name__ == '__main__':
    unittest.main()