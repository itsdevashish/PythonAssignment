import pandas as pd

def main():
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}
    df = pd.DataFrame(data)
    df['Age'] = df['Age'].astype(int)
    print(df.dtypes)

if __name__ == "__main__":
    main()