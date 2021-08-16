from PIL import Image
import photomosaics
import glob

image_properties = dict()
parts_of_image = dict()
IMAGE_WIDTH = int(input("Введите ширину кусочка картинки: "))
IMAGE_HEIGHT = int(input("Введите высоту кусочка картинки: "))

file = input("Введите название главной картики: ")
main_image = Image.open("main_photo/" + file + ".jpg")
parts_of_image = photomosaics.image_splitting(main_image, IMAGE_WIDTH, IMAGE_HEIGHT)

number_of_images = 0
images = glob.glob("all_photoes/*.jpg")
for image_name in images:
    image = Image.open(image_name)
    photomosaics.add_image(image_name, image, image_properties)
    number_of_images += 1

min_distance = 2        #Максимальное значение теоремы пифагора по 3 значением с диапазоном от 0 до 1 это корень из 3
k = 0
image_paste_name = ''
for i in parts_of_image:
    for j in image_properties:
        new_distance = photomosaics.distance(image_properties[j], (parts_of_image[i][2], parts_of_image[i][3], parts_of_image[i][4]))
        if new_distance <= min_distance:
            min_distance = new_distance
            image_paste_name = j

        if k >= number_of_images:
            k = 0
            image = Image.open(image_paste_name)
            image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
            Image.Image.paste(main_image, image, (parts_of_image[i][0], parts_of_image[i][1]))
            min_distance = 2
        k += 1

main_image.show()