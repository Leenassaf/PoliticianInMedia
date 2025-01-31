import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# Preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#|\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Interpret compound scores
def interpret_sentiment(compound):
    if compound >= 0.5:
        return 'Strong Positive'
    elif 0.1 <= compound < 0.5:
        return 'Positive'
    elif -0.1 < compound < 0.1:
        return 'Neutral'
    elif -0.5 <= compound <= -0.1:
        return 'Negative'
    else:
        return 'Strong Negative'

# Load the dataset
data = pd.read_csv("Annotated.csv")

# Combine and preprocess text
data['combined_text'] = (data['title'].fillna('') + ' ' + data['description'].fillna('')).apply(preprocess_text)

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Add custom words to the lexicon
# analyzer.lexicon.update({
#     "fake news": -3.0,
#     "excellent": 2.5,
#     "terrible": -2.5,
#     "unprecedented": 1.5,
#     "disaster": -3.0
# })

# Analyze sentiment
data['vader_sentiment'] = data['combined_text'].apply(
    lambda x: interpret_sentiment(analyzer.polarity_scores(x)['compound'])
)

# Save results
output_file = "annotated_with_improved_vader_sentiments.csv"
data.to_csv(output_file, index=False)

print(f"Improved VADER sentiment analysis completed. Results saved to '{output_file}'.")
