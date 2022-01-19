
import streamlit as st


st.header('Provotype: Model Explanation')
def click_button():
    st.write("you clicked! YAY!")

st.write("Hello Multiverse!")
st.image('./Feature_importance.png')
st.button("click me", on_click = click_button)

st.write("Fucking hell")
st.number_input('Pick a number', 0, 10)

