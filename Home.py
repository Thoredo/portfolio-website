import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Jurgen Stegeman")
    content = """
    Hello, I am Jurgen! I'm a starting developer, in my life I have done lots 
    of different studies and jobs. But I always had an itch for programming, 
    after a period of sickness I decided to use my time to learn something new.
    I started learning HTML, CSS and JavaScript. I had a lot of fun learning 
    them especially JS. But I wasn't sure what I wanted to do yet so after a 
    orientation program through Techgrounds, I started a data engineer course 
    through Bit Academy. I loved coding in Python so I decided to learn as 
    much as I could about Python.
    """
    st.info(content)

st.write("Below you can find some of the apps i have built in python. \
         Feel free to contact me!")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
   for index, row in df[:10].iterrows():
       st.header(row["title"])
       st.write(row['description'])
       st.image(f"images/{row['image']}")
       st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
       st.header(row["title"])
       st.write(row['description'])
       st.image(f"images/{row['image']}")
       st.write(f"[Source Code]({row['url']})")