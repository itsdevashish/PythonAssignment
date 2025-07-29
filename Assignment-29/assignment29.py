import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def marvellousdibeties(datapath):
    df=pd.read_csv(datapath)
    print(df.head())
    x=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
    y=df['Outcome']

    sc=StandardScaler()
    x_sclar=sc.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(x_sclar,y,test_size=0.5,random_state=42)

    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    accuracy=accuracy_score(y_test,y_pred)
    print(accuracy*100)
    
def main():
    marvellousdibeties("diabetes.csv")

if __name__=="__main__":
    main()