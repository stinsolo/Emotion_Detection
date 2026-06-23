"""
Server module for Emotion Detection Application.
"""

from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle emotion detection request from user.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    
    if not text_to_analyze:
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!", 400

    # Format the response as per requirement
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
