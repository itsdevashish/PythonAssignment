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
    amit_marks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

    plt.figure(figsize=(8,5))
    plt.plot(amit_marks.index, amit_marks.values, color='green')
    plt.title("Subject wise Marks for Amit")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()
if __name__ =="__main__":
    main()