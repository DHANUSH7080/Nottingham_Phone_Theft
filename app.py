import pandas as pd
import streamlit as st
import pydeck as pdk

# Load data
data = pd.read_csv("phone_theft.csv")


# Streamlit app
st.title("Detailed Phone Theft Map")
st.write("This map shows locations of phone theft incidents at Nottingham.")


# Define Pydeck Layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["lon", "lat"],
    get_radius=100,  # Size of each point
    get_color=[255, 0, 0, 160],  # Red with transparency
    pickable=True
)

# View State (map center + zoom)
view_state = pdk.ViewState(
    latitude=data["lat"].mean(),
    longitude=data["lon"].mean(),
    zoom=11,
    pitch=0
)

# Tooltip for hover info
tooltip = {
    "html": "<b>Location:</b> [{lat}, {lon}]",
    "style": {"color": "white"}
}

# Render map
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
))



