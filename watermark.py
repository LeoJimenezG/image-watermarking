from PIL import Image
from typing import cast


class Watermark:
    def __init__(self) -> None:
        """
           Initialize the object with preset settings
           :return: returns None
        """

        self.image: Image = cast(Image, None)
        self.watermark: Image = cast(Image, None)
        self.side: int = cast(int, None)
        # (left, upper, right, lower) where each value is based on the left corner (0, 0)
        self.positions: list = []

    def watermark_image(self, image: Image, watermark: Image, position: int) -> Image or None:
        """
        :param image: takes an Image object from PIL (pillow) to be watermarked
        :param watermark: takes an Image object from PIL (pillow) to mark the image
        :param position: takes a single option from preset positions
        :return: returns the watermarked image, being an Image object from PIL (pillow)
        """

        try:
            self.image = image
            self.watermark = watermark

            self.scale_watermark()

            self.image.paste(self.watermark, self.positions[position])

            return self.image
        except Exception as e:
            print(f"There has been an error when processing 'image': {e}")
            return None

    def set_positions(self):
        self.positions = [
            (0, 0, self.side, self.side),  # left upper corner
            (self.side * 3, 0, self.side * 4, self.side),  # right upper corner
            (0, self.side * 3, self.side, self.side * 4),  # left lower corner
            (self.side * 3, self.side * 3, self.side * 4, self.side * 4)  # right lower corner
        ]

    def scale_watermark(self) -> None:
        # This process is considering that the image size if properly scaled, being as close as possible to a square

        self.side = self.image.size[0] // 4

        self.watermark = self.watermark.resize((self.side, self.side))

        self.set_positions()
