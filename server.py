"""
Executing this function initiates the application of emotion
detector to be deployed over the Flask server.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the input text and returns formatted result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None (status code 400 or invalid input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores and dominant emotion from response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return formatted string
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
