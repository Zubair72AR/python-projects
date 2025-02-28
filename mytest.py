import qrcode


def generate_qr(link):
    if link:
        img = qrcode.make(link)
        img.save("qr_code.png")
        print(f"✅ QR Code generated and saved as 'qr_code.png' for: {link}")
    else:
        print("⚠ Please provide a valid URL!")


qr_link = input("🔗 Enter your URL/Link: ")
generate_qr(qr_link)
