import image
import qrcode
qr=qrcode.QRCode(version=15,box_size=10,border=5)
data='Sana please PJ maat sunao'
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill='black',back_color='white')
image.save('test.png')