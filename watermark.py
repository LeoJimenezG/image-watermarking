from PIL import Image
from typing import cast


class Watermark:
    def __init__(self) -> None:
        """
           Initialize the object with preset settings
           :return: returns None
        """

        self.__image: Image = cast(Image, None)
        self.__watermark: Image = cast(Image, None)
        self.__squares: int = 8
        self.__widthSide: int = cast(int, None)
        self.__heightSide: int = cast(int, None)
        self.__positions: list = []

    def watermark_image(self, image: Image, watermark: Image, position: int) -> Image or None:
        """
        :param image: takes an Image object from PIL (pillow) to be watermarked
        :param watermark: takes an Image object from PIL (pillow) to mark the image
        :param position: takes a single option from preset positions
        :return: returns the watermarked image, being an Image object from PIL (pillow)
        """

        try:
            self.__image = image
            self.__watermark = watermark

            self.__scale_watermark()

            self.__image.paste(self.__watermark, self.__positions[position])

            return self.__image
        except Exception as e:
            print(f"There has been an error when processing 'image': {e}")
            return None

    def __set_positions(self) -> None:
        # Calculates the four positions of each corner according to the resulting sides,
        # dividing the image into self.squares * self.squares.

        # (left, upper, right, lower) where each value is based on the left corner (0, 0).
        self.__positions = [
            # left upper corner
            (
                0, 0, self.__widthSide, self.__heightSide
            ),
            # right upper corner
            (
                self.__widthSide * (self.__squares - 1), 0, self.__widthSide * self.__squares, self.__heightSide
            ),
            # left lower corner
            (
                0, self.__heightSide * (self.__squares - 1), self.__widthSide, self.__heightSide * self.__squares
            ),
            # right lower corner
            (
                self.__widthSide * (self.__squares - 1), self.__heightSide * (self.__squares - 1),
                self.__widthSide * self.__squares, self.__heightSide * self.__squares
            )
        ]

        return None

    def __scale_watermark(self) -> None:
        # Sets the sides according to the image size and the number of squares. Then, scales
        # the image using the calculated sides.

        try:
            self.__widthSide = self.__image.size[0] // self.__squares
            self.__heightSide = self.__image.size[1] // self.__squares

            self.__watermark = self.__watermark.resize((self.__widthSide, self.__heightSide))

            self.__set_positions()

        except Exception as e:
            print(f"There has been an error when resizing 'watermark': {e}")

        finally:
            return None
