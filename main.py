import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Jurgen Stegeman")
    content = """
    Hello, I am Jurgen! I'm a starting developer, in my life i have done lots of different studies and jobs.
    But I always had an itch for programming, after a period of sickness I decided to use my time to learn something new.
    I started learning HTML, CSS and JavaScript.I had a lot of fun learning them especially JS.
    But I wasn't sure what i wanted to do yet so after a orientation program through Techgrounds, 
    i started a data engineer course through Bit Academy.
    I loved coding in Python so i decided to learn as much as i could about Python.
    """
    st.info(content)

