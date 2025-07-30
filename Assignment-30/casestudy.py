import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def marvellousdibeties(datapath):
    df=pd.read_csv(datapath)
    print(df.head())
    x=df.drop('y',inplace=True)
    y=df['y']

    sc=StandardScaler()
    x_sclar=sc.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

    sc=StandardScaler()
    x_sclar=sc.fit_transform(x_train)
    x_sclar=sc.fit_transform(x_test)

    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print(accuracy*100)
    
def main():
    marvellousdibeties("diabetes.csv")

if __name__=="__main__":
    main()