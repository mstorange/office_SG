import streamlit as st
import geopandas as gpd
import folium
from folium import Element
from numpy import float64
from streamlit_folium import st_folium
import streamlit.components.v1 as components
st.set_page_config(layout="wide")

st.title('Büromöglichkeiten in SG')
st.write('Topografische Darstellung der von BUM gefundenen Bürooptionen in St. Gallen')

with open("Büros_SG.html", "r", encoding="utf-8") as f:
    m = f.read()

components.html(m, height=600, width=1400, scrolling=True)



#st_data = st_folium(m, height = 500, width = 1300, returned_objects=[])
