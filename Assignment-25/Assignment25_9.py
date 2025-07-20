import pandas as pd
import numpy as np

def main():
    data = {'Marks': [45, 67, 88, 32, 76]}
    df = pd.DataFrame(data)

    df['Result'] = np.where(df['Marks'] < 50, 'Fail', 'Pass')
    print(df)

if __name__ == "__main__":
    main()