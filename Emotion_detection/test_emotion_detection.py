import unittest
from unittest.mock import patch
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    @patch('emotion_detection.emotion_detection.requests.post')
    def test_joy(self, mock_post):
        # Mocking the response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotion": {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.96,
                "sadness": 0.01
            }
        }
        result = emotion_detector("I am very happy today")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch('emotion_detection.emotion_detection.requests.post')
    def test_sadness(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotion": {
                "anger": 0.01,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.01,
                "sadness": 0.96
            }
        }
        result = emotion_detector("I am very sad today")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch('emotion_detection.emotion_detection.requests.post')
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotion": {
                "anger": 0.96,
                "disgust": 0.01,
                "fear": 0.01,
                "joy": 0.01,
                "sadness": 0.01
            }
        }
        result = emotion_detector("I am very angry today")
        self.assertEqual(result["dominant_emotion"], "anger")

if __name__ == "__main__":
    unittest.main()
