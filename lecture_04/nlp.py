# -*- coding: utf-8 -*-
"""
@author: BBarsch

There are several popular NLP libraries that can be used with pandas to perform natural language processing tasks. Here are a few examples:

NLTK (Natural Language Toolkit): NLTK is a popular open-source library for NLP in Python. It provides various modules for processing text, including tokenization, stemming, lemmatization, and part-of-speech tagging. NLTK can be used with pandas to preprocess text data and perform analysis.

SpaCy: SpaCy is another popular open-source library for NLP in Python. It provides various modules for processing text, including named entity recognition, dependency parsing, and text classification. SpaCy can be used with pandas to preprocess text data and perform analysis.

TextBlob: TextBlob is a Python library for processing textual data. It provides a simple API for common NLP tasks such as sentiment analysis, part-of-speech tagging, and noun phrase extraction. TextBlob can be used with pandas to preprocess text data and perform analysis.

Gensim: Gensim is a Python library for topic modeling, document indexing, and similarity retrieval with large corpora. It provides a simple API for creating and training topic models on text data. Gensim can be used with pandas to preprocess text data and create topic models.

Scikit-learn: Scikit-learn is a popular machine learning library in Python. It provides various modules for classification, regression, clustering, and dimensionality reduction. Scikit-learn can be used with pandas to preprocess text data and train machine learning models for NLP tasks such as text classification and sentiment analysis.

"""

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt') # download punkt tokenizer
nltk.download('stopwords') # download stopwords
nltk.download('wordnet') # download WordNet lemmatizer

# Load data into a pandas DataFrame
df = pd.read_csv('data/text.csv')

# Tokenize text data
df['tokens'] = df['text'].apply(nltk.word_tokenize)

# Perform part-of-speech tagging
df['pos_tags'] = df['tokens'].apply(nltk.pos_tag)

"""
This code uses NLTK to tokenize the text data and perform part-of-speech tagging on each token. The resulting DataFrame will have two additional columns: 'tokens' and 'pos_tags'.
"""

# Remove stopwords
stop_words = set(stopwords.words('english'))
df['filtered_text'] = df['tokens'].apply(lambda x: [word for word in x if word.lower() not in stop_words])

import spacy
nlp = spacy.load('en_core_web_sm')

# Define a function to extract keywords from text
def extract_keywords(text):
    doc = nlp(text)
    keywords = []
    for token in doc:
        if not token.is_stop and not token.is_punct and token.pos_ in ['NOUN', 'ADJ']:
            keywords.append(token.text)
    return keywords

df['keywords'] = df['text'].apply(extract_keywords)

# Define a function to get the top 5 keywords from a list of keywords
def get_top_keywords(keywords):
    keyword_counts = pd.Series(keywords).value_counts()
    if len(keyword_counts) < 5:
        return keyword_counts.index.tolist()
    else:
        return keyword_counts.head(5).index.tolist()
    
# Apply the function to the 'keywords' column and store the results in a new column
df['top_keywords'] = df['keywords'].apply(get_top_keywords)




