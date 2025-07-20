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

    sagar = df[df['Name'] == 'Sagar'].iloc[0]

    marks = [sagar['Math'], sagar['Science'], sagar['English']]
    subjects = ['Math', 'Science', 'English']

    plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140)
    plt.title("Sagar Subject Marks")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()