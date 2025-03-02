import streamlit as st
import unit_data

# Title and Subtitle
st.markdown("<h1 style='text-align: center; color:#ef233c;' >Unit Converter</h1>",
            unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color:gray;' >Convert values between different measurement units with ease!</h5>",
            unsafe_allow_html=True)

# Select Measurement Type
category = st.selectbox(
    "Select Measurement Type", unit_data.conversion_data.keys(), key="category", help="Choose the type of measurement (e.g., Length, Weight, Temperature)")


# Storing Category into Variable to prevent Same Category in both Inputs by default
units = unit_data.conversion_data[category]
# Columns for input and output fields
col1, col2, col3 = st.columns([4, 1, 4])
# Select the type of measurement
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

# Input Value
input_value = st.number_input(
    "Input Value", 1, help="Enter the amount you want to convert")


# Conversion Function
def conversion_function(convert_from, convert_to, input_value):
    conversion_formula = ""
    if convert_from == "Inch" and convert_to == "Centimetre":
        conversion_formula = "multiply the length value by 2.54"
        return input_value * 2.54, conversion_formula
    elif convert_from == "Centimetre" and convert_to == "Inch":
        conversion_formula = "divide the length value by 2.54"
        return input_value * 0.393701, conversion_formula
    else:
        return input_value, conversion_formula


# Calling the Conversion Function
output_result, conversion_formula = conversion_function(
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
    >{input_value} {convert_from} = <span style="font-size: 25px; font-weight: 900;   color: white;">{output_result:.4f}</span>{convert_to}</div>
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
      {conversion_formula}
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""<p style="color: #2f3038">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
