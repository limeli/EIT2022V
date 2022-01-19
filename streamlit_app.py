
import streamlit as st


st.header('Provotype: Model Explanation')
def click_button():
    st.write("you clicked! YAY!")

col1, col2 = st.columns(2)
with col1:
    st.write("Hello Multiverse!")
    st.image('./Feature_importance.png')
    st.button("click me", on_click = click_button)

    st.write("Fucking hell")
    st.number_input('Pick a number', 0, 10)

