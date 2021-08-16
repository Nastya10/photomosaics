from PIL import Image
import photomosaics
import colorsys
from PIL import Image
import glob

WIDTH_OF_INSERTS = 100
HEIGHT_OF_INSERTS = 100
image_properties = dict()
parts_of_image = dict()

file = input("Введите название первого файла: ")
file1 = input("Введите название первого файла: ")

image = Image.open("photo/" + file + ".jpg")
image1 = Image.open("photo/" + file1 + ".jpg")
(width, height) = image.size
#image.show()
#image.resize((20, 20), Image.ANTIALIAS)
#image = photomosaics.resize(image, 30, 30)
#image1.show()
#image = photomosaics.resize(image1, 30, 30)
image.show()
photomosaics.insert_image(image, image1, (30, 30))
image.show()
image = photomosaics.resize(image, 30, 30)
image.show()
photomosaics.add_image(file, image, parts_of_image)
photomosaics.add_image(file1, image1, parts_of_image)
print(parts_of_image)
print(photomosaics.distance(tuple(dict.values(parts_of_image))[0], tuple(dict.values(parts_of_image))[1]))
#print(photomosaics.image_splitting(image, 15, 15))

