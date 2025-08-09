import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def newspred():
    fake = pd.read_csv("Fake.csv")
    real = pd.read_csv("True.csv")

    fake['label'] = 0
    real['label'] = 1

    df = pd.concat([fake, real], axis=0)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    print(df.columns)
    print("Shape:", df.shape)
    print("Missing Values in each column:\n", df.isnull().sum())

    x = df['text']
    y = df['label']

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(x_train)
    X_test_tfidf = vectorizer.transform(x_test)

    model = LogisticRegression(max_iter=500)
    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy * 100)
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", cm)

    print("Classification Report:\n", classification_report(y_test, y_pred))

def main():
    newspred()

if __name__ == "__main__":
    main()
