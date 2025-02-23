
# import streamlit as st
# import pandas as pd
# import json
# import numpy as np
# import tensorflow as tf
# import xgboost as xgb

# # Load footfall data from CSV
# filename = "C:/SmartRailCrowdPrediction/data/station_data.csv"
# try:
#     df = pd.read_csv(filename)
#     df["time"] = pd.to_datetime(df["time"])  # Ensure time column is in datetime format
# except FileNotFoundError:
#     st.error("Error loading CSV data. Please check the file location.")
#     df = pd.DataFrame()

# # Sidebar Input
# st.sidebar.header("📊 Prediction Input")
# stations = ["New Delhi", "Howrah", "Mumbai CST", "Chennai Central", "Bangalore City"]
# selected_station = st.sidebar.selectbox("Select Station", stations)

# # Filter data for selected station
# station_data = df[df["station"] == selected_station]

# if not station_data.empty:
#     latest_data = station_data.iloc[-1]  # Get the latest entry
#     station_name = latest_data["station"]
#     current_footfall = latest_data["footfall"]
#     congestion_level = latest_data["congestion_level"]
#     entry_count = latest_data["entry_count"]
#     exit_count = latest_data["exit_count"]
#     peak_hours = latest_data["peak_hours"]

#     st.title("🚉 Smart Rail Crowd Prediction Dashboard")
#     st.subheader(f"📍 Station: {station_name}")
    
#     # Display metrics in a grid layout
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Current Footfall", current_footfall)
#     col2.metric("Congestion Level", congestion_level)
#     col3.metric("Peak Hours", peak_hours)
    
#     col4, col5 = st.columns(2)
#     col4.metric("Entry Count", entry_count)
#     col5.metric("Exit Count", exit_count)

#     # Minute-wise Footfall Trends
#     minute_trends = station_data.set_index("time")["footfall"]
#     st.subheader("📈 Minute-wise Footfall Trends")
#     st.line_chart(minute_trends)

#     # Predict Crowd Level
#     if st.sidebar.button("Predict Using Live Data"):
#         crowd_level = "Normal" if current_footfall < 2000 else "Medium" if current_footfall < 5000 else "Overcrowded"
#         st.success(f"Predicted Congestion Level: {crowd_level}")

#         # Alert if overcrowded
#         if crowd_level == "Overcrowded":
#             st.error("🚨 Alert: Overcrowding detected! Notify the station head for crowd management.")
# else:
#     st.error("No data available for the selected station or incorrect CSV format.")



import streamlit as st
import pandas as pd
import json
import numpy as np
import tensorflow as tf
import xgboost as xgb

# Load footfall data from CSV
filename = "C:/SmartRailCrowdPrediction/data/station_data.csv"
try:
    df = pd.read_csv(filename)
    df["Time"] = pd.to_datetime(df["Time"])  # Ensure time column is in datetime format
except FileNotFoundError:
    st.error("Error loading CSV data. Please check the file location.")
    df = pd.DataFrame()

# Sidebar Input
st.sidebar.header("📊 Prediction Input")
stations = ["New Delhi", "Howrah", "Mumbai CST", "Chennai Central", "Bangalore City"]
selected_station = st.sidebar.selectbox("Select Station", stations)

# Filter data for selected station
station_data = df[df["Station"] == selected_station]

if not station_data.empty:
    platforms = station_data["Platform"].unique().tolist()
    selected_platform = st.sidebar.selectbox("Select Platform", platforms)
    
    latest_data = station_data.iloc[-1]  # Get the latest entry
    station_name = latest_data["Station"]
    current_footfall = latest_data["Overall Footfall"]
    congestion_level = latest_data["Congestion Level"]
    entry_count = latest_data["Entry Count"]
    exit_count = latest_data["Exit Count"]
    peak_hours = latest_data["Peak Hours"]
    
    platform_data = station_data[station_data["Platform"] == selected_platform].iloc[-1]
    platform_footfall = platform_data["Platform Footfall"]
    
    st.title("🚉 Smart Rail Crowd Prediction Dashboard")
    st.subheader(f"📍 Station: {station_name}")
    
    # Display metrics in a grid layout
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Footfall", current_footfall)
    col2.metric("Congestion Level", congestion_level)
    col3.metric("Peak Hours", peak_hours)
    
    col4, col5 = st.columns(2)
    col4.metric("Entry Count", entry_count)
    col5.metric("Exit Count", exit_count)
    
    st.subheader(f"🚉 Platform {selected_platform} Details")
    st.metric("Platform Footfall", platform_footfall)
    
    # Minute-wise Footfall Trends
    minute_trends = station_data.set_index("Time")["Overall Footfall"]
    st.subheader("📈 Station Footfall Trends")
    st.line_chart(minute_trends)

     # Platform Footfall Trends
    platform_trends = station_data[station_data["Platform"] == selected_platform].set_index("Time")["Platform Footfall"]
    st.subheader(f"📊 Footfall Trends for Platform {selected_platform}")
    st.line_chart(platform_trends)
    
    # Predict Crowd Level
    if st.sidebar.button("Predict Using Live Data"):
        station_crowd_level = "Normal" if current_footfall < 2000 else "Medium" if current_footfall < 3500 else "Overcrowded"
        platform_crowd_level = "Normal" if platform_footfall < 200 else "Medium" if platform_footfall < 900 else "Overcrowded"
        
        st.success(f"Predicted Congestion Level for Station: {station_crowd_level}")
        st.success(f"Predicted Congestion Level for Platform {selected_platform}: {platform_crowd_level}")
        
        # Alerts for overcrowding
        if station_crowd_level == "Overcrowded":
            st.error("🚨 Alert: Overcrowding detected at the station! Notify the station head for crowd management.")
        if platform_crowd_level == "Overcrowded":
            st.error(f"🚨 Alert: Overcrowding detected at Platform {selected_platform}! Immediate action required.")
else:
    st.error("No data available for the selected station or incorrect CSV format.")