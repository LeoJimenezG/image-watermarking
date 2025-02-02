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
        self.squares: int = 8
        self.widthSide: int = cast(int, None)
        self.heightSide: int = cast(int, None)
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

    def set_positions(self) -> None:
        # Calculates the four positions of each corner according to the resulting sides,
        # dividing the image into self.squares * self.squares.

        # (left, upper, right, lower) where each value is based on the left corner (0, 0).
        self.positions = [
            # left upper corner
            (
                0, 0, self.widthSide, self.heightSide
            ),
            # right upper corner
            (
                self.widthSide * (self.squares - 1), 0, self.widthSide * self.squares, self.heightSide
            ),
            # left lower corner
            (
                0, self.heightSide * (self.squares - 1), self.widthSide, self.heightSide * self.squares
            ),
            # right lower corner
            (
                self.widthSide * (self.squares - 1), self.heightSide * (self.squares - 1),
                self.widthSide * self.squares, self.heightSide * self.squares
            )
        ]

        return None

    def scale_watermark(self) -> None:
        # Sets the sides according to the image size and the number of squares. Then, scales
        # the image using the calculated sides.

        try:
            self.widthSide = self.image.size[0] // self.squares
            self.heightSide = self.image.size[1] // self.squares

            self.watermark = self.watermark.resize((self.widthSide, self.heightSide))

            self.set_positions()

        except Exception as e:
            print(f"There has been an error when resizing 'watermark': {e}")

        finally:
            return None
