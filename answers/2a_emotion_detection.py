"""
Emotion Detection module using Watson NLP EmotionPredict service.
Task 2a: Initial function - returns raw response text.
"""
import requests


def emotion_detector(text_to_analyse):
    """
    Analyzes the input text using Watson NLP EmotionPredict API.
    Returns the raw response text.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    return response.text
