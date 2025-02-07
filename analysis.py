import pandas as pd

def analyze_performance(quiz_data, historical_data):
    """Analyze student performance and identify weak areas."""
    quiz_df = pd.DataFrame(quiz_data)
    history_df = pd.DataFrame(historical_data)

    # Calculate accuracy per topic
    topic_performance = history_df.groupby("topic")["correct"].mean().sort_values()
    
    # Determine weak topics (accuracy < 50%)
    weak_topics = topic_performance[topic_performance < 0.5].index.tolist()

    # Analyze difficulty performance
    difficulty_performance = history_df.groupby("difficulty")["correct"].mean()

    # Improvement trends
    history_df["quiz_number"] = range(1, len(history_df) + 1)
    trend = history_df.groupby("quiz_number")["score"].mean()

    return {
        "weak_topics": weak_topics,
        "difficulty_performance": difficulty_performance.to_dict(),
        "trend": trend.to_dict()
    }

if __name__ == "__main__":
    sample_quiz_data = [
        {"question_id": 1, "topic": "Physics", "difficulty": "Hard", "correct": 0},
        {"question_id": 2, "topic": "Biology", "difficulty": "Medium", "correct": 1},
    ]
    sample_historical_data = [
        {"quiz_number": 1, "topic": "Physics", "difficulty": "Hard", "correct": 0, "score": 40},
        {"quiz_number": 2, "topic": "Biology", "difficulty": "Medium", "correct": 1, "score": 50},
    ]
    
    insights = analyze_performance(sample_quiz_data, sample_historical_data)
    print("Insights:", insights)
