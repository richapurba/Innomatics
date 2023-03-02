import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


#Page title, header, and subheader
st.set_page_config(page_title="NASA Discovery")
st.header("Habitable Exoplanet and Stars 2023")
st.subheader("Are we already have a new home?")

#Load the dataset
excel = "Habitable.csv"
sheet_name = "DATA"

df = pd.read_excel(excel, sheet_name=sheet_name)

st.dataframe(df)