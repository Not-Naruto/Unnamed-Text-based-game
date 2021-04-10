from PIL import Image
import pygetwindow as gw

x = Image.open('Level 1.png')
x.show()
w=gw.getWindowsWithTitle('Photos')[0]
w.activate()
w.close()