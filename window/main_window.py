import tkinter as tk


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("My Window Application")

        # Add a label to the root window.
        self.label = tk.Label(self.root, text="Enter your name:")
        self.label.pack()

        # Add an entry widget to the root window.
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Add a button to the root window.
        self.button = tk.Button(self.root, text="Submit", command=self.submit)
        self.button.pack()

    def submit(self):
        name = self.entry.get()
        print("Hello, {}!".format(name))

    def run(self):
        self.root.mainloop()