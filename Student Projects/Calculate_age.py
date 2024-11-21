# Importing necessary libraries
import tkinter as tk  # tkinter is used for creating the GUI
from tkinter import messagebox  # messagebox is used to show error or information dialogs
from datetime import datetime  # datetime is used to handle date and time operations

# Function to calculate the age based on the provided birthdate
def calculate_age():
    try:
        # Convert the input birthdate string into a datetime object (format: YYYY-MM-DD)
        birth_date = datetime.strptime(entry_birthdate.get(), "%Y-%m-%d")
        
        # Get today's date using the datetime library
        today = datetime.today()
        
        # Calculate the age by subtracting the birth year from the current year.
        # The additional condition adjusts for whether the birthday has occurred this year or not.
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display the calculated age in the label
        label_result.config(text=f"Age: {age} years old")
    except ValueError:
        # If the user enters an invalid date format, show an error message
        messagebox.showerror("Invalid Date Format", "Please enter the date in YYYY-MM-DD format")

# Create the main window for the GUI
window = tk.Tk()
window.title("Age Calculator")  # Set the window title

# Create a label widget to prompt the user to enter their birthdate
label_birthdate = tk.Label(window, text="Enter your birthdate (YYYY-MM-DD):")
label_birthdate.pack(pady=10)  # Pack the label with some padding for spacing

# Create an entry widget to allow the user to input their birthdate
entry_birthdate = tk.Entry(window)
entry_birthdate.pack(pady=10)  # Pack the entry field with some padding for spacing

# Create a button widget that calls the calculate_age function when clicked
button_calculate = tk.Button(window, text="Calculate Age", command=calculate_age)
button_calculate.pack(pady=10)  # Pack the button with some padding for spacing

# Create a label widget to display the result (calculated age)
label_result = tk.Label(window, text="Age: ")
label_result.pack(pady=20)  # Pack the result label with some padding for spacing

# Run the Tkinter event loop, which waits for user interactions and keeps the window open
window.mainloop()
