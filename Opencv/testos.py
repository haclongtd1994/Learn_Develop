import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

for roots, dirs, files in os.walk(image_dir):
    for dir in dirs:
        print("DIR: {0}".format(dir))
        
    for file in files:
        print("FILE: {0}".format(file))