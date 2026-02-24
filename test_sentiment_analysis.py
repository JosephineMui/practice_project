import unittest
from SentimentAnalysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        ''' This function tests the sentiment_analyzer function by providing a sample text input and checking if the output contains the expected keys (score and label) in the response.
        '''
        # Call the sentiment_analyzer function with the sample text
        result = sentiment_analyzer("I love working with Python")
        self.assertEqual(result["label"], "SENT_POSITIVE", "The sentiment label should be 'SENT_POSITIVE' for the input text.")
        
        result2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(result2["label"], "SENT_NEGATIVE", "The sentiment label should be 'SENT_NEGATIVE' for the input text.")
       
        result3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(result3["label"], "SENT_NEUTRAL", "The sentiment label should be 'SENT_NEUTRAL' for the input text.")
        
        # Print the result for verification
        print("Sentiment Analysis Result:", result)

if __name__ == '__main__':
    unittest.main()