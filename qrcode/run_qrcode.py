from main import make

# Define the data to encode
data = "https://google.com"

# Create a QR code image
qr_image = make(
    data=data,
    version=5,  # Control size (1-40)
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size
)


# Save the image
qr_image.save("qrcode.png")
print("QR code saved as 'qrcode.png'")
