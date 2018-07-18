from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im

def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)

def serbia(im):
    pixels = im.getdata()
    new_pixels = []

    for p in pixels:
        serbia.append((p[1] + 30, p[2] + 30, p[3]))


    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

im = load_img("catdog.jpg")
newim = serbia(im)
show_img(newim)
