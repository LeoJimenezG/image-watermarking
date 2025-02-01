from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk


class UI:
    def __init__(self) -> None:
        """
        Initialize the interface with preset settings
        :return: returns None
        """

        self.rootSize = (1000, 1000)  # Width - Height
        self.canvasSize = (1000, 800)  # Width - Height
        self.font = ("Courier", 24, "normal")

        self.root = Tk()
        self.root.title("Image Watermarking")
        self.root.config(width=self.rootSize[0], height=self.rootSize[1], padx=5, pady=5)
        self.root.resizable(False, False)

        self.canvas = None
        self.originalImage = None
        self.canvasImage = None

        self.selectImageButton = Button(self.root, text="Select Image", command="", font=self.font)
        self.selectImageButton.grid(column=0, row=0)
        self.selectMarkButton = Button(self.root, text="Select Mark", command="", font=self.font)
        self.selectMarkButton.grid(column=1, row=0)
        self.selectPosButton = Button(self.root, text="Select Position", command="", font=self.font)
        self.selectPosButton.grid(column=2, row=0)
        self.saveButton = Button(self.root, text="Save Watermarked", command="", font=self.font)
        self.saveButton.grid(column=3, row=0)

        # TODO: create and add the functions for each button

    def set_image(self, image: Image) -> bool:
        """
        Set an image on the main window using
        :param image: an Image object from PIL (pillow) library is needed in order to proper functionality
        :return: returns True if the process didn't have errors. Otherwise, returns False
        """

        try:
            self.originalImage = image

            if not self.canvas:
                self.canvas = Canvas(self.root, width=self.canvasSize[0], height=self.canvasSize[1])
                self.canvas.grid(column=0, row=1, columnspan=4)

            if image.size[0] > self.canvasSize[0] or image.size[1] > self.canvasSize[1]:
                resizedImage = image.resize(self.canvasSize)
                self.canvasImage = ImageTk.PhotoImage(resizedImage)
            else:
                self.canvasImage = ImageTk.PhotoImage(image)

            centerX = self.canvasSize[0] // 2
            centerY = self.canvasSize[1] // 2

            self.canvas.delete("all")

            self.canvas.create_image(centerX, centerY, image=self.canvasImage)
            return True
        except Exception as e:
            print(f"Error when processing 'image' into the canvas: {e}")
            return False

    def keep_open(self) -> None:
        """
        Starts the main loop for keeping opened the window
        :return: returns None
        """

        self.root.mainloop()
