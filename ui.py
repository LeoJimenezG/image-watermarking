from tkinter import Tk, Canvas, Button, PhotoImage, simpledialog, filedialog, messagebox
from watermark import Watermark
from PIL import Image, ImageTk
from typing import cast
from os import getcwd


def select_file() -> Image:
    # Uses the current working directory for the initial directory and only accepts png and jpg or jpeg
    # files, could add more files according to PIL Image compatibility. This works with image outside the cwd.

    workingDirectory: str = getcwd()
    fileTypes: tuple = (
        ("PNG files", "*.png"),
        ("JPEG files", ("*.jpeg", "*.jpg"))
    )

    openImage: str = filedialog.askopenfilename(title="Open image", initialdir=workingDirectory, filetypes=fileTypes)
    image: Image = Image.open(openImage)

    return image


class UI:
    def __init__(self) -> None:
        """
        Initialize the interface with preset settings
        :return: returns None
        """

        self.__rootSize: tuple = (1000, 1000)  # Width - Height
        self.__canvasSize: tuple = (1000, 800)  # Width - Height
        self.__font: tuple = ("Courier", 20, "normal")

        self.__originalImage: Image = cast(Image, None)
        self.__originalMark: Image = cast(Image, None)
        self.__position: int = cast(int, None)
        self.__watermarked: bool = False

        self.__root: Tk = Tk()
        self.__root.title("Image Watermarking")
        self.__root.config(padx=5, pady=5, width=self.__rootSize[0], height=self.__rootSize[1])
        self.__root.resizable(False, False)

        self.__canvas: Canvas = cast(Canvas, None)
        self.__canvasImage: PhotoImage = cast(PhotoImage, None)

        self.__selectImageButton: Button = Button(
            self.__root, text="Select Image", command=self.__select_image, font=self.__font
        )
        self.__selectImageButton.grid(column=0, row=0, sticky="nsew")
        self.__selectMarkButton: Button = Button(
            self.__root, text="Select Mark", command=self.__select_mark, font=self.__font
        )
        self.__selectMarkButton.grid(column=1, row=0, sticky="nsew")
        self.__selectPosButton: Button = Button(
            self.__root, text="Select Position", command=self.__select_position, font=self.__font
        )
        self.__selectPosButton.grid(column=2, row=0, sticky="nsew")
        self.__watermarkButton: Button = Button(
            self.__root, text="Watermark Image", command=self.__watermark_image, font=self.__font
        )
        self.__watermarkButton.grid(column=3, row=0, sticky="nsew")
        self.__saveButton: Button = Button(
            self.__root, text="Save Watermarked", command=self.__save_image, font=self.__font
        )
        self.__saveButton.grid(column=4, row=0, sticky="nsew")

    def __select_image(self) -> None:
        openImage: str = select_file()

        self.__set_canvas_image(image=openImage)

        return None

    def __select_mark(self) -> None:
        openImage: str = select_file()

        self.__originalMark = openImage

        return None

    def __select_position(self) -> None:
        while True:
            position: int = simpledialog.askinteger(
                title="Select Position", prompt="Introduce the corner position you want to mark (1-4):"
            )
            if 0 < position < 5:
                break
            else:
                messagebox.showwarning(message="Try again! Introduce a valid position.")

        self.__position = position

        return None

    def __watermark_image(self) -> None:
        if self.__originalImage and self.__originalMark and self.__position:
            wk: Watermark = Watermark()
            result: Image = wk.watermark_image(
                image=self.__originalImage, watermark=self.__originalMark, position=self.__position - 1
            )
            self.__set_canvas_image(image=result)

            self.__watermarked = True
        else:
            messagebox.showwarning(
                message="You need to select all the required elements first!"
            )

        return None

    def __save_image(self) -> None:
        if self.__watermarked:
            saveImage: str = filedialog.asksaveasfilename(
                defaultextension=".jpeg",
                filetypes=(
                    ("PNG files", "*.png"),
                    ("JPEG files", ("*.jpeg", "*.jpg"))
                )
            )

            if saveImage:
                try:
                    self.__originalImage.save(saveImage)
                    print("Image successfully saved")
                except Exception as e:
                    print(f"Error saving the image: {e}")

            self.__originalImage = None
            self.__originalMark = None
            self.__position = None
            self.__watermarked = False

        return None

    def __set_canvas_image(self, image: Image) -> bool:
        """
        Set an image on the main window using
        :param image: an Image object from PIL (pillow) library is needed in order to proper functionality
        :return: returns True if the process didn't have errors. Otherwise, returns False
        """

        try:
            self.__originalImage = image

            if not self.__canvas:
                self.__canvas = Canvas(self.__root, width=self.__canvasSize[0], height=self.__canvasSize[1])
                self.__canvas.grid(column=0, row=1, columnspan=5)

            if image.size[0] > self.__canvasSize[0] or image.size[1] > self.__canvasSize[1]:
                resizedImage: Image = image.resize(self.__canvasSize)
                self.__canvasImage = ImageTk.PhotoImage(resizedImage)
            else:
                self.__canvasImage = ImageTk.PhotoImage(image)

            centerX: int = self.__canvasSize[0] // 2
            centerY: int = self.__canvasSize[1] // 2

            self.__canvas.delete("all")

            self.__canvas.create_image(centerX, centerY, image=self.__canvasImage)

            return True
        except Exception as e:
            print(f"Error when processing 'image' into the canvas: {e}")

            return False

    def keep_open(self) -> None:
        """
        Starts the main loop for keeping opened the window
        :return: returns None
        """

        self.__root.mainloop()

        return None
