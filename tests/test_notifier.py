import unittest
from unittest.mock import patch
from notifier import send_notification

class TestNotifier(unittest.TestCase):
    @patch('notifier.send_notification')
    def test_send_notification(self, mock_send_notification):
        episode_details = {
            'title': 'New Episode',
            'description': 'Episode description',
            'link': 'https://example.com/episode'
        }
        send_notification(episode_details)
        mock_send_notification.assert_called_once_with(episode_details)

if __name__ == '__main__':
    unittest.main()