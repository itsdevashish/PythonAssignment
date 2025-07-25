import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df=pd.DataFrame(data)
    print("Dataset",df)
    print("Shape",df.shape)

    print("Columns of dataset",df.columns.tolist())
    print("Columns of datatpes",df.dtypes)

if __name__ =="__main__":
    main()