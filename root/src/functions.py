import os
import streamlit as st
import pandas as pd
import re
from nltk.corpus import stopwords
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import numpy as np
import pickle
import plotly_express as px

# Functions
def create_keyfile_dict():
  variables_keys = {
    "type": os.getenv("TYPE"),
    "project_id": os.getenv("PROJECT_ID"),
    "private_key_id": os.getenv("PRIVATE_KEY_ID"),
    "private_key": os.getenv("PRIVATE_KEY"),
    "client_email": os.getenv("CLIENT_EMAIL"),
    "client_id": os.getenv("CLIENT_ID"),
    "auth_uri": os.getenv("AUTH_URI"),
    "token_uri": os.getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
  }
  return variables_keys

def saveData(email, completion, concentration, feedback, date, pre_med_stress, post_med_stress, db):
  # st.write([email, completion, concentration, feedback, date])
  db.collection("Meditation_Data").add({
    "email":email, "concentration":concentration,
    "completion":completion, "feedback": feedback,
    "date": date, "pre_med_stress": pre_med_stress,
    "post_med_stress" : post_med_stress
  })
  st.success("Data submitted Successfully.")

def saveScore(email, date, score, db):
  db.collection("Score_Data").add({
    "email":email,
    "date":date,
    "score":score
  })

# For sentiment analysis
TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    '''Removes HTML tags: replaces anything between opening and closing <> with empty space'''

    return TAG_RE.sub('', text)

def preprocess_text(sen):
    '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
    in lowercase'''
    
    sentence = sen.lower()

    # Remove html tags
    sentence = remove_tags(sentence)

    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)  # When we remove apostrophe from the word "Mark's", the apostrophe is replaced by an empty space. Hence, we are left with single character "s" that we are removing here.

    # Remove multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)  # Next, we remove all the single characters and replace it by a space which creates multiple spaces in our text. Finally, we remove the multiple spaces from our text as well.

    # Remove Stopwords
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    sentence = pattern.sub('', sentence)
    return sentence

def extractData(db):
  data = db.collection("Meditation_Data")
  docs = data.stream()
  database = pd.DataFrame(columns=["email", "date", "pre_med_stress", "concentration", "completion", "post_med_stress", "feedback"])
  for doc in docs:
    # st.write(doc.to_dict())
    database = database.append(doc.to_dict(), ignore_index=True)
  return database

def loadModel(model_path):
    from keras.models import load_model
    pretrained_lstm_model = load_model(model_path)
    return pretrained_lstm_model

def analyseFeedbacks(reviews):
    # database.to_csv("db.csv")
    # reviews = pd.read_csv("db.csv", index_col=[0])
    unseen_reviews = reviews['feedback']

    unseen_processed = []
    for review in unseen_reviews:
        review = preprocess_text(review)
        unseen_processed.append(review)

    # Tokenising instance with earlier trained tokeniser
    with open("./constants/model/tokeniser.pkl", "rb") as f:
      word_tokenizer = pickle.load(f)
    unseen_tokenized = word_tokenizer.texts_to_sequences(unseen_processed)

    # Pooling instance to have maxlength of 100 tokens
    maxlen = 100
    unseen_padded = pad_sequences(unseen_tokenized, padding='post', maxlen=maxlen)

    # Passing tokenised instance to the LSTM model for predictions
    lstm_model = loadModel("./constants/model/lstm_model_acc_0.868.h5")
    unseen_sentiments = lstm_model.predict(unseen_padded)
    reviews['Predicted Sentiments'] = np.round(unseen_sentiments*10,1)
    reviews['Sentiment'] = reviews['Predicted Sentiments'].apply(lambda x: "positve" if x >= 5 else "negative")
    reviews = reviews.drop(["date","pre_med_stress","concentration","completion","post_med_stress"], axis=1)
    return reviews

def interactivePlot(database, col):
  plot = px.bar(database, x = database['Sentiment'])
  plot.update_traces(marker=dict(color=col))
  st.plotly_chart(plot)
  
