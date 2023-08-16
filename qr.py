# Python Code for QR Code

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data("https://linkedin.com/in/shraddhanagar") # Add link for OR Code
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="white") # Add color in QR code
img.save("LinkedIn.png") # Name of image 
