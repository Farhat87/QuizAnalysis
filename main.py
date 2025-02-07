from data_fetcher import fetch_quiz_data, fetch_historical_data
from analysis import analyze_performance
from recommendation import generate_recommendations
from rank_predictor import train_rank_model, predict_rank

def main(user_id):
    """Run the complete analysis pipeline for a student."""
    
    print("\n🚀 Fetching Quiz Data...")
    current_data = fetch_quiz_data(user_id)
    historical_data = fetch_historical_data(user_id)

    if not current_data or not historical_data:
        print("\n⚠️ Error: No quiz data found. Please check the API response.")
        return

    print("\n📊 Analyzing Student Performance...")
    insights = analyze_performance(current_data, historical_data)

    print("\n📌 Generating Recommendations...")
    recommendations = generate_recommendations(insights)

    print("\n--- 🏆 Personalized Recommendations ---")
    for rec in recommendations:
        print(f"✅ {rec}")

    # Predict NEET Rank
    print("\n🎯 Predicting NEET Rank...")
    sample_neet_data = {
        "quiz_scores": [40, 50, 60, 70, 80], 
        "neet_ranks": [50000, 40000, 30000, 20000, 10000]
    }
    model = train_rank_model(sample_neet_data)

    latest_score = insights["trend"].get(
        max(insights["trend"], key=insights["trend"].get, default=50), 50
    )
    predicted_rank = predict_rank(model, latest_score)

    print(f"\n🏅 Predicted NEET Rank: {int(predicted_rank)}")


if __name__ == "__main__":
    user_id = input("\n🆔 Enter User ID: ").strip()
    main(user_id)
