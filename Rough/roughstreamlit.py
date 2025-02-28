import streamlit as st
import qrcode

st.title("🖼 QR Code Generator")

qr_link = st.text_input("🔗 Enter your URL/Link:")

if st.button("Generate QR Code") and qr_link:
    img = qrcode.make(qr_link)
    img.save("qr_code.png")

    st.image("qr_code.png", caption="📌 Your QR Code")

    st.download_button("⬇ Download QR Code", open(
        "qr_code.png", "rb"), "qr_code.png")
else:
    st.warning("⚠ Please provide a valid URL!")
