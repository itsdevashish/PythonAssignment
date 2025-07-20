import matplotlib.pyplot as plt
import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math'] + df['Science'] + df['English']
    df['status'] = df['Total'].apply(lambda x:'Pass'if x>=250 else 'Fail')
    passedstudent = (df['status'] == 'Pass').sum()
    print("Passed students:", passedstudent) 

    plt.hist(df['Math'],bins=5,color='orange')
    plt.title("Histogram")
    plt.xlabel("Marks")
    plt.ylabel("No of students")
    plt.show()


if __name__ == "__main__":
    main()