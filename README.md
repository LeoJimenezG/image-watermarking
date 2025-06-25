# Image Watermarking

Python GUI tool for watermarking images with a selected image at pre-defined positions, built using Tkinter and Pillow.

---

## Installation

To get this project up and runnig on your local machine, follow the next instructions.

### Prerequisites
Before anything else, make sure you have installed **Python 3.x** or more in your system.

### Steps
1. **Clone the repository:**
Open your prefered terminal and clone the project to your local machine
    ```bash
    git clone https://github.com/LeoJimenezG/image-watermarking.git
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd image-watermarking
    ```
3. **Create a Virtual Environment (Recommended):**
It's a good practice to use a virtual environment to manage project dependencies. This ensures that the project's dependencies don't interfere with other Python projects or your system's Python installation.
    * Create the virtual environment:
        ```bash
        python -m venv .venv
        ```
    * Activate the virtual environment:
        * **On macOS / Linux:**
            ```bash
            source .venv/bin/activate
            ```
        * **On Windows (Command Prompt):**
            ```bash
            .venv\Scripts\activate.bat
            ```
4. **Install Project Dependencies:**
With your virtual environment activated, install all the required libraries (like Pillow) using `pip`:
    ```bash
    pip install Pillow
    ```
5. **Run the Application:**
Finally, execute the main script to launch the Image Watermarking Application:
    ```bash
    python main.py
    ```

---

## How Does It Work?

This project provides a single, streamlined functionality built with an object-oriented approach and a graphical user interface. It allows you to apply a watermark (another image) onto a target image, placing the watermark in one of the four given corner positions.

The entire watermarking process is completed through the GUI buttons in **five steps**:

### 1. Select Image
* **Choose the Target Image**: Select the Image you wish to watermark from any directory. For convenience, it's best if the image is in the same directory as the code.
* **Display on GUI**: Once selected, the Image is shown on a Tkinter Canvas.
* **Resizing for Display**: If the Image is larger than the Canvas, it will be resized to fit. This resizing is only for display purposes and does not affect the final Watermarked Image. For optimal display, use an Image as close to a square as possible.

### 2. Select Mark
* **Choose the Mark Image**: Select an image to serve as the Mark, following a process similar to selecting the target Image.
* **Set Up the Mark**: Once selected, the Mark image is stored in a variable and prepared to use.
* **Automatic Resizing**: By default, the Mark is resized relative to the target Image's dimensions (occupying approximately 1/64 of the Image).

### 3. Select Position
* **Input the Position**: After selecting both the target Image and the Mark, you must input an integer corresponding to one of the four positions:
  * **1**: Left Upper Corner  
  * **2**: Right Upper Corner  
  * **3**: Left Lower Corner  
  * **4**: Right Lower Corner
* **Validation**: If an invalid Position is entered, the GUI will ask you to try again until a valid Position is provided, or you close the window.

### 4. Watermark Image
* **Apply the Watermark**: With the target Image, Mark, and valid Position selected, you can proceed to Watermark the image.
* **Pre-Process Checks**: Attempting to watermark without completing the previous steps will trigger a warning, and the process will not continue.
* **Display the Result**: Once successful, the Watermarked Image is displayed in the GUI. You can then choose to save it or repeat the process as needed.

### 5. Save Watermarked 
* **Save Your Work**: When satisfied with the Watermarked Image displayed on the GUI, save it to your files with a name of your choice.
* **Supported Formats**: You can save the image in PNG, JPEG, or JPG formats (the same formats supported when selecting an image).
* **Reset for Next Process**: After saving, the current selections (Image, Mark, and Position) are cleared, allowing you to start a new watermarking process.

---

## Application Configuration

### UI Class Configurations
* **Accepted File Types**:
  * You can modify the accepted file types to suit your needs, as long as they are compatible with the PIL Image Object.
  * This setting is stored in a variable named `fileTypes` inside the `select_file()` function.
* **Saving File Types**:
  * Similar to the accepted file types, this configuration defines which file formats can be used when saving the Watermarked Image.
  * It is provided as an argument named `filetypes` in the `__save_image(self)` function.
* **Root Window Size**:
  * To change the size of the main window, adjust the variable `self.__rootSize`.
* **Canvas Size**:
  * When modifying the root window size, you should also update the canvas size.
  * Ensure that the canvas height is 200 pixels less than the root window height.
  * This is controlled by the variable `self.__canvasSize`.
* **Button Font**:
  * You can customize the font type, size, and style used for the button text.
  * This is managed by the variable `self.__font`.

### Watermark Class Configurations
* **Mark Size**:
  * To adjust the size of the Mark, change the variable `self.__squares`.
  * This variable determines the number of squares used to divide the image and calculate the corner positions, maintaining the original Image's scale.
    * **Example**:
      * Setting `self.__squares` to 4 will make the Mark occupy 1/16 of the image.
      * Setting it to 2 will make the Mark occupy 1/4 of the image.
  * So, make sure you understand this concept before making any modifications.
* **Mark Positions**:
  * Once you grasp the concept of Mark size, modifying the positions becomes easier.
  * By default, four positions (one per corner) are defined, but you can add more if needed.
  * Each position is represented as a tuple of four values, corresponding to two points in the image: the upper left corner and the lower right corner. All positions are calculated from the Image's upper left corner (0,0).
  * These positions are stored in a list of tuples named `self.__positions`, which is set up in the `__set_positions(self)` function.

---

## Notes

* The image displayed in the GUI is resized in order to properly fit in the canvas and avoid making it look weird, but it may still look different from the original image in some degree. However, this resizing process **does not affect the final result**, so the image keeps its original dimensions.
* Although the PIL Image Object can handle various formats, this project is limited to **PNG**, **JPEG**, and **JPG** formats for simplicity.
* Many attributes within the `UI` class are configurable. Feel free to adjust them according to your requirements. The code is designed to work without issues after modifications.
* Similarly, the `Watermark` class offers flexibility for changes. However, please ensure you understand the underlying code before making any adjustments.

---

## Useful Resources

* [PIL documentation](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) - Official documentation for the Pillow library, a powerful tool for image processing and manipulation in Python.
* [typing documentation](https://docs.python.org/3/library/typing.html) - Official documentation for Python's typing module, which provides support for type hints.
* [Tkinter documentation](https://docs.python.org/3/library/tk.html) - Official documentation for Tkinter, Python's standard library for building graphical user interfaces (GUIs).

