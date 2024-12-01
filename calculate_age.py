# Import necessary libraries  
import tkinter as tk  # For creating the GUI  
from tkinter import messagebox  # For displaying message boxes  
from datetime import datetime  # For handling date and time  
import matplotlib.pyplot as plt  # For plotting charts  

# Function to calculate the age based on user input  
def calculate_age():  
    try:  
        # Get birth date input from the user  
        byy = int(birth_year_entry.get())  # Birth year  
        bmm = int(birth_month_entry.get())  # Birth month  
        bdd = int(birth_day_entry.get())  # Birth day  
        
        # Get current date input from the user  
        cyy = int(current_year_entry.get())  # Current year  
        cmm = int(current_month_entry.get())  # Current month  
        cdd = int(current_day_entry.get())  # Current day  
        
        # Calculate the birth date and current date  
        birth_date = datetime(byy, bmm, bdd)  
        current_date = datetime(cyy, cmm, cdd)  
        
        # Calculate the difference between the two dates in days  
        age_days = (current_date - birth_date).days  
        
        # Calculate years, months, and days from the total days  
        years = age_days // 365  # Total years  
        months = (age_days % 365) // 30  # Total months  
        days = (age_days % 365) % 30  # Remaining days  

        # Show the calculated age in a message box  
        messagebox.showinfo("Your Age", f"Your age is: {years} years, {months} months, and {days} days.")  
        
        # Draw the age distribution chart  
        draw_chart(years, months, days)  
    
    except ValueError:  
        # Handle the case where the input is not a valid integer  
        messagebox.showerror("Input Error", "Please enter valid integers for all fields.")  
    except Exception as e:  
        # Handle any other exceptions that may occur  
        messagebox.showerror("Error", str(e))  

# Function to draw a pie chart showing age distribution  
def draw_chart(years, months, days):  
    # Define labels and sizes for the pie chart  
    labels = ['Years', 'Months', 'Days']  
    sizes = [years, months, days]  
    colors = ['gold', 'lightcoral', 'lightskyblue']  # Colors for each slice  
    explode = (0.1, 0, 0)  # Slightly explode the first slice (Years)  

    # Create a pie chart  
    plt.figure(figsize=(6, 6))  # Set the figure size  
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,  
            autopct='%1.1f%%', shadow=True, startangle=140)  # Create the pie chart  

    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle  
    plt.title('Age Distribution')  # Title of the chart  
    plt.show()  # Display the chart  

    # Display the age below the chart  
    plt.text(0, -1.2, f'Your age is: {years} years, {months} months, and {days} days',   
             horizontalalignment='center', fontsize=12, color='black')  # Text settings  

# Create the main GUI window  
window = tk.Tk()  
window.title("Age Calculator")  # Title of the window  

# Input fields for birth date  
tk.Label(window, text="Enter your birth year:").grid(row=0, column=0)  
birth_year_entry = tk.Entry(window)  # Entry for birth year  
birth_year_entry.grid(row=0, column=1)  

tk.Label(window, text="Enter your birth month:").grid(row=1, column=0)  
birth_month_entry = tk.Entry(window)  # Entry for birth month  
birth_month_entry.grid(row=1, column=1)  

tk.Label(window, text="Enter your birth day:").grid(row=2, column=0)  
birth_day_entry = tk.Entry(window)  # Entry for birth day  
birth_day_entry.grid(row=2, column=1)  

# Input fields for current date  
tk.Label(window, text="Enter current year:").grid(row=3, column=0)  
current_year_entry = tk.Entry(window)  # Entry for current year  
current_year_entry.grid(row=3, column=1)  

tk.Label(window, text="Enter current month:").grid(row=4, column=0)  
current_month_entry = tk.Entry(window)  # Entry for current month  
current_month_entry.grid(row=4, column=1)  

tk.Label(window, text="Enter current day:").grid(row=5, column=0)  
current_day_entry = tk.Entry(window)  # Entry for current day  
current_day_entry.grid(row=5, column=1)  

# Button to trigger age calculation  
calculate_button = tk.Button(window, text="Calculate Age", command=calculate_age)  
calculate_button.grid(row=6, column=0, columnspan=2)  # Position the button in the grid  

# Start the main event loop of the GUI  
window.mainloop()