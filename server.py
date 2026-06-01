from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the input text for emotions and returns a formatted response string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)
    
    # Error handling for blank inputs (Task 7)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    return (
        f"For the given text the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main index page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)