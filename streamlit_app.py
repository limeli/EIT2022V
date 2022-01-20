import numpy as np
import streamlit as st
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.ibb.co/XJxXp9Y/Provotype-background-2.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.header('Provotype: Model Explanation')
col1, col2= st.columns([3, 2])

with col1:
    st.write("Hello Multiverse!")
    st.image('./Feature_importance.png')

with col2:
    st.header('Model Calculator')
    st.number_input("Age", 18, 100)
    st.selectbox("Sex", ["Male", "Female", "Other"])
    st.selectbox("Citizenship", ["Norwegian", "Other"])
    st.multiselect("Family Status", ["Parent", "Child"])
    st.number_input("Postal Code", 0, 9999)
    st.number_input("Value of personal assets", min_value=-1000000, max_value=1000000)
    st.number_input("Annual income", min_value=0, max_value=1000000)
    st.selectbox("Study Degree", ["Bachelor", "Master", "PhD"])
    st.multiselect("Study Subject", ["Natural Sciences", "Economics", "Social Studies", "Enginearing", "Philosophy"])
    st.multiselect("Country of Study", ["Norway", "Other"])
    st.number_input("Startup year", 2010, 2021)
    st.number_input("Expected year of completed education", 2011, 2030)
    st.selectbox("University Credits", ["0-179", "180-300", "300+"])
    st.multiselect("Tuition Fees", ["0-999", "1000-10000", "10000+"])
    st.checkbox("Same municipality as parents")
    st.write(f"Result: {np.random.uniform(low= 0, high= 10) :.1f} %")

