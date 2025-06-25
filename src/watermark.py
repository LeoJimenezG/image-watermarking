from PIL import Image
from typing import cast


class Watermark:
    def __init__(self) -> None:
        """
        Initialize the object with pre-configured settings.
        :return: returns nothing.
        """
        self.__image: Image.Image = cast(Image.Image, None)
        self.__watermark: Image.Image = cast(Image.Image, None)
        self.__positions: list = []
        self.__squares: int = 8  # Squares that divide the full image (1/64).
        self.__width: int = 0
        self.__height: int = 0

    def __scale_watermark(self) -> None:
        """
        Calculates the watermark sides according to the original image
        size and the configured number of squares.
        Then, scales the image using the calculated sides.
        """
        try:
            self.__width = self.__image.size[0] // self.__squares
            self.__height = self.__image.size[1] // self.__squares
            self.__watermark = self.__watermark.resize(
                (self.__width, self.__height)
            )
            self.__set_positions()
        except Exception as e:
            print(f"There has been an error when resizing 'watermark': {e}")
        finally:
            return None

    def __set_positions(self) -> None:
        """
        Calculates the four positions of each corner according to
        the corresponding sides of the image, dividing the image on
        an specific amount of squares.
        """
        # (left, upper, right, lower)
        # Each value is based on the left corner (0, 0).
        self.__positions = [
            # left upper corner
            (
                0, 0, self.__width, self.__height
            ),
            # right upper corner
            (
                self.__width * (self.__squares - 1), 0,
                self.__width * self.__squares, self.__height
            ),
            # left lower corner
            (
                0, self.__height * (self.__squares - 1),
                self.__width, self.__height * self.__squares
            ),
            # right lower corner
            (
                self.__width * (self.__squares - 1),
                self.__height * (self.__squares - 1),
                self.__width * self.__squares,
                self.__height * self.__squares
            )
        ]
        return None

    def watermark_image(self,
                        image: Image.Image,
                        watermark: Image.Image,
                        position: int) -> Image.Image or None:
        """
        :param image: takes the PIL Image object to be marked.
        :param watermark: takes the PIL Image object to mark with.
        :param position: takes a single integer representing a position.
        :return: returns the marked image as a PIL Image object.
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
