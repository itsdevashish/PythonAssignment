import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df=pd.DataFrame(data)
    drop=df.drop('English',axis=1)
    print(drop)

if __name__ =="__main__":
    main()