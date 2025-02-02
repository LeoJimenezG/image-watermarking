from ui import UI
from watermark import Watermark
from PIL import Image

interface = UI()
watermarkObj = Watermark()

im = Image.open("img.jpeg")
wk = Image.open("tomate.png")

interface.set_image(image=im)
mk = watermarkObj.watermark_image(im, wk, 0)
interface.set_image(image=mk)
interface.keep_open()
