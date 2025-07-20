import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def marvellousheadbrainlinear(datapath):
    # Load dataset
    df = pd.read_csv(datapath)
    print("Dataset sample is:")
    print(df.head())

    x=df[['Flavanoids','OD280/OD315 of diluted wines','Proline','Color intensity','Alcohol']]
    y=df['Class']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    model=KNeighborsClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print(y_pred)
    accuracy=accuracy_score(y_pred,y_test)

    print("Accuracy is :",accuracy*100)

def main():
    marvellousheadbrainlinear("WinePredictor.csv")



if __name__ == "__main__":
    main()

