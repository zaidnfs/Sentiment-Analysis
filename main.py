from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# 1. Create a FastAPI app instance
app = FastAPI()

# 2. Load the sentiment analysis model from Hugging Face
# This will download the model on the first run
sentiment_pipeline = pipeline("sentiment-analysis")

# 3. Define the request model using Pydantic
# This ensures the input data is a string
class TextToAnalyze(BaseModel):
    text: str

# 4. Define the prediction endpoint
@app.post("/analyze")
def analyze_sentiment(data: TextToAnalyze):
    # Run the sentiment analysis pipeline on the input text
    result = sentiment_pipeline(data.text)
    # Return the result
    return result[0]

# A simple root endpoint to check if the API is running
@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API is running!"}