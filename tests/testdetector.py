import unittest
from backend.detectorlogic import AdvancedAlgorithm

class TestPhishingLogic(unittest.TestCase):
    """
    Professional unit tests to ensure high code quality.
    """
    def setUp(self):
        self.algo = AdvancedAlgorithm()

    def test_ip_detection(self):
        """Checks if the algorithm flags numerical IP addresses."""
        features = self.algo.extract_features("http://192.168.1.1/login")
        self.assertEqual(features['has_ip'], 1)

    def test_length_feature(self):
        """Verifies URL length calculation."""
        url = "http://short.com"
        features = self.algo.extract_features(url)
        self.assertEqual(features['length'], len(url))

if __name__ == '__main__':
    unittest.main()