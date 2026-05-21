# 🎬 CineMatch — AI Powered Movie Recommendation System

CineMatch is a modern full-stack movie recommendation platform that combines Machine Learning based recommendation systems with real-time movie metadata from TMDB.

The application provides:
- AI-powered movie recommendations
- Similar movie suggestions using TF-IDF cosine similarity
- Real-time movie search using TMDB API
- Genre-based recommendations
- Cinematic modern UI built using Streamlit
- FastAPI backend with scalable API architecture

---

# 🚀 Live Demo

## Frontend (Streamlit)
https://movie-recommendation-145.streamlit.app/

---

# 📌 Features

## 🎥 Movie Search
- Search movies dynamically
- TMDB-powered live suggestions
- Real-time poster loading

## 🤖 AI-Based Recommendations
- TF-IDF vectorization
- Cosine similarity recommendation engine
- Content-based filtering system

## 🎭 Genre Recommendations
- Similar movies from same genres
- Trending movies by category

## 🌑 Modern Cinematic UI
- Dark Netflix-inspired design
- Responsive movie cards
- Interactive browsing experience

## ⚡ Scalable Backend
- FastAPI REST APIs
- Async TMDB requests
- Optimized response handling

---

# 🛠️ Tech Stack

## Frontend
- Streamlit
- Custom CSS

## Backend
- FastAPI
- Uvicorn

## Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## Data Processing
- Pandas
- NumPy
- SciPy

## APIs
- TMDB API

## Deployment
- Streamlit Community Cloud
- Render

---

# 🧠 Recommendation System Architecture

The recommendation engine uses:

## TF-IDF Vectorization
Movie metadata such as:
- title
- genres
- keywords
- overview
- cast

are transformed into numerical vectors using TF-IDF.

## Cosine Similarity
Similarity between movies is computed using cosine similarity over sparse TF-IDF vectors.

---

# 📂 Project Structure

```bash
movie-recommendation/
│
├── app.py                     # Streamlit frontend
├── main.py                    # FastAPI backend
├── requirements.txt
├── runtime.txt
├── .python-version
│
├── df.pkl                     # Processed dataframe
├── tfidf.pkl                  # TF-IDF vectorizer
├── tfidf_matrix.pkl           # Sparse TF-IDF matrix
├── indices.pkl                # Movie title indices
│
├── movies_metadata.csv
├── movie_recommendations.ipynb
│
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/shubham-kumar145/movie-recommendations.git
cd movie-recommendations
```

---

# 📦 Create Virtual Environment

## Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# 📥 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Environment Variables

Create a `.env` file:

```env
TMDB_API_KEY=your_tmdb_api_key
```

Get your TMDB API key from:
https://www.themoviedb.org/settings/api

---

# ▶️ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# ▶️ Run Streamlit Frontend

Open a new terminal:

```bash
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# 📡 API Endpoints

# Health Check

```http
GET /health
```

---

# Home Feed

```http
GET /home
```

Query Params:
- category
- limit

---

# TMDB Search

```http
GET /tmdb/search
```

Query Params:
- query
- page

---

# Movie Details

```http
GET /movie/id/{tmdb_id}
```

---

# Genre Recommendations

```http
GET /recommend/genre
```

---

# TF-IDF Recommendations

```http
GET /recommend/tfidf
```

---

# Full Recommendation Bundle

```http
GET /movie/search
```

Returns:
- movie details
- TF-IDF recommendations
- genre recommendations

---

# 🧪 Machine Learning Pipeline

## Data Preprocessing
- Text cleaning
- Stopword removal
- Feature engineering

## Feature Extraction
- TF-IDF Vectorization

## Recommendation Engine
- Sparse matrix multiplication
- Cosine similarity ranking

---

# 🌐 Deployment

## Backend Deployment (Render)

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## Frontend Deployment (Streamlit)

Deploy using:
- Streamlit Community Cloud

Main file:
```bash
app.py
```

---

# 📷 Screenshots

## Home Page
- Trending Movies
- Search Suggestions
- Interactive Posters

## Movie Details
- Backdrop Hero Section
- Movie Overview
- Similar Recommendations

---

# 🔥 Future Improvements

- Collaborative Filtering
- User Authentication
- Watchlist System
- Personalized User Profiles
- Hybrid Recommendation System
- Deep Learning Recommendation Engine
- Redis Caching
- Recommendation Analytics Dashboard

---

# 👨‍💻 Author

## Shubham Kumar

### Connect With Me

- GitHub: https://github.com/shubham-kumar145
- LinkedIn: https://www.linkedin.com/in/shubham-kumar145/
- Portfolio: https://shubhamkumar.me

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like this project:
- Give it a ⭐ on GitHub
- Fork the repository
- Contribute improvements

---

# 🙌 Acknowledgements

- TMDB API
- FastAPI
- Streamlit
- Scikit-learn
- Render
- Open Source Community
