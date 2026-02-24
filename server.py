''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.

    To run the application, execute the command "python server.py" in the terminal.
    To run static code analysis, execute the command "pylint server.py" in the terminal.
'''

# Import Flask, render_template, request from the flask pramework
# package to create a web application and handle HTTP requests
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created:
from SentimentAnalysis import sentiment_analyzer

#Initiate the flask app :
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyse = request.args.get("textToAnalyze")

    result = sentiment_analyzer(text_to_analyse)
    # Check if the result is not None (i.e., the sentiment analysis was successful)
    if result is not None:
        # Return the sentiment label and confidence score as a response to the HTML interface
        return (
            f"The given text has been identified as {result['label']} "
            f"with a confidence score of {result['score']}"
        )

    # Return an error message if the sentiment analysis failed (i.e., result is None)
    return "Invalid input! Try again."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Render the index.html template as the main page of the application
    return render_template("index.html")

if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)

    # Run the Flask app with debug mode enabled for development purposes
    # app.run(debug=True)
