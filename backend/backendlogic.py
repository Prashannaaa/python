import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class PhishingBackend: 
    def __init__(self, engine): 
        """
        Standardizes the backend initialization. 
        Accepts 1 argument: 'engine' (the AdvancedAlgorithm instance).
        """
        self.engine = engine

    def analyze_url(self, url: str) -> str:
        # Use the engine to perform the heavy lifting
        features = self.engine.extract_features(url)
        risk = self.engine.calculate_risk(features)
        
        if risk >= 50:
            return "DANGER: High Phishing Risk"
        return "SAFE: Low Risk"
