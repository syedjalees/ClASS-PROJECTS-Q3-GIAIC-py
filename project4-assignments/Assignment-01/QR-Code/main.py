from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('E:/GI-AIWMD/Quarter 3/Sir Zia Project/CLASSPROJECTS/project4-assignments/Assignment-01/QR-Code/myqrcode.png')

result = decode(img)
print(result)