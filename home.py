import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import os
import pathlib

#chart_data = pd.DataFrame(
 #  np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
  # columns=['lat', 'lon'])

path = os.path.join(str(pathlib.Path().resolve()), './okycgeoGM_color.csv')
with open(path) as f:
    data = pd.read_csv(f)
chart_data = pd.DataFrame(data)
"""
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=35.964668,
        longitude=-83.926453,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[longitude, latitude]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
"""

'''
# One Knox Youth Club Player Database
### Map of player location with team color: yellow = 1st team, orange = 2nd team, blue = 3rd team, white = 4th team, green = monsters
'''
st.map(chart_data,color="color")
'''
# Players on NPL, DPL, Yellow, and USL Academy
'''
yellow = chart_data.loc[chart_data['color'] == '#fdb960']
st.map(yellow,color='#fdb960')
'''
# PLayers on Orange teams
'''
orange = chart_data.loc[chart_data["color"] == "#f5854f"]
st.map(orange,color="#f5854f")
'''
# Players on Blue teams
'''
blue = chart_data.loc[chart_data["color"] == "#475a86"]
st.map(blue,color="#475a86")
'''
# Players on White Teams
'''
white = chart_data.loc[chart_data["color"] == "#eae6d0"]
st.map(white,color="#eae6d0")
'''
# Monsters
'''
monsters = chart_data.loc[chart_data["color"] == "#29ac31ff"]
st.map(monsters,color="#29ac31ff")