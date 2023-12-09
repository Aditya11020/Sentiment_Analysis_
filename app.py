from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk 
nltk.downloader.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        sentiment_score = sia.polarity_scores(text)['compound']
        sentiment_label = get_sentiment_label(sentiment_score)
        return render_template('index.html', text=text, sentiment_label=sentiment_label)

def get_sentiment_label(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':
    app.run(debug=True)
