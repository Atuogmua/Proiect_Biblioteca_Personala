import json
import pandas as pd
import streamlit as st
import numpy as np


st.header("Biblioteca persoanala")
tab = pd.DataFrame(columns=("Denumire","Autor","Recenzie proprie"))

st.dataframe(tab)  # Same as st.write(df)
buton = st.button("Add new row")

st.write("value:", buton)
if buton == True:
    st.write(":blue[a]")
    denumire = st.text_input("Denumire")
    autor = st.text_input("Autor")
    rec_prop =
    df = pd.DataFrame(columns = (denumire, autor, rec_prop))
    #tab.add_row("Denumire":denumire)
    buton = False
st.write("value:", buton)
