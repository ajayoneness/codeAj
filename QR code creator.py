import pyqrcode
import png
from pyqrcode import QRCode

link = input ('web link : ')
url=pyqrcode.create(link)
url.png(f'{link[4:10]}.png',scale = 6)
print(f'QRcode is sucessfully created with name {link[4:10]}.png')
