import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Comparison",
    page_icon="🤖"
)

# ---------- CSS ----------
st.markdown("""
<style>

.header{
background: linear-gradient(90deg,#667eea,#764ba2);
padding:40px;
border-radius:20px;
text-align:center;
color:white;
margin-bottom:30px;
}

.model-card{
background:white;
padding:40px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.1);
text-align:center;
}

.model-emoji{
font-size:60px;
margin-bottom:10px;
}

.model-title{
font-size:28px;
font-weight:600;
}

.model-acc{
font-size:42px;
font-weight:700;
margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header">
<h1>🧠 Model Comparison</h1>
<p>Compare Machine Learning Models Performance</p>
</div>
""", unsafe_allow_html=True)

# ---------- ACCURACY ----------
dt = 0.706
knn = 0.622
nn = 0.804

# ---------- MODEL CARDS ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="model-card">
        <div class="model-emoji">🌳</div>
        <div class="model-title">Decision Tree</div>
        <div class="model-acc">{dt}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="model-card">
        <div class="model-emoji">📍</div>
        <div class="model-title">KNN</div>
        <div class="model-acc">{knn}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="model-card">
        <div class="model-emoji">🧠</div>
        <div class="model-title">Neural Network</div>
        <div class="model-acc">{nn}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------- BAR CHART ----------
data = pd.DataFrame({
    "Model":["Decision Tree","KNN","Neural Network"],
    "Accuracy":[dt,knn,nn]
})

fig = px.bar(
    data,
    x="Model",
    y="Accuracy",
    color="Model",
    text="Accuracy",
    title="Model Accuracy Comparison"
)

fig.update_layout(
    title_x=0.5,
    height=450
)

st.plotly_chart(fig,use_container_width=True)

# ---------- BEST MODEL ----------
best_model = data.loc[data["Accuracy"].idxmax()]

st.success(
    f"🏆 Best Model: {best_model['Model']} with Accuracy {best_model['Accuracy']:.3f}"
)
