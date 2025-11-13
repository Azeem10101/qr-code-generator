import qrcode

#take URL input from user
url = input("Enter the URL to generate QR code: ").strip()
file_path = "C:\\Users\\arsha\\OneDrive\\Desktop\\Python\\MyProject\\qrcode.png"

#generate QR code
qr = qrcode.QRCode()
qr.add_data(url)

#generate the QR code and save it as an image file
img = qr.make_image()
img.save(file_path)

#let's user know that the QR code has been generated
print("QR code generated!")
