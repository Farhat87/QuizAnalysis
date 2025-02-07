# 🌟 Quiz Performance Analysis

A Python-based data analysis pipeline that fetches quiz data, analyzes student performance, generates personalized recommendations, and predicts NEET ranks based on quiz scores.

---

## 📌 Project Overview  

This project retrieves quiz data from APIs, processes historical student performance, and provides actionable insights. The system is designed to help students track their progress, receive personalized recommendations, and predict their potential NEET rank.

### 🔥 **Key Features**  

✅ Fetches **current quiz** and **historical performance** data using APIs  
✅ Analyzes **student performance trends**  
✅ Generates **personalized recommendations**  
✅ Predicts **NEET rank** based on historical score trends  

---

## ⚙️ **Setup Instructions**  

### 🛠 Prerequisites  

Ensure you have **Python 3.7+** installed and the following dependencies:

```bash
pip install requests pandas scikit-learn
```

### 🚀 **Running the Project**  

1. Clone the repository:

```bash
git clone https://github.com/your-repo/quiz-analysis.git
cd quiz-analysis
```

2. Run the main script:

```bash
python main.py
```

3. Enter your **User ID** when prompted.

---

## 💽 **API Endpoints Used**  

- **Current Quiz Data:** [JSONKeeper API](https://www.jsonkeeper.com/b/LLQT)  
- **Quiz Submission Data:** [JSONServe API](https://api.jsonserve.com/rJvd7g)  
- **Historical Quiz Data:** [JSONServe API](https://api.jsonserve.com/XgAgFJ)  

---

## 🏗 **Project Approach**  

### 1️⃣ **Data Fetching**  
- Retrieves quiz, submission, and historical data from APIs.  
- Handles empty or invalid API responses with error messages.  

### 2️⃣ **Data Processing & Analysis**  
- Extracts user-specific quiz performance from fetched data.  
- Computes performance trends over time.  

### 3️⃣ **Generating Insights & Recommendations**  
- Identifies weak areas and suggests focus topics.  
- Highlights improvement trends.  

### 4️⃣ **NEET Rank Prediction**  
- Uses a **regression model** to predict NEET rank based on quiz scores.  
- Trains the model on past NEET performance data.  

---

## 📊 **Key Visualizations & Insights Summary**  

### 📌 **Performance Trends Over Time**
*(Attach a screenshot here, e.g., a line chart showing score trends.)*

### 📌 **Topic Weakness Analysis**
*(Attach a bar chart visualization of weak topics.)*

### 📌 **Predicted NEET Rank**  
```
🏅 Predicted NEET Rank: XXXXX
---

## ⚖️ **Future Improvements**  
🚀 Enhance the rank prediction model with **real-world NEET datasets**  
🚀 Add a **user-friendly dashboard** for better visualization  
🚀 Implement **adaptive quiz recommendations** based on weak areas  

---

## 🤝 **Contributing**  
Contributions are welcome! Feel free to fork this repo and submit a PR.  


