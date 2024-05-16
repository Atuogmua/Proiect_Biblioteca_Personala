import json
import pandas as pd
import streamlit as st
import numpy as np
from streamlit_star_rating import st_star_rating

st.header("Biblioteca persoanala")
row1 = pd.DataFrame(columns=("Denumire","Autor","Recenzie proprie"))
tab = st.table(row1)

buton = st.button("Add new row")
st.write("value:", buton)
if buton == True:
    denumire = st.text_area("Denumire")
    autor = st.text_area("Autor")
    #rec_prop = st_star_rating("Recenzie proprie", maxValue=5, defaultValue=3, key="rating")
    df = pd.DataFrame(columns = (denumire, autor))
    tab.add_row(df)
    new_row = {
        "Denumire": str(denumire),
        "Autor": str(autor)
        #"Recenzii proprii": int(rec_prop)
    }
    biblio = json.dumps(new_row, sort_keys = True)
    ver = st.button("Gata")
    if ver == True:
        buton = False

st.write("value:", buton)
