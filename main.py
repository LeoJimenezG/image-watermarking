from ui import UI
from PIL import Image

interface = UI()
im = Image.open("tomate.png")
interface.set_image(image=im)
interface.keep_open()
