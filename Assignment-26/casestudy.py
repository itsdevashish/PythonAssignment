import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def playpredictor(datapath):
    df=pd.read_csv(datapath)
    print(df.shape)
    print(df.head())
    df.drop(columns=['Unnamed: 0'],inplace=True)
    print(df.head())
       
    weather = LabelEncoder()
    temp = LabelEncoder()

    df['Whether'] = weather.fit_transform(df['Whether'])
    df['Temperature'] = temp.fit_transform(df['Temperature'])

    x=df[['Whether','Temperature']]
    y=df['Play']

    print(df.head())

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_pred,y_test)
    print("Accuracy is :",accuracy*100)


    plt.hist(df[['Whether','Temperature']])
    plt.title("Playpredictor case Study")
    plt.xlabel("Whether Temperature")
    plt.ylabel("Encoded Values")
    plt.show()



def main():
    playpredictor("PlayPredictor.csv")


if __name__ == "__main__":
    main()
