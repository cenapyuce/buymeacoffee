# Wait 5 minute i drink coffee
from time import sleep
import io
import qrcode
import os
# My link https://www.buymeacoffee.com/cenapp

link = "https://www.buymeacoffee.com/cenapp"

qr = qrcode.QRCode()
qr.add_data(link)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
qr = f.read()
def coffee():
    os.system('cls')
    for i in range(5):
        print("""
      .-~~-.             Wait 5 minute i cook coffee
    ,|`-__-'|
    ||      |            If you want to buy me a coffee, read the qr.
    `|      |  
      `-__-'             link: {link}
        """.format(link=link))
        print(qr)
        sleep(60)
        os.system("cls")

coffee()