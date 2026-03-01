import re
from urllib.parse import urlparse

class AdvancedAlgorithm:
    # Handles high-efficiency URL feature extraction.
    def extract_features(self, url: str) -> dict:
        # Professional logic using regex and parsing
        features = {
            'length': len(url),
            'has_ip': 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0,
            'subdomains': urlparse(url).netloc.count('.'),
            'special_chars': len(re.findall(r'[@-_?=%&]', url))
        }
        return features

    def calculate_risk(self, features: dict) -> float:
        #Logic-based scoring system (heuristic algorithm).
        score = 0
        if features['has_ip']: score += 50
        if features['subdomains'] > 3: score += 30
        if features['length'] > 75: score += 20
        if features['special_chars'] >= 2: score += 25
        return min(score, 100)