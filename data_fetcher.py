import requests
import pandas as pd

# API Endpoints
QUIZ_ENDPOINT = "https://www.jsonkeeper.com/b/LLQT"
QUIZ_SUBMISSION_ENDPOINT = "https://api.jsonserve.com/rJvd7g"
HISTORICAL_ENDPOINT = "https://api.jsonserve.com/XgAgFJ"

def fetch_data(url):
    """Fetch data from an API endpoint with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        if not response.text.strip():
            print(f"⚠️ Error: Empty response from {url}")
            return None

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request Error: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"⚠️ Error: API did not return valid JSON from {url}")
        print(f"⚠️ Response Text: {response.text}")
        return None

def fetch_quiz_data(user_id):
    """Fetch and filter quiz data based on user_id."""
    data = fetch_data(QUIZ_ENDPOINT)
    
    if data is None:
        return None
    
    if isinstance(data, list):  # Check if data is a list of quizzes
        user_quiz = [quiz for quiz in data if str(quiz.get("id")) == str(user_id)]
        return user_quiz if user_quiz else None
    
    return data  # If not a list, return as-is

def fetch_quiz_submission_data():
    """Fetch quiz submission data."""
    return fetch_data(QUIZ_SUBMISSION_ENDPOINT)

def fetch_historical_data(user_id):
    """Fetch and filter historical data based on user_id."""
    data = fetch_data(HISTORICAL_ENDPOINT)
    
    if data is None:
        return None
    
    if isinstance(data, list):  
        user_history = [record for record in data if str(record.get("user_id")) == str(user_id)]
        return user_history if user_history else None
    
    return data  

if __name__ == "__main__":
    # Get user ID
    user_id = input("\n🆔 Enter User ID: ").strip()

    # Fetch data for the user
    current_quiz_data = fetch_quiz_data(user_id)
    quiz_submission_data = fetch_quiz_submission_data()
    historical_data = fetch_historical_data(user_id)

    # Debugging: Print fetched data
    print("\n✅ Current Quiz Data:")
    print(pd.DataFrame(current_quiz_data).head() if current_quiz_data else "No Data Available")

    print("\n✅ Quiz Submission Data:")
    print(pd.DataFrame(quiz_submission_data).head() if isinstance(quiz_submission_data, list) else quiz_submission_data)

    print("\n✅ Historical Data:")
    print(pd.DataFrame(historical_data).head() if historical_data else "No Data Available")
