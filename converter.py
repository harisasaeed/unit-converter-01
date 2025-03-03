import streamlit as st
import pandas as pd
import os
from io import BytesIO


# Function to convert units
def convert_length(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
    }
    
    if from_unit not in units or to_unit not in units:
        return None
    
    return value * (units[from_unit] / units[to_unit])

# Title of the app
st.title("♻️ Unit Converter")

# Select input value
value = st.number_input("Enter the value to convert:", value=1.0)

# Select input unit
from_unit = st.selectbox("From unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet'])

# Select output unit
to_unit = st.selectbox("To unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet'])

# Automatic conversion
result = convert_length(value, from_unit, to_unit)

if result is not None:
    st.write(f"{value} {from_unit} is equal to {result:.6f} {to_unit}.")
else:
    st.write("Invalid units selected.")
