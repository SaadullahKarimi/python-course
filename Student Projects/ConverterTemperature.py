# Importing the Tkinter library for creating a graphical user interface
import tkinter as tk

# Function to convert temperature
def convert_temperature():
    try:
        # Getting the temperature value from the user input and converting it to a numerical type
        temperature = float(entry.get())
        # Checking if the selected unit is Celsius
        if var.get() == "C":
            # Converting the temperature from Celsius to Fahrenheit
            converted = (temperature * 9/5) + 32
            # Displaying the conversion result in the result label
            result_label.config(text=f"Result: {converted:.2f} °F")
        else:
            # Otherwise, converting the temperature from Fahrenheit to Celsius
            converted = (temperature - 32) * 5/9
            # Displaying the conversion result in the result label
            result_label.config(text=f"Result: {converted:.2f} °C")
    except ValueError:
        # If the input is invalid, an error message is shown
        result_label.config(text="Please enter a valid number.")

# Creating the main window
root = tk.Tk()
# Setting the window title
root.title("Temperature Converter")
# Setting the window size
root.geometry("300x250")  # Width: 300px, Height: 250px
# Setting the background color of the window to light gray
root.config(bg="#f0f0f0")  # Background color of the window

# Creating a title label for the program with a specific background color and text color
title_label = tk.Label(root, text="Temperature Converter", font=("Helvetica", 16), bg="#f0f0f0", fg="#333333")
# Displaying the title label in the window
title_label.pack(pady=10)

# Creating a label for the temperature input
entry_label = tk.Label(root, text="Input Temperature:", bg="#f0f0f0", fg="#333333")
# Displaying the input temperature label in the window
entry_label.pack(pady=5)

# Creating a text entry widget for the temperature input
entry = tk.Entry(root)
# Displaying the temperature entry in the window
entry.pack(pady=5)

# Variable to store the selected temperature unit (Celsius or Fahrenheit)
var = tk.StringVar(value="C")  # Default value: Celsius

# Creating a radio button for selecting Celsius with specific colors
celsius_button = tk.Radiobutton(root, text="Celsius (C)", variable=var, value="C", bg="#f0f0f0", fg="#333333")
# Displaying the Celsius radio button in the window
celsius_button.pack()

# Creating a radio button for selecting Fahrenheit with specific colors
fahrenheit_button = tk.Radiobutton(root, text="Fahrenheit (F)", variable=var, value="F", bg="#f0f0f0", fg="#333333")
# Displaying the Fahrenheit radio button in the window
fahrenheit_button.pack()

# Creating a button to perform the temperature conversion with specific colors
convert_button = tk.Button(root, text="Convert", command=convert_temperature, bg="#4CAF50", fg="white")
# Displaying the convert button in the window
convert_button.pack(pady=10)

# Creating a label to display the conversion result with specific colors
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", fg="#333333")
# Displaying the result label in the window
result_label.pack(pady=10)

# Running the window and starting the program
root.mainloop()
