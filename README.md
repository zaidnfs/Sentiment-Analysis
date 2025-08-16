# Sentiment Analysis API

This project is a **FastAPI-based Sentiment Analysis API** that uses Hugging Face's `transformers` library with a pre-trained model (`distilbert-base-uncased-finetuned-sst-2-english`) to classify text into **positive** or **negative** sentiments.

---

## 🚀 Features

* REST API built with **FastAPI**
* Uses Hugging Face `transformers` for NLP
* Dockerized for easy deployment
* Exposes API endpoint for sentiment prediction

---

## 📦 Installation

### 1. Clone the repository

```bash
 git clone https://github.com/your-username/sentiment-api.git
 cd sentiment-api
```

### 2. Install dependencies (for local development)

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

API will be available at:

```
http://127.0.0.1:8080
```

---

## 🐳 Running with Docker

### 1. Build Docker Image

```bash
docker build -t sentiment-api .
```

### 2. Run Docker Container

```bash
docker run -p 8080:80 sentiment-api
```

### 3. Configure Docker Resources (if needed)

If you face memory/CPU issues:

* Open **Docker Desktop** → **Settings** → **Resources**
* Increase **Memory (RAM)** and **CPUs**
* Restart Docker

---

## 🔥 API Usage

### Endpoint: `/predict`

**POST** request with JSON body:

```json
{
  "text": "I love this product!"
}
```

### Example cURL

```bash
curl -X POST http://127.0.0.1:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "This is amazing!"}'
```

### Example Response

```json
{
  "label": "POSITIVE",
  "score": 0.9991
}
```

---

## ⚙️ Environment Variables

If you want to specify a custom Hugging Face model:

```
MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english
```

---

## 📄 Requirements

See [requirements.txt](./requirements.txt) for dependencies.

---

## 🛠 Tech Stack

* **FastAPI**, **Python**
* **Transformers (Hugging Face)**
* **Docker**
* **Kubernetes**

---

## 📌 To-Do

* [ ] Add batch prediction
* [ ] Add multilingual model support
* [ ] Deploy on cloud (AWS/GCP/Azure)

---

## 👨‍💻 Author

Developed by **Zaid** 🚀
