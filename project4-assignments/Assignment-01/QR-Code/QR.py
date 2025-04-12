#  QR code encoder / decoder Python Project
import qrcode

data = "Don't forget to subscribe!"

# img = qrcode.make(data)

# img.save('E:/GI-AIWMD/Quarter 3/Sir Zia Project/CLASSPROJECTS/project4-assignments/Assignment-01/QR-Code/myqrcode.png')

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="white")
img.save('E:/GI-AIWMD/Quarter 3/Sir Zia Project/CLASSPROJECTS/project4-assignments/Assignment-01/QR-Code/myqrcode.png')