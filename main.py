import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        # Create a text area
        self.text_area = tk.Text(self.root, bg="Black", fg="white")
        self.text_area.config(insertbackground="white")  
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Create a status bar
        self.status_bar = tk.Label(self.root, text="", bg = "Black", fg="White")
        self.status_bar.pack(anchor=tk.SE, fill=tk.X)

        # Create a menu
        self.menu = tk.Menu(self.root, bg="Black", fg="White")
        self.root.config(menu=self.menu)

        # Create a file menu
        self.file_menu = tk.Menu(self.menu, tearoff=False,bg="Black", fg="White")
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_program)

        # Create an edit menu
        self.edit_menu = tk.Menu(self.menu, tearoff=False, bg="Black", fg="White")
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Count Words", command=self.count_words)
        self.edit_menu.add_command(label="Count Lines", command=self.count_lines)

        # Bind the key release event to update word and line count
        self.text_area.bind("<KeyRelease>", self.update_counts)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.update_status("New file created.")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.update_status("File opened: " + file_path)

    def save_file(self):
        # If the file has not been saved before, prompt for a file name
        if not hasattr(self, "file_path"):
            self.save_file_as()
            return

        content = self.text_area.get(1.0, tk.END)
        with open(self.file_path, "w") as file:
            file.write(content)
        self.update_status("File saved.")

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path = file_path
            self.save_file()

    def exit_program(self):
        self.root.destroy()

    def count_words(self):
        content = self.text_area.get(1.0, tk.END)
        word_count = len(content.split())
        self.update_status("Word count: " + str(word_count))

    def count_lines(self):
        content = self.text_area.get(1.0, tk.END)
        # line_count = 0
        line_count = len(content.split('\n')) - 1
        self.update_status("Line count: " + str(line_count))

    def update_counts(self, event):
        content = self.text_area.get(1.0, tk.END)
        word_count = len(content.split())
        line_count = len(content.split('\n'))
        self.update_status("Word count: " + str(word_count) + "   |   Line count: " + str(line_count))
        
    def update_status(self, message):
        self.status_bar.config(text=message)
    
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()


