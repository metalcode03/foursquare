import numpy as np
from PIL import Image, ImageDraw

img = Image.open("boobs.jpg")
img1 = Image.open("img/foursquare.jpg")
img.show()
if img.height > img.width:
    img = img.crop((0,0, img.width, img.height / 1.3))
elif img.width > img.height:
    img = img.crop((img.width / 6, 0, img.width / 1.1, img.height))

height, width = img.size
lum_img = Image.new('L', [height, width], 0)

draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0, 0), (height, width)], 0, 360,
              fill=255, outline="white")
img_arr = np.array(img)
lum_img_arr = np.array(lum_img)
display = Image.fromarray(lum_img_arr)
display.show()
final_img_arr = np.dstack((img_arr, lum_img_arr))
play = Image.fromarray(final_img_arr)
play.thumbnail((255, 255), Image.ANTIALIAS)
play.show()
play.save("pic.png")

img2 = Image.open("pic.png")
# Pasting img2 image on top of img1
# starting at coordinates (0, 0)
img1.paste(img2, (60, 440), mask=img2)

# Displaying the image
img1.save("newdata.jpg")
img1.show("newdata.jpg")
