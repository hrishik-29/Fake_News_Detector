import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def remove_punct_and_numbers(text):
    if isinstance(text, str):
        text = re.sub(r'[^a-zA-Z\s]','',text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    else:
        return ""

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if not isinstance(text , str):
        return ""
    text = text.lower()
    text = remove_punct_and_numbers(text)
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word,pos='v') for word in tokens]
    return " ".join(tokens)