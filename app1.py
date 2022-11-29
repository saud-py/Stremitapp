import streamlit as st
import pandas as pd

st.title("Hello this is my Streamlit app")

st.write("My name is Saud Ali")

st.write(

    pd.DataFrame({
        'A' : [1,5,9,7],
        'B' : [3,2,4,8]
    })
)