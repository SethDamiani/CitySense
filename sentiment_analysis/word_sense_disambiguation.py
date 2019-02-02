from textblob import TextBlob
import json

def query(text):
    blob = TextBlob(text)
    return json.dumps({"pos_score": blob.sentences[0].sentiment.polarity})
