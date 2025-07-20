
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    df = pd.DataFrame(data)

    encode = pd.get_dummies(df, columns=['Department'])
    print(encode)

if __name__ == "__main__":
    main()