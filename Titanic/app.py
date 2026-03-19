import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="wide"
)

df = pd.read_csv("titanic.csv")
total_passengers = len(df)
survival_rate = round(df['Survived'].mean() * 100, 2)
features_used = df.shape[1]

# ---------- CSS ----------
st.markdown("""
<style>

.hero{
background: linear-gradient(90deg,#1f77b4,#00b4d8);
padding:60px;
border-radius:25px;
text-align:center;
color:white;
}

.hero-title{
font-size:64px;
font-weight:800;
}

.hero-sub{
font-size:24px;
}

.titanic{
font-size:80px;
text-align:center;
animation: float 3s ease-in-out infinite;
}

@keyframes float{
0%{transform:translateY(0px);}
50%{transform:translateY(-12px);}
100%{transform:translateY(0px);}
}

div.stButton > button{
height:80px;
font-size:20px;
font-weight:600;
border-radius:20px;
border:none;
color:white;
}

/* Button Colors */

div.stButton:nth-child(1) button{
background: linear-gradient(90deg,#3a7bd5,#00d2ff);
}

div.stButton:nth-child(2) button{
background: linear-gradient(90deg,#667eea,#764ba2);
}

div.stButton:nth-child(3) button{
background: linear-gradient(90deg,#ff7e5f,#ff4b2b);
}

div.stButton button:hover{
transform:scale(1.05);
box-shadow:0px 8px 20px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
<div class="hero-title">🚢 Titanic Survival Prediction</div>
<div class="hero-sub">
Machine Learning Dashboard for Predicting Titanic Passenger Survival
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="titanic">🚢</div>', unsafe_allow_html=True)

st.write("")

# ---------- KPI CARDS ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Passengers",total_passengers)

with col2:
    st.metric("Survival Rate", f"{survival_rate}%")

with col3:
    st.metric("Features Used", features_used)

st.write("---")

# ---------- NAVIGATION BUTTONS ----------
col1,col2,col3 = st.columns(3)

with col1:
    if st.button("📊 Explore Titanic Data Dashboard", use_container_width=True):
        st.switch_page("pages/Dashboard.py")

with col2:
    if st.button("🧠 Compare Machine Learning Models", use_container_width=True):
        st.switch_page("pages/Model_Comparison.py")

with col3:
    if st.button("🔮 Predict Passenger Survival", use_container_width=True):
        st.switch_page("pages/Prediction.py")

st.write("")

st.markdown(
"<center>Use the navigation menu on the left to explore the dashboard.</center>",
unsafe_allow_html=True
)
