import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df=pd.DataFrame(data)

    df['Gender'] = ['M', 'M', 'F']  
    df = pd.get_dummies(df, columns=['Gender'])
    df.groupby('Gender_M').mean(numeric_only=True)
    print(df)


if __name__ =="__main__":
    main()