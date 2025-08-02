import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,VotingClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def breastcancerwisconsin(datapath):
    df=pd.read_csv(datapath)
    print(df.head())
    print(df.shape)

    df.replace('?', np.nan, inplace=True)
    df.dropna(inplace=True)

    df['CancerType']=df['CancerType'].map({2:0,4:1})

    df.drop(columns=['CodeNumber'],inplace=True)

    x=df.drop(columns=['CancerType'])
    y=df['CancerType']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    decisionT=DecisionTreeClassifier(max_depth=8)
    randomF=RandomForestClassifier(max_depth=7)
    gradientB=GradientBoostingClassifier()


    voting=VotingClassifier(
        estimators=[
            ('dt',decisionT),
            ('rf',randomF),
            ('gb',gradientB)
        ],
        voting='hard'
    )

    voting.fit(x_train,y_train)
    y_pred=voting.predict(x_test)
    accuracy=accuracy_score(y_pred,y_test)
    print("Accuracy is :",accuracy*100)

def main():
    breastcancerwisconsin("breast-cancer-wisconsin.csv")


if __name__ == "__main__":
    main()
