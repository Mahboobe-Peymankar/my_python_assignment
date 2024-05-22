import qrcode

name = input ( "please enter your name ..." )
phonenumber = input ( "please enter your cell phone number..." )

name_phone = name + "|" + phonenumber

img = qrcode.make ( name_phone )
img.save ( "MyQRCode.png" )