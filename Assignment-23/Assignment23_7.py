import pandas as pd
import matplotlib.pyplot as plt
def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df=pd.DataFrame(data)
    df['Total']=df['Math']+df['Science']+df['English']
    print(df)

    plt.figure(figsize=(8,5))
    plt.bar(df['Name'],df['Total'],color='skyblue')
    plt.xlabel('Name')
    plt.ylabel('Total')
    plt.title("Total Marks By Students")
    plt.show()

if __name__ =="__main__":
    main()