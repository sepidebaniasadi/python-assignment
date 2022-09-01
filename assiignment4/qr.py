import qrcode
text=input("enter what you vant convert: ")
QR=qrcode.make(text)
QR.save('qrcode_result.jpg')
