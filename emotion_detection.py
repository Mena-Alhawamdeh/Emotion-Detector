import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the required format
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API with the text string
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion scores from the response structure
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']
    
    # Finding the dominant emotion (the one with the highest score)
    emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)
    
    # Returning the final formatted dictionary output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
