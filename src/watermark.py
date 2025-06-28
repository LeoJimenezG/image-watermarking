from PIL import Image, ImageEnhance
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

    def __transform_watermark(self, transparency: int) -> None:
        """
        Calculates the watermark dimensions according to the original image
        size and the configured number of squares.
        Then, transforms the image using the calculated dimensions.
        """
        try:
            # Get the watermark dimensions from the orignial image.
            self.__width = self.__image.size[0] // self.__squares
            self.__height = self.__image.size[1] // self.__squares
            # Convert the watermark into RGBA format.
            self.__watermark = self.__watermark.convert("RGBA")
            # Change the watermark alpha (transparency).
            alpha = self.__watermark.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(transparency)
            self.__watermark.putalpha(alpha)
            # Resize the watermark using the calculated dimensions.
            self.__watermark = self.__watermark.resize(
                (self.__width, self.__height)
            )
            # Create the positions based on the calculated dimensions.
            self.__set_positions()
        except Exception as e:
            print("Error when transforming watermark:", e)
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
                        position: int,
                        transparency: float) -> Image.Image or None:
        """
        :param image: takes the PIL Image object to be marked.
        :param watermark: takes the PIL Image object to mark with.
        :param position: takes a single integer representing a position.
        :return: returns the marked image as a PIL Image object.
        """
        try:
            self.__image = image
            self.__watermark = watermark
            self.__transform_watermark(transparency)
            self.__image.paste(self.__watermark, self.__positions[position])
            return self.__image
        except Exception as e:
            print("Error when processing the image:", e)
            return None
