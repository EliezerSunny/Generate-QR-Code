import qrcode

# Prompt the user for data to be encoded
data = input("Enter the data to be encoded in the QR code: ")

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code
    border=4,  # border size
)

# Add data to the QR Code instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("image/qrcode.png")

print("QR code generated and saved as qrcode.png")
