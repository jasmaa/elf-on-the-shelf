from PIL import Image
import random

def construct_img(query, base, size):
    img1 = Image.open("queries/"+query+".png")
    #img1.show()

    img2 = Image.open("images/"+base)
    img2 = img2.resize((size,size), Image.ANTIALIAS)

    img2.paste(img1, (random.randint(100,size-100), random.randint(100,size-100)), mask=img1)
    img2.save("images/res_out.png")
