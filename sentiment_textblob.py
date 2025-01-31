import pandas as pd
from textblob import TextBlob


data = pd.read_csv("Annotated.csv")
data['combined_text'] = data['title'].fillna('') + ' ' + data['description'].fillna('')


def get_sentiment_category(text):
    blob = TextBlob(str(text))  
    polarity = blob.sentiment.polarity
    if polarity > 0.1: 
        return 'Positive'
    elif polarity < -0.1:  
        return 'Negative'
    else: 
        return 'Neutral'

data['combined_sentiment'] = data['combined_text'].apply(get_sentiment_category)

output_file = "annotated_with_combined_sentiments.csv"
data.to_csv(output_file, index=False)

print(f"Sentiment analysis completed for combined text. Results saved to '{output_file}'.")
