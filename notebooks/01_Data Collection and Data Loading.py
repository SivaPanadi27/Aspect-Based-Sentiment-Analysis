
## Project Title: Aspect-Based Sentiment Analysis for Product Review Insights

### Introduction

In modern e-commerce platforms such as Amazon, Flipkart, and Myntra, users purchase a wide range of products and share their experiences through reviews. These reviews contain valuable information about customer satisfaction and product quality.

However, manually analyzing a large volume of reviews to understand overall product performance is time-consuming and inefficient. Traditional sentiment analysis techniques classify reviews into categories such as positive, negative, or neutral, but they fail to provide detailed insights about specific product features.

To overcome this limitation, this project focuses on **Aspect-Based Sentiment Analysis (ABSA)**, which enables fine-grained analysis by identifying individual product aspects and determining the sentiment associated with each of them.

---

### Objective

The primary objective of this project is to develop a Natural Language Processing (NLP) model that can:

* Automatically identify key aspects of a product from customer reviews
* Determine the sentiment (positive, negative, or neutral) associated with each aspect
* Provide structured insights into product strengths and weaknesses based on user feedback

This approach helps in generating more meaningful and actionable insights compared to traditional sentiment analysis methods.
"""

#Importing Libraries
import nltk
import pandas as pd

"""### Step 1: Data Collection

For this project, we collected a real-world dataset of Amazon product reviews from Google Dataset Search.

The dataset consists of **4,916 rows and 12 columns**, containing detailed information such as review text, ratings, and product identifiers.

From this dataset, we filtered and selected reviews corresponding to a specific product using its ASIN (Amazon Standard Identification Number). The selected product is a **SanDisk microSD Memory Card**, which is a storage device commonly used in smartphones, cameras, and other electronic devices.

Focusing on a single product helps ensure consistency in the type of aspects (such as speed, storage capacity, and performance) mentioned in the reviews, making the aspect-based sentiment analysis more accurate and meaningful.

"""

#Step-2: Data Loading

pd_df=pd.read_csv("amazon_review.csv")
pd_df
