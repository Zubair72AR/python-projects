import streamlit as st
import unit_data as cd
from decimal import Decimal

st.markdown("<h1 style='text-align: center; color:#ef233c;' >Unit Converter</h1>",
            unsafe_allow_html=True)  # Main Title
st.markdown("<h5 style='text-align: center; color:gray;' >Convert values between different measurement units with ease!</h5>",
            unsafe_allow_html=True)  # Subtitle

category = st.selectbox(
    "Select Measurement Type", cd.conversion_data.keys(), key="category", help="Choose the type of measurement (e.g., Length, Weight, Temperature)")  # Select Measurement Type

# Storing Category into Variable to prevent Same Category in both Inputs by default
units = cd.conversion_data[category]
col1, col2, col3 = st.columns([4, 1, 4])  # Columns for input and output fields

# Select the type of Units field
with col1:
    convert_from = st.selectbox("Convert From", units, key="convert_from",
                                help="Select the unit you want to convert from")
with col2:
    st.write("<h1 style='text-align: center;' >=</h1>",
             unsafe_allow_html=True)
# Index Number If else to prevent Same Category in both Inputs by default
with col3:
    convert_to = st.selectbox("Convert To", units, index=1 if len(
        units) > 1 else 0, key="convert_to", help="Select the unit you want to convert to")

input_value = st.number_input(
    "Input Value", min_value=0.1, help="Enter the amount you want to convert")  # Input Value


def conversion_function(convert_from, convert_to, input_value):  # Convert function
    if category == "Temperature":  # if Measurement type is Temperature
        if convert_from == "Degree Celsius":
            if convert_to == "Fahrenheit":  # if Degree Celsius to Fahrenheit
                result = (input_value * 9/5 + 32)  # Conversion Calculation
                conversion_formula = (
                    f"({input_value}°C x 9/5) + 32 = {result:.2f}°F")
                return f"{result:.2f}", conversion_formula
            elif convert_to == "Kelvin":  # if Degree Celsius to Kelvin
                result = input_value + 273.15  # Conversion Calculation
                conversion_formula = (
                    f"{input_value}°C + 273.15 = {result:.2f}K")
                return f"{result:.2f}", conversion_formula
            else:
                conversion_formula = (f"{input_value}°C")
                return input_value, conversion_formula

        elif convert_from == "Fahrenheit":
            if convert_to == "Degree Celsius":  # if Fahrenheit to Degrees Celsius
                result = (input_value - 32) * 5/9  # Conversion Calculation
                conversion_formula = (
                    f"({input_value}°F - 32) x 5/9 = {result:.2f}°C")
                return f"{result:.2f}", conversion_formula
            elif convert_to == "Kelvin":  # if Fahrenheit to Kelvin
                result = (input_value - 32) * 5/9 + \
                    273.15  # Conversion Calculation
                conversion_formula = (
                    f"({input_value}°F - 32) x 5/9 + 273.15 = {result:.2f}K")
                return f"{result:.2f}", conversion_formula
            else:
                conversion_formula = (f"{input_value}°F")
                return input_value, conversion_formula

            #     return (input_value - 32) * 5/9 + 273.15
            # else:
            #     return input_value
        elif convert_from == "Kelvin":
            if convert_to == "Degree Celsius":  # if Kelvin to Degrees Celsius
                result = input_value - 273.15  # Conversion Calculation
                conversion_formula = (
                    f"({input_value}K - 273.15 = {result:.2f}°C")
                return f"{result:.2f}", conversion_formula
            elif convert_to == "Fahrenheit":  # if Kelvin to Fahrenheit
                result = (input_value - 273.15) * 9/5 + \
                    32  # Conversion Calculation
                conversion_formula = (
                    f"({input_value}K - 273.15) x 9/5 + 32 = {result:.2f}°F")
                return f"{result:.2f}", conversion_formula
            else:
                conversion_formula = (f"{input_value}K")
                return input_value, conversion_formula
    else:  # Rest Categories
        mater_value = float(input_value) * \
            float(cd.conversion_data[category][convert_from])
        converted_value = mater_value / \
            float(cd.conversion_data[category][convert_to])
        conversion_formula = f"( {convert_from} {cd.conversion_data[category][convert_from]:,} ) x ( Input Value {input_value:,} ) / ( {convert_to} {cd.conversion_data[category][convert_to]:,} )"
        # result Decimals Display Filters
        if abs(converted_value) < Decimal("1e-4") or abs(converted_value) > Decimal("1e+6"):
            return f"{converted_value:.4e}", conversion_formula
        else:
            return f"{converted_value:.2f}", conversion_formula


# Calling the Conversion Function
output_result, formula = conversion_function(
    convert_from, convert_to, input_value)


# Result Display
st.markdown(f"""
<div
      style="
        padding: 10px;
        border-radius: 8px;
        background: linear-gradient(135deg, #d90429, #ef233c);
        color: #0E1117;
        font-size: 20px;
        font-weight: 600;
        margin-top: 5px;
        margin-bottom: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        white-space: nowrap;
      "
    >{input_value} {convert_from} = <span style="font-size: 25px; font-weight: 900;   color: white;">{output_result}</span>{convert_to}</div>
""", unsafe_allow_html=True)

# Display Conversion Formula
st.markdown(f"""
<div style="
        display: flex;
        justify-content: start;
        align-items: center;
        gap: 10px;
        color: gray;
        margin-bottom: 15px;">
      <span
        style="
        padding: 2px 10px;
        background: linear-gradient(135deg, #ffc300, #ffd60a);
        border-radius: 5px;
        color: #0E1117;
        font-weight: 600;
        "
        >Formula</span
      >
      {formula}
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""<p style="color: #2f3038">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
