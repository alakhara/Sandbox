import streamlit as st
import joblib
import numpy as np
import requests
import pickle
 
def load_model(url):
    response = requests.get(url)
    file_content = response.content
    data = pickle.loads(file_content)
    return data
 
# Load the trained model
model = load_model("https://github.com/alakhara/Sandbox/raw/main/second_model")
 
st.title('Car Selling Price Predictor')
 
# Input fields
year = st.number_input('Year', min_value=2000, max_value=2024, value=2014)
km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=500000, value=150000)
fuel = st.selectbox('Fuel Type', options=["Diesel", "Petrol", "CNG"]) 
seller_type = st.selectbox('Seller Type', options=["Individual", "Dealership"])  # Assuming 0-1 are codes for seller types
transmission = st.selectbox('Transmission', options=["Manual", "Automatic"])  # Assuming 0-1 are codes for transmission
owner = st.selectbox('Owner', options=["First Owner", "Second Owner", "Third Owner"])  # Assuming 0-3 are codes for owner types
mileage = st.number_input('Mileage', min_value=0, max_value=5000, value=200)
engine = st.number_input('Engine (CC)', min_value=500, max_value=5000, value=1500)
max_power = st.number_input('Max Power (BHP)', min_value=10, max_value=1000, value=100)
seats = st.number_input('Seats', min_value=2, max_value=10, value=5)
sales_status = st.selectbox('Sales Status', options=["y", "n"])  # Assuming 0-1 are codes for sales status
region_label = st.selectbox('Region Label', options=["West", "North", "South", "Central", "East"])  # Assuming 0-4 are codes for regions
 
# Map categorical inputs to numerical codes
fuel_map = {"Diesel": 1, "Petrol": 2, "CNG": 3}
seller_type_map = {"Individual": 0, "Dealership": 1}
transmission_map = {"Manual": 0, "Automatic": 1}
owner_map = {"First Owner": 0, "Second Owner": 1, "Third Owner": 2}
sales_status_map = {"y": 1, "n": 0}
region_label_map = {"West": 0, "North": 1, "South": 2, "Central": 3, "East": 4}
 
# Convert inputs to numerical codes
fuel_code = fuel_map[fuel]
seller_type_code = seller_type_map[seller_type]
transmission_code = transmission_map[transmission]
owner_code = owner_map[owner]
sales_status_code = sales_status_map[sales_status]
region_label_code = region_label_map[region_label]
 
# Predict button
if st.button('Predict Selling Price'):
    features = np.array([[year, km_driven, fuel_code, seller_type_code, transmission_code, owner_code, mileage, engine, max_power, seats, sales_status_code, region_label_code]])
    prediction = model.predict(features)
    st.write(f'Predicted Selling Price: {prediction[0]:.2f}')
