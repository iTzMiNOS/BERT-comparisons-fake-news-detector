import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from transformers import pipeline

nltk.download('stopwords')
en_sw = stopwords.words('english')

st.title("BERT Comparisons (DistilBERT, MobileBERT, TinyBERT)")

st.subheader("Fake News Detection")

models = {
    "DistilBERT": "iTzMiNOS/distilbert-uncased-fake-news-detector",
    "MobileBERT": "iTzMiNOS/mobilebert-uncased-fake-news-detector",
    "TinyBERT": "iTzMiNOS/tinybert-uncased-fake-news-detector"
}

model_choice = st.radio("Select Classifier:", list(models.keys()))

if 'classifier' not in st.session_state or st.session_state['classifier_model'] != model_choice:
    model_name = models[model_choice]
    st.session_state['classifier'] = pipeline('text-classification', model=model_name)
    st.session_state['classifier_model'] = model_choice

text = st.text_area("Enter News Here:", placeholder="Start Typing...")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"([^\s\w])", "", text)
    text = ' '.join([word for word in text.split() if word not in en_sw])
    return text

if st.button("Predict"):
    processed_text = preprocess_text(text)

    result = st.session_state['classifier'](processed_text)
    
    st.markdown("## Result: " + result[0]['label'])
    st.markdown("#### Accuracy: %" + str(round(result[0]['score'] * 100, 1)))
