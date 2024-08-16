from django.db import models
from django.contrib.auth.models import User
import pickle
import joblib
import sklearn
from sklearn.preprocessing import LabelEncoder

# Create your models here.

class tree:
    model = None
    gender_encoder = LabelEncoder()
    genre_mapping = {
        1: 'HipHop',
        2: 'Jazz',
        3: 'Classical',
        4: 'Dance',
        5: 'Acoustic'
    }

    @classmethod
    def load_model(cls):
        if cls.model is None:
            cls.model = joblib.load(r'C:\Users\USER\Desktop\MUSIC GENRE\model\model\tree.pkl')
            # Load or fit the label encoder if needed
            cls.gender_encoder.fit(['male', 'female'])

    @staticmethod
    # Ensure the model is loaded
    def predict(age, gender):
        tree.load_model()

        # Preprocess the input
        gender_encoded = tree.gender_encoder.transform([gender])[0]
        features = [age, gender_encoded] 
        prediction_encoded = tree.model.predict([features])[0]
        prediction = tree.genre_mapping.get(prediction_encoded, 'Unknown Genre')

        return prediction
        


