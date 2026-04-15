#  Aspect-Based Sentiment Analysis for Product Review Insights

## Overview

This project focuses on **Aspect-Based Sentiment Analysis (ABSA)** to extract fine-grained insights from customer reviews. Unlike traditional sentiment analysis, which classifies entire reviews as positive or negative, this project identifies specific product features (aspects) and determines sentiment for each of them individually.

---

## Objective

* Identify key product aspects from customer reviews
* Determine sentiment (Positive, Negative, Neutral) for each aspect
* Provide actionable insights into product strengths and weaknesses

---

## Dataset

* Source: Amazon Product Reviews Dataset
* Total Records: 4,916
* Product: SanDisk microSD Memory Card
* Contains: Review text, ratings, and metadata

---

## Workflow

### 1. Data Preprocessing

* Removed irrelevant columns (reviewerID, asin, etc.)
* Handled missing values
* Cleaned text (lowercasing, URL removal, punctuation handling)
* Removed stopwords (while preserving important words like *not, but*)

### 2. NLP Processing

* Tokenization (word-level)
* POS Tagging
* Lemmatization

### 3. Feature Engineering

* TF-IDF Vectorization (`max_features=5000`)

### 4. Model Training

Trained and compared multiple models:

* Logistic Regression
* Naive Bayes
* Support Vector Machine (SVM) 

### 5. Evaluation Metrics

* Accuracy
* Precision (Weighted)
* Recall (Weighted)
* F1-Score (Weighted)
* Stratified K-Fold Cross Validation

---

## Results

Model                Accuracy   F1 Score  
Logistic Regression  ~0.90      ~0.90     
Naive Bayes         ~0.91      ~0.87     
**SVM (Best)**      **~0.94**  **~0.92** 

---

## Aspect-Based Sentiment Analysis (ABSA)

### Steps:

1. Extracted aspects using POS tagging (nouns)
2. Split reviews into sentences
3. Predicted sentiment at sentence level
4. Mapped aspects to corresponding sentiment
5. Aggregated results to generate insights

---

## Key Insights

* **Speed and Storage** are highly positively perceived aspects
* **Battery and Durability** show mixed or negative feedback
* Dataset is highly imbalanced (~79% positive reviews)

---

## Limitations

* Imbalanced dataset affects minority class prediction
* Aspect extraction is rule-based and may include noise
* Limited handling of complex language (sarcasm, context)

---

## Future Improvements

* Use transformer models (BERT for ABSA)
* Improve aspect extraction using dependency parsing
* Handle class imbalance (SMOTE, class weighting)
* Deploy as a web application

---

## Tech Stack

* Python
* Pandas, NumPy
* NLTK
* Scikit-learn
* Matplotlib

---

##  Conclusion

This project demonstrates how NLP and machine learning can be used to extract meaningful, aspect-level insights from customer reviews. It moves beyond traditional sentiment analysis and provides actionable feedback for product improvement.

---

## Author

* Panadi Siva Prasad
