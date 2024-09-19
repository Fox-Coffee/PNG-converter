import os
from PIL import Image

path = './images/'
files = os.listdir(path)

for file in files:
    if file.endswith('.webp'):
        im = Image.open(path + file)
        im.save(file.replace('.webp', '.png'), 'png')
    elif file.endswith('.jpg'):
        im = Image.open(path + file)
        im.save(file.replace('.jpg', '.png'), 'png')
    elif file.endswith('.jpeg'):
        im = Image.open(path + file)
        im.save(file.replace('.jpeg', '.png'), 'png')