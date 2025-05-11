import qrcode
from PIL import Image

data = input("Link para el QR:  ")

qr = qrcode.QRCode(version=2, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill = "black", back_color="white")

file_name = "qr_code.png"
image.save(file_name)

img = Image.open(file_name)
img.show()

