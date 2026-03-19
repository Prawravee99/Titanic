import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️"
)

# ---------- CSS ----------
st.markdown("""
<style>

/* SECTION TITLE */
.section-title{
font-size:34px;
font-weight:700;
margin-bottom:10px;
}

/* CARD */
.card{
background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.1);
margin-bottom:25px;
}

/* CARD TEXT */
.card-text{
font-size:18px;
line-height:1.6;
}

/* ICON */
.icon{
font-size:36px;
margin-right:10px;
}

/* ALGORITHM CARD */
.algocard{
background:white;
padding:30px;
border-radius:18px;
box-shadow:0px 5px 12px rgba(0,0,0,0.1);
text-align:center;
font-size:20px;
font-weight:600;
}

.algo-icon{
font-size:42px;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- PROJECT OVERVIEW ----------
st.markdown("""
<div class="card">

<div class="section-title">
<span class="icon">📌</span>Project Overview
</div>

<div class="card-text">
This project predicts whether a passenger survived the Titanic disaster using Machine Learning techniques.
The model analyzes passenger information such as age, class, gender, and fare to determine survival probability.
</div>

</div>
""", unsafe_allow_html=True)

# ---------- DATASET ----------
st.markdown("""
<div class="card">

<div class="section-title">
<span class="icon">📊</span>Dataset
</div>

<div class="card-text">
Dataset Source: <b>Kaggle Titanic Dataset</b><br><br>

The dataset contains passenger information including:

• Age<br>
• Sex<br>
• Passenger Class<br>
• Fare<br>
• Survival Status
</div>

</div>
""", unsafe_allow_html=True)

# ---------- ALGORITHMS ----------
st.markdown("""
<div class="section-title">
🤖 Algorithms Used
</div>
""", unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="algocard">
    <div class="algo-icon">🌳</div>
    Decision Tree
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="algocard">
    <div class="algo-icon">📍</div>
    KNN
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="algocard">
    <div class="algo-icon">🧠</div>
    Neural Network
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- FOOTER ----------
st.markdown("""
<div class="card">

<div class="card-text">
This dashboard demonstrates <b>Data Mining</b> and <b>Machine Learning</b> techniques for predictive analysis using the Titanic dataset.
</div>

</div>
""", unsafe_allow_html=True)
