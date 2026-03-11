import qrcode
import os

print("Enter the website you need to make QR Code")
s = input()

q = qrcode.QRCode(version=1, box_size=10, border=5)
q.add_data(s)
q.make(fit=True)

img = q.make_image(fill_color="black", back_color="white")

# get script directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# create static folder
static_folder = os.path.join(base_dir, "static")
os.makedirs(static_folder, exist_ok=True)

# save image
img_path = os.path.join(static_folder, "qrcode.jpg")
img.save(img_path)

print("QR Code saved at:", img_path)