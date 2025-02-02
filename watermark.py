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
        self.positions: list = [
            (0, 0, self.side, self.side),  # left upper corner
            (self.side * 3, 0, self.side * 4, self.side),  # right upper corner
            (0, self.side * 3, self.side, self.side * 4),  # left lower corner
            (self.side * 3, self.side * 3, self.side * 4, self.side * 4)  # right lower corner
        ]

    def watermark_image(self, image: Image, watermark: Image, position: int) -> Image:
        """
        :param image: takes an Image object from PIL (pillow) to be watermarked
        :param watermark: takes an Image object from PIL (pillow) to mark the image
        :param position: takes a single option from preset positions
        :return: returns the watermarked image, being an Image object from PIL (pillow)
        """

        self.image = image
        self.watermark = watermark
