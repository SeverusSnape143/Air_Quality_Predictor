import streamlit as st
import base64
import pandas as pd
import numpy as np
from index import predictor
import streamlit as st
@st.cache_data
def get_image(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image = get_image("C:/Users/Dell/Desktop/Air Quality/Background.jpg")
 # Replace with the path to your background image
background_image = f""" <style>
[data= testid = "stAppViewContainer"] {{background-image: url("C:/Users/Dell/Desktop/Air Quality/Background.jpg"),
background-size = cover;}}
</style>"""
st.title("Air Quality Predictor")
st.subheader('Enter the value of Following Parameters', divider='rainbow')
def get_user_input_with_name(variable_name, min_limit, max_limit):
    user_input = st.number_input(f"Enter value for {variable_name}:", min_value=min_limit, max_value=max_limit, key=variable_name)
    st.caption(f"Enter the value between {min_limit} and {max_limit}")
    return user_input

# Define variable names and limits
variables_info = [
    ("CO(GT)", 0, 30), ("PT08.S1(CO)", 0, 3000),("NMHC(GT)", 0,2000), ("C6H6(GT)", 0, 100),
    ("PT08.S2(NMHC)", 0, 3000),("NOx(GT)", 0, 2000),("PT08.S3(NOx)", 0, 3000),("NO2(GT)", 0, 500),
    ("PT08.S4(NO2)", 0, 3000), ("PT08.S5(O3)", 0, 3000), ("T", 0, 80), ("AH", 0, 5)
]

# Collect user input for each variable
input_values = []

for variable_name, min_limit, max_limit in variables_info:
    user_input = get_user_input_with_name(variable_name, min_limit, max_limit)
    input_values.append(user_input)



parameters = np.array(input_values).reshape(1,-1)

click = st.button("           Predict               ")
air_quality = predictor(parameters)
if click:
    st.write("""
    <div style="font-family: Times New Roman, sans-serif; color: white;">
     The Relative Humidity is:
    </div>
    """, air_quality,
    unsafe_allow_html=True
)

