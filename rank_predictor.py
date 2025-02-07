import numpy as np
from sklearn.linear_model import LinearRegression

def train_rank_model(neet_data):
    """Train a regression model to predict NEET rank."""
    X = np.array(neet_data["quiz_scores"]).reshape(-1, 1)
    y = np.array(neet_data["neet_ranks"])

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_rank(model, quiz_score):
    """Predict rank based on quiz score."""
    return model.predict([[quiz_score]])[0]

if __name__ == "__main__":
    sample_neet_data = {
        "quiz_scores": [40, 50, 60, 70, 80],
        "neet_ranks": [50000, 40000, 30000, 20000, 10000]
    }

    model = train_rank_model(sample_neet_data)
    predicted_rank = predict_rank(model, 75)
    print(f"Predicted NEET Rank: {predicted_rank}")
