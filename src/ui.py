from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import simpledialog, filedialog, messagebox
from watermark import Watermark
from PIL import Image, ImageTk
from typing import cast
from os import getcwd


def select_file() -> Image.Image or None:
    """
    Opens the current working directory as the initial selection. It only
    allows png, jpeg and jpg files. This works with any path, as it gets
    the absolute path of the file.
    :return: returns a PIL Image object. Or None if fails.
    """
    try:
        cwd: str = getcwd()
        file_types: list = [
            ("PNG files", "*.png"),
        ]
        abs_image_path: str = filedialog.askopenfilename(
            title="Open Image File", initialdir=cwd, filetypes=file_types
        )
        selected_img: Image.Image = Image.open(abs_image_path)
        return selected_img
    except Exception as error:
        print("Error when getting the file:", error)
        return None


class UI:
    def __init__(self) -> None:
        """
        Initialize interface with pre-configured settings.
        :return: returns nothing.
        """
        self.__root_size: list = [800, 700]  # Width - Height
        self.__font: tuple = ("Courier", 20, "normal")

        self.__original_img: Image.Image = cast(Image.Image, None)
        self.__original_mark: Image.Image = cast(Image.Image, None)
        self.__position: int = 1
        self.__transparency: float = 1.0
        self.__watermarked: bool = False

        self.__root: Tk = Tk()
        self.__root.title("Image Watermarking")
        self.__root.config(
            padx=5,
            pady=5,
            width=self.__root_size[0],
            height=self.__root_size[1]
        )
        self.__root.resizable(False, False)

        self.__canvas_img: PhotoImage = cast(PhotoImage, None)

        self.__select_img_btn: Button = Button(
            master=self.__root,
            text="Image",
            command=self.__select_image,
            font=self.__font
        )
        self.__select_img_btn.grid(column=0, row=0, sticky="nsew")

        self.__select_mark_btn: Button = Button(
            master=self.__root,
            text="Mark",
            command=self.__select_mark,
            font=self.__font
        )
        self.__select_mark_btn.grid(column=1, row=0, sticky="nsew")

        self.__select_pos_btn: Button = Button(
            master=self.__root,
            text="Position",
            command=self.__select_position,
            font=self.__font
        )
        self.__select_pos_btn.grid(column=2, row=0, sticky="nsew")

        self.__select_transparency_btn: Button = Button(
            master=self.__root,
            text="Transparency",
            command=self.__select_transparency,
            font=self.__font
        )
        self.__select_transparency_btn.grid(column=3, row=0, sticky="nsew")

        self.__watermark_btn: Button = Button(
            master=self.__root,
            text="Watermark",
            command=self.__watermark_image,
            font=self.__font
        )
        self.__watermark_btn.grid(column=4, row=0, sticky="nsew")

        self.__save_btn: Button = Button(
            master=self.__root,
            text="Save",
            command=self.__save_image,
            font=self.__font
        )
        self.__save_btn.grid(column=5, row=0, sticky="nsew")

        self.__root.update_idletasks()

        self.__root_size[0] = self.__root.winfo_width()

        self.__canvas = Canvas(
            master=self.__root,
            width=self.__root_size[0],
            height=self.__root_size[1]
        )
        self.__canvas.grid(column=0, row=1, columnspan=6, sticky="nsew")

    def __select_image(self) -> None:
        self.__set_canvas_img(image=select_file())
        return None

    def __select_mark(self) -> None:
        self.__original_mark = select_file()
        return None

    def __select_position(self) -> None:
        while True:
            try:
                position: int = simpledialog.askinteger(
                    title="Select Position",
                    prompt="Introduce the corner position for the mark (1-4):"
                )
                if 0 < position < 5:
                    break
                messagebox.showwarning(
                    message="Try again! Introduce a valid position."
                )
            except Exception as e:
                print("Error when getting the position:", e)
        self.__position = position or 1
        return None

    def __select_transparency(self) -> None:
        while True:
            try:
                transparency: int = simpledialog.askfloat(
                    title="Select Transparency",
                    prompt="Introduce the transparecy for the mark (0 - 1.0)"
                )
                if 0 <= transparency <= 1.0:
                    break
                messagebox.showwarning(
                    message="Try again! Introduce a valid transparency."
                )
            except Exception as e:
                print("Error when getting the transparency:", e)
        self.__transparency = transparency or 1.0
        return None

    def __watermark_image(self) -> None:
        try:
            if (
                self.__original_img and
                self.__original_mark and
                self.__position and
                self.__transparency
            ):
                mark: Watermark = Watermark()
                marked_img: Image.Image = mark.watermark_image(
                    image=self.__original_img,
                    watermark=self.__original_mark,
                    position=self.__position - 1,
                    transparency=self.__transparency
                )
                self.__set_canvas_img(image=marked_img)
                self.__watermarked = True
            else:
                messagebox.showwarning(
                    message="You need to select all the required elements!"
                )
        except Exception as e:
            print("Error when watermarking the image:", e)
        finally:
            return None

    def __save_image(self) -> None:
        try:
            if self.__watermarked:
                saveImage: str = filedialog.asksaveasfilename(
                    defaultextension=".png",
                    filetypes=[
                        ("PNG files", "*.png"),
                    ]
                )
                self.__original_img.save(saveImage)
                self.__original_img = None
                self.__original_mark = None
                self.__position = 1
                self.__transparency = 1.0
                self.__watermarked = False
        except Exception as e:
            print("Error when saving the watermarked image:", e)
        finally:
            return None

    def __set_canvas_img(self, image: Image.Image) -> None:
        """
        Set an image in the canvas object.
        :param image: a PIL Image object.
        :return: returns True if the process didn't have any errors.
        Returns False otherwise.
        """
        try:
            self.__original_img = image
            if (
                self.__original_img.size[0] > self.__root_size[0]
                and
                self.__original_img.size[1] > self.__root_size[1]
            ):
                resized_img: Image.Image = self.__original_img.resize(
                    tuple(self.__root_size)
                )
                self.__canvas_img = ImageTk.PhotoImage(resized_img)
            elif self.__original_img.size[0] > self.__root_size[0]:
                resized_img: Image.Image = self.__original_img.resize(
                    (self.__root_size[0], self.__original_img.size[1])
                )
                self.__canvas_img = ImageTk.PhotoImage(resized_img)
            elif self.__original_img.size[1] > self.__root_size[1]:
                resized_img: Image.Image = self.__original_img.resize(
                    (self.__original_img.size[0], self.__root_size[1])
                )
                self.__canvas_img = ImageTk.PhotoImage(resized_img)
            else:
                self.__canvas_img = ImageTk.PhotoImage(self.__original_img)
            center_x: int = self.__root_size[0] // 2
            center_y: int = self.__root_size[1] // 2
            self.__canvas.delete("all")
            self.__canvas.create_image(
                center_x, center_y,
                image=self.__canvas_img
            )
        except Exception as e:
            print("Error when showing the image in canvas:", e)
        finally:
            return None

    def keep_open(self) -> None:
        """
        Starts the main loop to keep opened the root window.
        :return: returns nothing.
        """
        self.__root.mainloop()
        return None
