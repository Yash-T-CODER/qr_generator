import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=20,border=4)

data=input("Enter the url of the website for creating qr code: ").lower().strip()
qr.add_data(f"{data}")
qr.make(fit=True)
img = qr.make_image(fill_color=	"black", back_color="white")
print("Your qr code has been made.")
loc=input("Tell me the name of file so that i can save it: ")
des_loc=f"{loc}.png"
img.save(des_loc)
print(f"Your file has been made and has been stored to {des_loc}")