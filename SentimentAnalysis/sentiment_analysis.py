'''
Docstring for zzrjt-practice-project-emb-ai.SentimentAnalysis.sentiment_analysis
This module contains the sentiment_analyzer function that takes a text input and applies 
sentiment analysis using the Watson NLP API. The function returns the sentiment label and 
confidence score for the provided text.
'''
import json
import requests


URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
HEADERS = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }


def sentiment_analyzer(text_to_analyse):
    ''' This function takes the input text and applies sentiment analysis
        over it using the Watson NLP API. The output returned shows the 
        label and its confidence score for the provided text.
    '''
    # Create a payload with the input text and make a POST request to the Watson NLP API
    payload = {"raw_document": {"text": text_to_analyse}}
    # Make a POST request to the Watson NLP API with the payload and headers, and return the response
    # The headers are required to specify the model to be used for sentiment analysis. The response is 
    # returned in JSON format, which includes the sentiment label and confidence score for the input text.
    response = requests.post(URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        resp = json.loads(response.text)
        return {"score": resp["documentSentiment"]["score"], "label": resp["documentSentiment"]["label"]}
    else:
        return None
    
# Coursera's Solution
# import requests  # Import the requests library to handle HTTP requests

# def sentiment_analyzer(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
#     url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
#     myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
#     header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
#     response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
#     return response.text  # Return the response text from the API