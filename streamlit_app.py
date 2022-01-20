import numpy as np
import streamlit as st
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.ibb.co/TvmxXHb/Provotype-background-3.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('# Provotype: Model Explanation')
col1, col2, col3= st.columns([3, 1, 1])

with col1:
    st.write("""Student loan fraud costs Lånekassen approximately 26 million kroner (2018) a year. In particular, applicants may falsely state that they are living away from home, and thus be eligible for an education grant (stipend). Lånekassen estimates that a recurring 4-5 % of students cannot prove that they’re living away from home. \n
To combat this problem, our team has developed an AI that will suggest high-risk cases of student loan holders, whose applications will be processed manually. This initiative will help us allocate our resources more efficiently. Both in terms of time needed to process the student loan applications, and in terms of funds distributed. In the long run, this will lead to more efficient use of tax money and give more people the opportunity to get an education. \n
To gain trust with our applicants, we strive to provide insight into how our AI makes decisions about which applications to process manually, and how the risk profile is calculated. Feature importance is a useful measure of the importance of input variables in determining the outcome variable in AI models. \n
In our risk calculator widget below, you see the eight most important variables of our AI model. To better understand how our model calculates risk, we invite you to manipulate the variables below and see how the risk estimate changes. 
""")
    st.markdown("## Feature Importance")
    st.image('./Feature_importance.png')

with col2:
    st.markdown('## Model Calculator')
    st.number_input("Age", 18, 100)
    st.selectbox("Citizenship", ["Norwegian", "Other"])
with col3:
    st.write("\n")
    st.selectbox("Sex", ["Male", "Female", "Other"])
    st.selectbox("Country of Study", ["Norway", "Other"])
    st.selectbox("Family Status", ["Parent", "Child"])
    st.number_input("Postal Code", 0, 9999)
    st.number_input("Value of personal assets", min_value=-1000000, max_value=1000000)
    st.number_input("Annual income", min_value=0, max_value=1000000)
    st.selectbox("Study Degree", ["Bachelor", "Master", "PhD"])
    st.selectbox("Study Subject", ["Natural Sciences", "Economics", "Social Studies", "Enginearing", "Philosophy"])
    st.number_input("Startup year", 2010, 2021)
    st.number_input("Expected year of completed education", 2011, 2030)
    st.selectbox("University Credits", ["0-179", "180-300", "300+"])
    st.selectbox("Tuition Fees", ["0-999", "1000-10000", "10000+"])
    st.checkbox("Same municipality as parents")
    st.write(f"Result: {np.random.uniform(low= 0, high= 10) :.1f} %")

