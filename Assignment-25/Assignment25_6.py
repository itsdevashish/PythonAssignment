import pandas as pd

def main():
    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    df = pd.DataFrame(data)

    replace = {'A+': 'Excellent', 'A': 'Very Good', 'B+': 'Good', 'B': 'Average', 'C': 'Poor'}
    df['Grade'] = df['Grade'].replace(replace)
    print(df)


if __name__ == "__main__":
    main()