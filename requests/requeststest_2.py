import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpaperaccess.com/full/630848.jpg")

print("Status code", r.status_code)

image = Image.open(BytesIO(r.content)) #binary data

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")