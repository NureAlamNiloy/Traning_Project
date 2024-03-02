import qrcode
x = input("Enter a code = ")
img=qrcode.make(x)
img.save("qr.png")