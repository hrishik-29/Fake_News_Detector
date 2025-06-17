import streamlit as st
import joblib

from text_preprocessing_code import preprocess_text

try:
    nb_model = joblib.load('naive_bayes_model.pkl')
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
except FileNotFoundError:
    st.error("Error: Model or Vectorizer files not found.Make sure 'naive_bayes_model.pkl' and 'tfidf_vectorizer.pkl' are in the same directory as x_'app.py'.")
    st.stop()

st.set_page_config(page_title="Fake News Detector",page_icon ="🚨")
st.title("Fake News Detector")
st.markdown("Enter a news article's content below to check if it's likely fake or real. This model uses a Naive Bayes classifier trained on various news articles.")
user_input = st.text_area("Paste the Article Here :",height=300,placeholder="Type or paste the news article content here...")

if st.button('Predict') :
    if user_input:
        processed_input = preprocess_text(user_input)
        if not processed_input.strip():
            st.warning("The inputtext was processed but resulted in empty content.Please try again with different text.")
        else:
            input_tfidf = tfidf_vectorizer.transform([processed_input])
            prediction = nb_model.predict(input_tfidf)
            if(prediction[0] == 'fake') :
                st.error("Result : This news article is likely **FAKE NEWS** 🚨")
            else:
                st.success("Result: This news article is likely **REAL NEWS** ✅")
    else:
        st.warning("The text area seems to be empty ,please paste some content into the text area to make a prediction")
