""" This will be the main python file"""
""" Just testing changes """

import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
import rasterio
import numpy as np
from shapely.geometry import Point

st.title("Light Pollution Map for Stargazers")

# 1. Get user location
location_input = st.text_input("Enter your location (City, Zip, etc):")

if location_input:
    geolocator = Nominatim(user_agent="stargazer-app")
    location = geolocator.geocode(location_input)
    if location:
        st.success(f"Location found: {location.address}")
        lat, lon = location.latitude, location.longitude

        # 2. Display map
        m = folium.Map(location=[lat, lon], zoom_start=8)
        folium.Marker([lat, lon], tooltip="You are here").add_to(m)
        st_folium(m, width=700)

        # Placeholder for raster logic
        st.info("🛰️ Raster light pollution analysis coming soon!")

    else:
        st.error("Location not found. Try a more specific place.")