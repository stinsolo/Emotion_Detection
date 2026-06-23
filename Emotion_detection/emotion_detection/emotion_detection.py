import requests

def emotion_detector(text_to_analyze):
    """
    This function sends text to the Watson NLP Emotion Analyzer
    and returns a formatted response.
    """

    url = "https://sn-watson-emotion.labs.skills.network/emotion-analyzer/api/v1/analyze"

    headers = {"Content-Type": "application/json"}

    input_json = {
        "text": text_to_analyze
    }

    response = requests.post(url, headers=headers, json=input_json)
    
    # If the response status code is 400, the function should return None
    if response.status_code == 400:
        return None

    formatted_response = response.json()
    emotions = formatted_response["emotion"]

    # Calculate individual emotion scores
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # The function should also find the dominant emotion, which is the emotion with the highest score
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_list, key=emotion_list.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
