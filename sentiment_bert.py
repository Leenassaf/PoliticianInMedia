from transformers import pipeline
import pandas as pd

data = pd.read_csv("Annotated.csv")
data['combined_text'] = data['title'].fillna('') + ' ' + data['description'].fillna('')

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
data['bert_sentiment'] = data['combined_text'].apply(lambda x: sentiment_pipeline(str(x))[0]['label'])

output_file = "annotated_with_bert_sentiments.csv"
data.to_csv(output_file, index=False)

print(f"BERT sentiment analysis completed. Results saved to '{output_file}'.")
