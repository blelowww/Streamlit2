import streamlit as st
import pandas as pd
import numpy as np
import folium as fo
from streamlit_folium import folium_static
import geopandas as gp

st.title('Streamlit with Folium')

"""
## An easy way to create a website using Python
"""

df = pd.read_csv('https://raw.githubusercontent.com/Maplub/odsample/master/20190101.csv')

df = df[['latstartl','lonstartl','timestart']]

df = df[:100]
st.write('<h1>จรัสพงศ์ เทพรอด 6030804921</h1>',unsafe_allow_html=True)

st.write(df)

longitude = 100.7200
latitude = 13.9514

station_map = fo.Map(
	location = [latitude, longitude], 
	zoom_start = 10)

latitudes = list(df.latstartl)
longitudes = list(df.lonstartl)
labels = list(df.timestart)

for lat, lng, label in zip(latitudes, longitudes, labels):
	fo.Marker(
		location = [lat, lng], 
		popup = label,
		icon = fo.Icon(color='red', icon='pin',icon_color='black',angle=35)
	).add_to(station_map)

folium_static(station_map)