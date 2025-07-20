import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    df = pd.DataFrame(data)

    result = LabelEncoder()
    df['city_encoded'] = result.fit_transform(df['City'])
    print(df)

if __name__ == "__main__":
    main()