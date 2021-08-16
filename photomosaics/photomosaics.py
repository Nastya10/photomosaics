from PIL import Image
import colorsys
import math

#Функция меняет размер изображения
def resize(image, new_width, new_height):
    image = image.resize((new_width, new_height), Image.ANTIALIAS)
    return image

#Функция выводит средний цвет изображения в hsv
def average_value(image, x0 = 0, y0 = 0, x1 = 0, y1 = 0):       #картинка, координаты начала и конца кусочка
    if x1 == 0 and y1 == 0:
        (x1, y1) = image.size

    pix = image.load()
    H = 0
    S = 0
    V = 0
    number_of_pixels = 0

    for i in range(x0, x1):
        for j in range(y0, y1):
            pix_hsv = colorsys.rgb_to_hsv(pix[i, j][0] / 255, pix[i, j][1] / 255, pix[i, j][2] / 255)
            H += pix_hsv[0]
            S += pix_hsv[1]
            V += pix_hsv[2]

            number_of_pixels += 1

    return (H / number_of_pixels, S / number_of_pixels, V / number_of_pixels)

#Функция создаёт словарь, значения которого являются координаты кусочков и значения среднего hsv
def image_splitting(image, width_of_piece, height_of_piece):
    parts_of_image = dict()
    (width, height) = image.size
    k = 0

    for i in range(width // width_of_piece):
        for j in range(height // height_of_piece):

            average_color_of_piece = average_value(image, i * width_of_piece, j * height_of_piece,
                                                         (i + 1) * width_of_piece, (j + 1) * height_of_piece)

            parts_of_image.update({k : (i * width_of_piece, j * height_of_piece,
                                        average_color_of_piece[0], average_color_of_piece[1], average_color_of_piece[2])})

            k += 1
    return parts_of_image

#Функция определяет наилучшее совпадение параметров
def distance(coordinates1, coordinates2):
    return math.sqrt(math.pow((float(coordinates1[0]) - float(coordinates2[0])), 2) +
                     math.pow((float(coordinates1[1]) - float(coordinates2[1])), 2) +
                     math.pow((float(coordinates1[2]) - float(coordinates2[2])), 2))

#Функция добавляет параметры заданной картинки в общий славарь
def add_image(image_name, image, image_properties):
    average_color = average_value(image)
    image_properties.update({image_name : (average_color[0], average_color[1], average_color[2])})
