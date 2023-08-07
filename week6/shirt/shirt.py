import sys
from PIL import Image, ImageOps
import os

extensions = [".jpg" , ".jpeg", ".png"]
if len(sys.argv) < 3:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")
elif os.path.splitext(sys.argv[1])[1] not in extensions:
    sys.exit("Invalid input")
elif os.path.splitext(sys.argv[2])[1] not in extensions:
    sys.exit("Invalid output")
elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    with Image.open(sys.argv[1]) as inim:
        inim = ImageOps.fit(inim,size)
        inim.paste(shirt, mask= shirt)
        inim.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
