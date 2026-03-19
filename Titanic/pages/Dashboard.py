import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลด dataset
data = pd.read_csv("titanic.csv")

st.title("📊 Titanic Data Dashboard")

col1,col2 = st.columns(2)

# Gender Distribution
with col1:
    fig,ax = plt.subplots()
    data['Sex'].value_counts().plot(kind='bar',ax=ax)
    ax.set_title("Gender Distribution")
    st.pyplot(fig)

# Survival by Gender
with col2:
    fig,ax = plt.subplots()
    data.groupby('Sex')['Survived'].mean().plot(kind='bar',ax=ax)
    ax.set_title("Survival by Gender")
    st.pyplot(fig)

col3,col4 = st.columns(2)

# Survival by Class
with col3:
    fig,ax = plt.subplots()
    data.groupby('Pclass')['Survived'].mean().plot(kind='bar',ax=ax)
    ax.set_title("Survival by Class")
    st.pyplot(fig)

# Age Distribution
with col4:
    fig,ax = plt.subplots()
    data['Age'].hist(bins=20,ax=ax)
    ax.set_title("Age Distribution")
    st.pyplot(fig)

col5,col6 = st.columns(2)

# Fare Distribution
with col5:
    fig,ax = plt.subplots()
    data['Fare'].hist(bins=20,ax=ax)
    ax.set_title("Fare Distribution")
    st.pyplot(fig)

# SibSp Distribution
with col6:
    fig,ax = plt.subplots()
    data['SibSp'].value_counts().plot(kind='bar',ax=ax)
    ax.set_title("SibSp Distribution")
    st.pyplot(fig)