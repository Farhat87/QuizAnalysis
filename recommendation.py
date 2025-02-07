def generate_recommendations(insights):
    """Provide personalized recommendations based on performance analysis."""
    weak_topics = insights["weak_topics"]
    difficulty_issues = insights["difficulty_performance"]

    recommendations = []

    if weak_topics:
        recommendations.append(f"Focus on these weak topics: {', '.join(weak_topics)}.")
    
    if difficulty_issues.get("Hard", 0) < 0.5:
        recommendations.append("Practice more hard-level questions to improve accuracy.")
    
    if insights["trend"][max(insights["trend"], key=insights["trend"].get)] > 50:
        recommendations.append("Your scores are improving! Keep up the momentum.")

    return recommendations

if __name__ == "__main__":
    sample_insights = {
        "weak_topics": ["Physics", "Chemistry"],
        "difficulty_performance": {"Easy": 0.9, "Medium": 0.6, "Hard": 0.3},
        "trend": {1: 40, 2: 45, 3: 50}
    }
    print(generate_recommendations(sample_insights))