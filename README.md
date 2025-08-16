# End-to-End Sentiment Analysis API (Docker & Kubernetes)

This project is a complete, full-stack **MLOps pipeline** that serves a sentiment analysis model as a scalable microservice.
It includes a Python backend, a containerized deployment managed by Kubernetes, and a user-friendly web interface for interaction.

This project is designed to showcase a **full development-to-deployment lifecycle**, demonstrating key skills in **AI, MLOps, and Cloud-Native technologies**.

---

## 🏛️ Architecture

The application consists of a **FastAPI backend** that serves a Hugging Face model.
This service is **containerized with Docker** and deployed on a **Kubernetes cluster** for high availability.
A **vanilla JavaScript frontend (index.html)** acts as a client to interact with the deployed API.

**Request Flow**:

```
User (Browser) → Frontend (index.html) → Kubernetes Service → Pod → Container (API)
```

---

## ✨ Key Features

* **FastAPI Backend**: A robust REST API for serving the AI model.
* **Dockerized Service**: The application is fully containerized for portability and consistency.
* **Kubernetes Deployment**: Managed by Kubernetes for scalability and self-healing.
* **Interactive Frontend**: A simple web UI to interact with the API without using the command line.
* **MLOps Pipeline**: A complete example of a model deployment pipeline.

---

## 🛠️ Tech Stack

* **Backend**: Python, FastAPI
* **Machine Learning**: Hugging Face Transformers
* **Containerization**: Docker
* **Orchestration**: Kubernetes
* **Frontend**: HTML, Tailwind CSS, JavaScript

---

## 🚀 Getting Started

### Prerequisites

* Git
* Docker Desktop with Kubernetes enabled
* ⚠️ Ensure Docker has **at least 4GB of memory** allocated (Settings > Resources > Advanced)

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api
```

### Step 2: Build the Image and Deploy to Kubernetes

```bash
# Build the image
docker build -t sentiment-api .

# Deploy the application
kubectl apply -f deployment.yaml -f service.yaml
```

✅ Wait \~1 minute for the pods to start.
Check status:

```bash
kubectl get pods
```

### Step 3: Use the Web Frontend

1. Find the API URL:

   ```bash
   kubectl get service sentiment-api-service
   ```

   Example → `http://localhost:31234`

2. Open **index.html** in your browser.

3. Paste the API URL → Type text → Click **"Analyze Sentiment"** 🎉

---

## 🧪 API Usage (via cURL)

**Endpoint**: `POST /analyze`

```bash
curl -X POST "http://localhost:31234/analyze" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is an amazing project!"}'
```

**Response**:

```json
{
  "label": "POSITIVE",
  "score": 0.9998
}
```

---

<details>
<summary><strong>Optional: Running Backend Locally (Without Docker)</strong></summary>

```bash
# Create venv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

</details>

---

## 📈 Future Improvements

* [ ] **CI/CD Pipeline**: Automate testing & deployment with GitHub Actions.
* [ ] **Cloud Deployment**: Deploy on GKE (Google Cloud) / EKS (AWS).
* [ ] **Monitoring**: Add Prometheus & Grafana for real-time monitoring.

---

## 👨‍💻 Author

Developed by **Zaid** 🚀
🔗 [LinkedIn](https://www.linkedin.com/in/zaidalam-cloud-ai/) | [GitHub](https://github.com/zaidnfs)

---
