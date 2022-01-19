
import streamlit as st


def click_button():
    st.write("you clicked! YAY!")

st.write("Hello Multiverse!")
st.button("click me", on_click = click_button)

st.write("Fucking hell")