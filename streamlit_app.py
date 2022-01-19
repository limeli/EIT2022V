import numpy as np
import streamlit as st
from image_as_background import set_png_as_page_bg

set_png_as_page_bg('./provotype_background.png')

st.header('Provotype: Model Explanation')
col1, col2= st.columns([3, 2])
with col1:
    st.write("Hello Multiverse!")
    st.image('./Feature_importance.png')

    st.write("Fucking hell")


with col2:
    st.header('Model Calculator')
    st.selectbox("Gender", ["Male", "Female", "Other"])
    st.number_input("Age", 18, 100)
    st.selectbox("Citizenship", ["Norwegian", "Other"])
    st.selectbox("University Credits", ["0-179", "180-300", "300+"])
    st.number_input("Annual income", min_value=0, max_value=1000000)
    st.number_input("Value of personal assets", min_value=-1000000, max_value=1000000)
    st.number_input("How many times cried this week", min_value = 0)
    st.checkbox("Same address as parent(s)")
    st.checkbox("Mental disorder")
    st.write(f"Result: {np.random.uniform(low= 0, high= 10) :.1f} %")

