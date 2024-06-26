import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)


with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi, I'm Ardit! I am a Python programmer, teacher and founder of Python how.
    I graduated!
    """
    st.info(content)

content2 = """

Here are some of my Python related projects that I have worked on! 
If you have any questions, please feel free to contact my email via the "Contact me" page.
"""
st.write(content2)


