import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# โหลด dataset
data = pd.read_csv("titanic.csv")

# เลือก features
data = data[['Survived','Pclass','Sex','Age','Fare','SibSp']]

# แปลงเพศเป็นตัวเลข
data['Sex'] = data['Sex'].map({'male':0,'female':1})

# ลบข้อมูลว่าง
data = data.dropna()

# features / target
X = data[['Pclass','Sex','Age','Fare','SibSp']]
y = data['Survived']

# train test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# สร้างโมเดล
model = MLPClassifier(max_iter=500)

model.fit(X_train,y_train)

# ทำนาย
pred = model.predict(X_test)

# UI
st.title("📈 Model Evaluation")

# Accuracy
acc = accuracy_score(y_test,pred)

st.metric("Model Accuracy",round(acc,3))

# Confusion Matrix
cm = confusion_matrix(y_test,pred)

fig,ax = plt.subplots()

sns.heatmap(cm,annot=True,fmt='d',cmap='Blues',ax=ax)

st.pyplot(fig)