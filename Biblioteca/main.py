import json
import pandas as pd
import streamlit as st
st.header("Biblioteca persoanala")
tab =st.dataframe()
buton = st.button("Add new row")

st.write("value:", buton)
if buton == True:
    st.write("a")
    buton = False
i2 = st.checkbox("reset button")