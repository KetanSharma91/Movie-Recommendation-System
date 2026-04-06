# 🎬 Movie Recommendation System

## 📌 Overview

This project builds a **Movie Recommendation System** using both:

* 🎯 **Content-Based Filtering**
* 🤝 **Collaborative Filtering (SVD)**

The goal is to recommend movies based on:

* Movie content (genres + tags)
* User behavior (ratings)

---

## 🚀 Features

* Recommend similar movies based on content
* Predict user preferences using collaborative filtering
* Evaluate model performance using RMSE & Precision@K
* SQL-based data analysis
* Streamlit web app for interaction

👉 Live App: **[[movierecommendsystemket.streamlit.app]](https://movierecommendsystemket.streamlit.app/)**

---

## 📂 Dataset

We used the **MovieLens dataset**, which includes:

* `movies.csv` → movie titles & genres
* `ratings.csv` → user ratings
* `tags.csv` → user-generated tags

---

## 🧠 How the System Works

### 1. Content-Based Filtering

We combine:

* Genres
* Tags

Then convert them into numerical form using **TF-IDF**.

👉 After that, we compute similarity using **Cosine Similarity**

💡 Idea:

> Movies with similar content (genre + tags) are recommended

---

### 2. Collaborative Filtering (SVD)

We use **Singular Value Decomposition (SVD)** to learn user preferences.

💡 Idea:

> Users who liked similar movies will get similar recommendations

---

## ❓ Why SVD instead of Random Forest?

### ❌ Random Forest Problems

* Not designed for recommendation systems
* Cannot handle sparse user-movie matrix well
* Doesn’t learn hidden patterns (latent features)

### ✅ SVD Advantages

* Works well with sparse data
* Learns hidden relationships between users and movies
* Industry standard for recommender systems

👉 That’s why we use **SVD instead of Random Forest**

---

## 📊 Evaluation Metrics

### 🔹 RMSE (Root Mean Square Error)

Measures how close predicted ratings are to actual ratings.

💡 Lower RMSE = Better model

Example:

* Predicted: 4.5
* Actual: 5
  👉 Small error → good prediction

---

### 🔹 Precision@K

Measures how good top recommendations are.

💡 Example:
If 3 out of 5 recommended movies are relevant:
👉 Precision@5 = 0.6

---

## 🗄️ SQL Analysis

We performed SQL queries to analyze data:

* Top rated movies
* Most active users
* Most popular movies
* Movie rating distribution

👉 This shows real-world data handling skills

---

## 💾 Model Deployment (Pickle)

We saved the model using **pickle**:

* Avoids recomputing everything
* Makes app faster
* Enables easy deployment

---

## 🌐 What is Streamlit?

**Streamlit** is a Python library used to create web apps easily.

👉 It allows:

* User input (movie name)
* Display recommendations
* Interactive UI

---

## 🎬 Streamlit App Workflow

1. Load saved model (pickle)
2. Take user input
3. Generate recommendations
4. Display results

---

## 🧱 Project Structure

```
project/
│
├── notebook.ipynb
├── app.py
├── model.pkl
├── movies.csv
├── ratings.csv
├── tags.csv
```

---

## 💼 Resume Description

Built a hybrid movie recommendation system using content-based filtering (TF-IDF + cosine similarity) and collaborative filtering (SVD), evaluated using RMSE and Precision@K, with SQL-based data analysis and Streamlit deployment.

---

## 🚀 Future Improvements

* Add movie posters using TMDB API
* Improve hybrid recommendation system
* Use deep learning models
* Deploy on cloud (AWS / Render)

---

## 🙌 Conclusion

This project demonstrates:

* Recommender system design
* Machine learning concepts
* Data processing & evaluation
* Deployment skills

---

## ⭐ One-line Summary

👉 This system recommends movies using both **what the movie is about** and **what users like**

---

## 🔗 Links

* Notebook: **[[MovieRecommendations.ipynb]]([https://movierecommendsystemket.streamlit.app/](https://github.com/KetanSharma91/Movie-Recommendation-System/blob/main/MovieRecommendations.ipynb))**
* Streamlit App: **[[movierecommendsystemket.streamlit.app]](https://movierecommendsystemket.streamlit.app/)**

---
