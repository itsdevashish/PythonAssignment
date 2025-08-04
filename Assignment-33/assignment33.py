import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def student(datapath):
    df=pd.read_csv(datapath,sep=';')
    print(df.head())

    x=df[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]
    sc=StandardScaler()
    x_scale=sc.fit_transform(x)

    WCSS=[]
    for k in range(1,11):
        model=KMeans(n_clusters=k,init='k-means++',n_init=10,random_state=42)
        model.fit(x_scale)
        WCSS.append(model.inertia_)
        print(model.labels_)

    plt.plot(range(1, 11), WCSS, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    plt.show()

    model = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42)
    df['Cluster'] = model.fit_predict(x_scale)

    print("Cluster wise averages")
    print(df.groupby('Cluster')[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']].mean())

def main():
    student("student-mat.csv")


if __name__ == "__main__":
    main()