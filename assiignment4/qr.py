import qrcode
text=input("enter what you want convert: ")
QR=qrcode.make(text)
QR.save('qrcode_result.jpg')
