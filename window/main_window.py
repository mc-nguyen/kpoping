import tkinter as tk

from data.scraping_from_kpop import ScrapingFromKPop


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("My Window Application")

        # Create listbox and scrollbar
        self.listbox = tk.Listbox(self.root)
        scrollbar = tk.Scrollbar(self.listbox, command=self.listbox.yview)

        self.classKpop = ScrapingFromKPop()
        profile_categories = list(self.classKpop.get_all_profile_category())
        for i in range(len(profile_categories)):
            self.listbox.insert(tk.END, profile_categories[i])

        # Connect listbox and scrollbar
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind("<ButtonRelease-1>", self.listbox_clicked)

        # Pack widgets
        self.listbox.pack(fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Button
        self.button = tk.Button(self.root,
                                text="Please choose a group",
                                font=("Arial", 16))
        self.button.pack(fill="x")

    def run(self):
        self.root.mainloop()
        print(self.listbox.get(self.listbox.curselection()[0]))

    def listbox_clicked(self, event):
        index = self.listbox.curselection()[0]
        chosen_value = self.listbox.get(index)
        self.button.config(text=chosen_value)
        print(self.classKpop.get_link(chosen_value))