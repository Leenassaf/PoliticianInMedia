import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')
stop_words = list(stopwords.words('english'))

file_path = 'Annotated.csv'
data = pd.read_csv(file_path)


data['text'] = data['title'] + ' ' + data['description']
data = data.dropna(subset=['annotation', 'text'])
grouped_data = data.groupby('annotation')['text'].apply(lambda x: ' '.join(x))

vectorizer = TfidfVectorizer(stop_words=stop_words, max_features=5000)
tfidf_matrix = vectorizer.fit_transform(grouped_data)
feature_names = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_matrix.T.toarray(), index=feature_names, columns=grouped_data.index)
top_words = {category: tfidf_df[category].nlargest(10).index.tolist() for category in grouped_data.index}

output_file_path = 'top_words_no_stopwords.txt'

with open(output_file_path, 'w') as file:
    for category, words in top_words.items():
        file.write(f"Category: {category}\n")
        file.write(", ".join(words) + "\n\n")

print(f"Top words for each category (stopwords removed) have been written to {output_file_path}")
