# Fake_News_detector

## Project Description
This project develops a machine learning model capable of classifying news articles as either authentic or fabricated (fake). Built to address the pervasive issue of misinformation, the system processes textual news content to provide an automated verification mechanism. It showcases an end-to-end machine learning pipeline from data preprocessing to an interactive user interface.

## Features
* Automated classification of news articles (authentic/fake).
* Leverages Natural Language Processing (NLP) techniques for text data.
* Utilizes TF-IDF vectorization for efficient text representation.
* Powered by a trained Naive Bayes machine learning model.
* Interactive web interface built with Streamlit for real-time predictions.
* Robust data preprocessing pipeline to handle raw text input.

## Technologies Used
* **Programming Language:** Python 3.x
* **Data Manipulation:** Pandas, NumPy
* **Text Processing:** NLTK
* **Machine Learning:** Scikit-learn (for TF-IDF, Naive Bayes)
* **Web Framework:** Streamlit
* **Development Environment:** Jupyter Notebook
* **Other:** Joblib (for model serialization)

## Usage
Once the Streamlit application is running (you would typically run it using `streamlit run app.py` from your terminal after setting up the environment and training the model), open your web browser to the provided local URL (e.g., `http://localhost:8501`).
1.  Enter the text of the news article you wish to classify into the input text area.
2.  Click the "Classify" button.
3.  The application will display the prediction (e.g., "Real News" or "Fake News").
