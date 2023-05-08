import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.markdown("<h1 style='color: #FF69B4; text-align: center;'>Interactive Map of all the Roller Coasters in the United States</h1>", unsafe_allow_html=True)

#Create the map of all of the rollercoasters in the United States
df = pd.read_csv("RollerCoasters-Geo.csv", usecols=['Coaster','Park', 'Latitude', 'Longitude']) #selects only the 'Coaster', 'Park', 'Latitude', and 'Longitude' columns
df.columns = ['Coasters','Park', 'latitude', 'longitude']
m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=3, control_scale=True) #map with zoom level of three

for i, row in df.iterrows(): # iterates over each row
    iframe = folium.IFrame(str(row["Coasters"]) + ' located at '+ str(row["Park"])) #creates a popup object with the name of the coaster and the park it is located
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    folium.Marker(location=[row['latitude'], row['longitude']], popup=popup, color=row['Coasters']).add_to(m) #adds the marker

st_data = st_folium(m, width=700)





