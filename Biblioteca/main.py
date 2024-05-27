import json
import pandas as pd
import streamlit as st
import numpy as np
from streamlit_star_rating import st_star_rating

st.title("Biblioteca personală")

if "row_data" not in st.session_state:
    st.session_state.row_data = []

row1 = pd.DataFrame(st.session_state.row_data, columns=["Denumire", "Autor", "Recenzie proprie"])
tab = st.table(row1)

with st.expander("**Add New Row**"):
    den = st.text_input("Denumire", placeholder="Introduceti denumirea carții")
    aut = st.text_input("Autor", placeholder="Introduceti numele autorului")
    rec_prop = st_star_rating("Recenzie proprie", maxValue=5, defaultValue=0)

    if st.button("Gata"):
        if den and aut:
            new_row = {"Denumire": den, "Autor": aut, "Recenzie proprie": rec_prop}
            st.session_state.row_data.append(new_row)
            row1 = pd.DataFrame(st.session_state.row_data)
            st.experimental_rerun()

st.write(st.session_state)
