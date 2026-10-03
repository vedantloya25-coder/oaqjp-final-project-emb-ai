# Emotion Detection Application with Watson NLP and Flask

An AI-based web application built with Python and Flask that performs Emotion Detection on user-submitted text using the IBM Watson NLP runtime service.

## Project Overview

This project was developed as the final project for the course **Developing AI Applications with Python and Flask** provided by IBM on Coursera / IBM Developer Skills Network.

The application analyzes user text input and calculates confidence scores across five primary emotions:
- **Anger**
- **Disgust**
- **Fear**
- **Joy**
- **Sadness**

It dynamically determines the **dominant emotion** (the emotion with the highest confidence score) and presents the formatted output to the user through a Flask web interface.

---

## Project Structure

```
├── EmotionDetection/
│   ├── __init__.py               # Package initializer exporting emotion_detector
│   └── emotion_detection.py      # Core logic calling Watson NLP API and formatting results
├── static/
│   └── mywebscript.js            # Frontend JavaScript sending asynchronous requests
├── templates/
│   └── index.html                # Frontend HTML user interface
├── evidence/                     # Evidence files and execution logs
├── requirements.txt              # Project dependencies
├── setup.py                      # Package installation and distribution script
├── server.py                     # Flask web server and routing application
├── test_emotion_detection.py     # Unit tests covering all 5 emotion categories
└── README.md                     # Project documentation
```

---

## Features

1. **Watson NLP Integration:** Communicates with the Watson NLP `EmotionPredict` endpoint using the `emotion_aggregated-workflow_lang_en_stock` model.
2. **Dynamic Dominant Emotion Calculation:** Computes the highest-scoring emotion among all five emotions.
3. **Modular Package Design:** Packaged under `EmotionDetection` with clean import mechanisms.
4. **Robust Error Handling:** Gracefully handles empty or blank inputs and status code 400 responses, returning appropriate error messages without crashing.
5. **Full Unit Testing:** Verified with `unittest` across representative statements for joy, anger, disgust, sadness, and fear.
6. **Code Quality:** Adheres strictly to PEP 8 standards with a perfect **10.00/10** score on `pylint`.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the package locally:**
   ```bash
   pip install -e .
   ```

---

## Running the Application

1. **Start the Flask server:**
   ```bash
   python server.py
   ```

2. **Access the application:**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Run Sentiment / Emotion Analysis:**
   Enter any text statement in the text area and click **Run Sentiment Analysis**.

---

## Running Unit Tests

Run the test suite using Python's built-in `unittest` framework:
```bash
python -m unittest test_emotion_detection.py
```

---

## Static Code Analysis

Run `pylint` on the server and application module:
```bash
pylint server.py EmotionDetection/emotion_detection.py
```
Expected score: **10.00/10**
