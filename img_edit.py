from PIL import Image
import random

def construct_img(query, base, size):
    img1 = Image.open("queries/"+query+".png")
    #img1.show()

    img2 = Image.open(base)
    img2 = img2.resize((size,size), Image.ANTIALIAS)

    img2.paste(img1, ( int(250-img1.size[0]/2), int(250-img1.size[1]/2) ), mask=img1)
    img2.save("images/out.png")
