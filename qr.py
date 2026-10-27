
import qrcode

# Enter the text or URL
data = input("Enter text or URL: ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("my_qr.png")

print("QR code generated successfully!")
print("Saved as my_qr.png")
