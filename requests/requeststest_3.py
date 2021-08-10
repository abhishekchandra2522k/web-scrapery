import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://i.pinimg.com/originals/52/e0/b4/52e0b4cdb0add5d4d13080020506a0d9.png")

print("Status code", r.status_code)

image = Image.open(BytesIO(r.content)) #binary data

print(image.size, image.format, image.mode)

path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")