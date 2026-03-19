import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮"
)

# ---------- CSS ----------
st.markdown("""
<style>

.header{
background: linear-gradient(90deg,#4facfe,#7b2ff7);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:30px;
}

.input-card{
background:white;
padding:30px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.1);
margin-bottom:25px;
}

.result-success{
background: linear-gradient(90deg,#6a11cb,#2575fc);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
font-size:26px;
font-weight:600;
margin-top:20px;
}

.result-fail{
background: linear-gradient(90deg,#4facfe,#7b2ff7);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
font-size:26px;
font-weight:600;
margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header">
<h1>🔮 Survival Prediction</h1>
<p>Predict whether a passenger survived the Titanic disaster</p>
</div>
""", unsafe_allow_html=True)

# ---------- INPUT CARD ----------
st.markdown('<div class="input-card">', unsafe_allow_html=True)

pclass = st.selectbox("Passenger Class", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = st.slider("Age", 1, 80)
fare = st.number_input("Fare", 0, 500)
sibsp = st.number_input("SibSp", 0, 10)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- PREDICT BUTTON ----------
predict = st.button("🚀 Predict Survival")

# ---------- SIMPLE MODEL (Example) ----------
if predict:

    sex = 0 if sex == "male" else 1

    # Example scoring (แทนโมเดลจริง)
    score = (sex*0.4)+(pclass*0.1)+(age*0.01)+(fare*0.001)

    prob = min(score,1)

    if prob > 0.5:

        st.markdown(f"""
        <div class="result-success">
        🎉 Passenger Likely Survived<br><br>
        Probability: {prob:.2f}
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="result-fail">
        ❌ Passenger Likely Did Not Survive<br><br>
        Probability: {prob:.2f}
        </div>
        """, unsafe_allow_html=True)