import tkinter as tk  # Import the tkinter module and alias it as 'tk' for easier reference.
from tkinter import filedialog  # Import the 'filedialog' module from tkinter for file operations.

class Notepad(tk.Tk):  # Define a new Notepad class that inherits from the Tk class to create the main window.
    def __init__(self, *args, **kwargs):  # Initialize the Notepad class, which is a subclass of Tk.
        tk.Tk.__init__(self, *args, **kwargs)  # Call the constructor of the parent Tk class to initialize the main window.

        # Set the title for the notepad window.
        self.title("Notepad")  # Set the window title to "Notepad".

        # Create a text widget for multi-line text input.
        self.text = tk.Text(self, wrap="word")  # Create a Text widget with word wrapping enabled.
        self.text.pack(side="top", fill="both", expand=True)  # Add the text widget to the window and make it expandable.

        # Create a menu bar for the notepad application.
        self.menu = tk.Menu(self)  # Create a Menu widget for the main window.
        self.config(menu=self.menu)  # Set the menu bar to the current window.

        # Create a "File" menu with options like New, Open, Save, and Exit.
        file_menu = tk.Menu(self.menu)  # Create a submenu for "File".
        self.menu.add_cascade(label="File", menu=file_menu)  # Add the File menu to the menu bar.
        file_menu.add_command(label="New", command=self.new_file)  # Add a "New" option that calls the 'new_file' method.
        file_menu.add_command(label="Open", command=self.open_file)  # Add an "Open" option that calls the 'open_file' method.
        file_menu.add_command(label="Save", command=self.save_file)  # Add a "Save" option that calls the 'save_file' method.
        file_menu.add_separator()  # Add a separator line to visually separate options.
        file_menu.add_command(label="Exit", command=self.quit)  # Add an "Exit" option that calls the 'quit' method to close the app.

        # Create an "Edit" menu with options like Cut, Copy, and Paste.
        edit_menu = tk.Menu(self.menu)  # Create a submenu for "Edit".
        self.menu.add_cascade(label="Edit", menu=edit_menu)  # Add the Edit menu to the menu bar.
        edit_menu.add_command(label="Cut", command=self.cut)  # Add a "Cut" option that calls the 'cut' method.
        edit_menu.add_command(label="Copy", command=self.copy)  # Add a "Copy" option that calls the 'copy' method.
        edit_menu.add_command(label="Paste", command=self.paste)  # Add a "Paste" option that calls the 'paste' method.

    def new_file(self):  # Define the method to create a new file.
        self.text.delete("1.0", "end")  # Delete any text currently in the text widget.
        self.title("Notepad")  # Reset the window title to "Notepad" after creating a new file.

    def open_file(self):  # Define the method to open an existing file.
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")  # Open a file dialog to select a file.
        if file:  # If a file is selected:
            contents = file.read()  # Read the contents of the file.
            self.text.delete("1.0", "end")  # Delete any existing text in the text widget.
            self.text.insert("1.0", contents)  # Insert the file contents into the text widget at the start.
            file.close()  # Close the file after reading.
            self.title(file.name + " - Notepad")  # Set the window title to the name of the opened file.

    def save_file(self):  # Define the method to save the current file.
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])  # Open a file save dialog.
        if file:  # If a file is selected:
            contents = self.text.get("1.0", "end")  # Get all the text in the text widget.
            file.write(contents)  # Write the contents to the selected file.
            file.close()  # Close the file after saving.
            self.title(file.name + " - Notepad")  # Set the window title to the name of the saved file.

    def cut(self):  # Define the method to cut selected text.
        self.text.event_generate("<<Cut>>")  # Generate the "cut" event to remove selected text and place it on the clipboard.

    def copy(self):  # Define the method to copy selected text.
        self.text.event_generate("<<Copy>>")  # Generate the "copy" event to place the selected text on the clipboard.

    def paste(self):  # Define the method to paste text from the clipboard.
        self.text.event_generate("<<Paste>>")  # Generate the "paste" event to insert text from the clipboard at the cursor position.

if __name__ == "__main__":  # Ensure this code runs only if it's the main module being executed.
    notepad = Notepad()  # Create an instance of the Notepad class.
    notepad.mainloop()  # Start the Tkinter event loop to run the application.
