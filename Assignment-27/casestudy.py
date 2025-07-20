import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def marvellousheadbrainlinear(datapath):
    # Load dataset
    df = pd.read_csv(datapath)
    print("Dataset sample is:")
    print(df.head())

    df.drop(columns=['Unnamed: 0'], inplace=True)
    
    print("Updated data is:")
    print(df.head())

    print("Missing values in each column:",df.isnull().sum())

    print("Statistical summary is")
    print(df.describe)

    print("correlation Matrix")
    print(df.corr)

    x=df[['TV','radio','newspaper']]
    y=df['sales']

    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    model=LinearRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    mse=mean_squared_error(y_pred,y_test)
    rmse=np.sqrt(mse)
    r2=r2_score(y_pred,y_test)

    print("Mean Squared error is :",mse)
    print("Root mean squared error is :",rmse)
    print("R Square value :",r2)

    plt.figure(figsize=(8, 5))
    plt.scatter(y_test, y_pred, color='blue')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', lw=2)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Actual vs Predicted Sales")
    plt.show()

def main():
    marvellousheadbrainlinear("Advertising.csv")


if __name__ == "__main__":
    main()
