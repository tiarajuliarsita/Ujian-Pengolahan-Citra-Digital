import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create label to show the original image
        self.original_label = tk.Label(self)
        self.original_label.pack(side="left", padx=10, pady=10)

        # Create label to show the processed image
        self.processed_label = tk.Label(self)
        self.processed_label.pack(side="right", padx=10, pady=10)

        # Create label for nama
        self.tiara_label = tk.Label(self, text="Nama : Tiara Juli Arsita ")
        self.tiara_label.pack()

        # Create label for nim
        self.Nim_label = tk.Label(self, text="Nim : F55121053 ")
        self.Nim_label.pack()

        # Create button to select the image
        self.select_image_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.select_image_button.pack(padx=10, pady=10)

        # Create button to apply grayscale conversion
        self.grayscale_button = tk.Button(self, text="Grayscale", command=self.convert_to_grayscale)
        self.grayscale_button.pack(padx=10, pady=10)

        # Create button to apply image inversion
        self.invert_button = tk.Button(self, text="Invert Colors", command=self.invert_colors)
        self.invert_button.pack(padx=10, pady=10)

        # Create button to close the app
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack(padx=10, pady=10)
        self.image_path = None

    def select_image(self):
        # Show file dialog to select the image
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path

            # Load the image and display it in the original label
            img = Image.open(self.image_path)
            img = ImageOps.exif_transpose(img)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.original_label.config(image=img_tk)
            self.original_label.image = img_tk

    def convert_to_grayscale(self):
        if self.image_path:
            # Load the image and convert it to grayscale
            img = Image.open(self.image_path).convert('L')

            # Display the processed image in the processed label
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)
            self.processed_label.config(image=img_tk)
            self.processed_label.image = img_tk

    def invert_colors(self):
        if self.image_path:
            # Load the image and invert its colors
            img = Image.open(self.image_path)
            inverted_img = ImageOps.invert(img)

            # Display the processed image in the processed label
            inverted_img = inverted_img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(inverted_img)
            self.processed_label.config(image=img_tk)
            self.processed_label.image = img_tk

root = tk.Tk()
app = App(master=root)
app.mainloop()
