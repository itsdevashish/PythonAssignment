from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

df['target'] = data.target

print(df.isnull().sum())  

x=df.drop(columns='target')
y=df['target']

sc=StandardScaler()
xscaler=sc.fit_transform(x)

x_train,x_test,y_train,y_test=train_test_split(xscaler,y,test_size=0.2,random_state=42)
model=RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
confusionmatrix=confusion_matrix(y_test,y_pred)
classificationreport=classification_report(y_test,y_pred)

print("Accuracy is ",accuracy*100)
print("Confusion Matrix",confusionmatrix)
print("Classification Report ",classificationreport)

