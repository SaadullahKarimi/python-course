# Import Required Libraries
from tkinter import *  # Import the Tkinter library for GUI creation
import datetime  # Import the datetime library to get the current time
import time  # Import time library to control time-based events like delays
import winsound  # Import winsound library for playing sound on Windows
from threading import *  # Import the threading library to run the alarm in a separate thread

# Create Object for the root window
root = Tk()  # Initialize the main window object

# Set the window geometry (width x height)
root.geometry("400x200")  # Set the window size to 400x200 pixels

# Function to handle threading
def Threading():  # Define a function to create and start a new thread for the alarm
    t1 = Thread(target=alarm)  # Create a new thread to run the alarm function
    t1.start()  # Start the thread

def alarm():  # Define the function that runs the alarm
    # Infinite loop to keep checking the time until alarm triggers
    while True:  # Keep running the loop to continuously check the time
        # Set the alarm time from the user's input (formatted as HH:MM:SS)
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        
        # Wait for one second before checking the time again
        time.sleep(1)  # Delay the loop for 1 second to avoid continuous processing

        # Get the current time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)  # Print both the current time and the alarm time for debugging

        # Check if the current time matches the set alarm time
        if current_time == set_alarm_time:  # Compare the current time with the set alarm time
            print("Time to Wake up")  # Print a message when the alarm triggers
            # Play a sound (async so it doesn't block the rest of the program)
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Play the sound.wav file as an alarm sound

# Add a Label for the title of the application
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)  # Display the title "Alarm Clock" in red with large bold font

# Add another Label for the text "Set Time"
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()  # Display the "Set Time" label with a bold font

# Create a frame to hold the time input widgets
frame = Frame(root)  # Create a frame container to hold the hour, minute, and second option menus
frame.pack()  # Add the frame to the window

# Create a StringVar to store the selected hour value
hour = StringVar(root)  # StringVar stores the value of the hour selection
# Define the available hours (00 to 24)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])  # Set the default selected hour to '00'

# Create an OptionMenu for selecting the hour, passing the available hours
hrs = OptionMenu(frame, hour, *hours)  # Create an OptionMenu widget for selecting hours
hrs.pack(side=LEFT)  # Place the OptionMenu on the left side of the frame

# Create a StringVar to store the selected minute value
minute = StringVar(root)  # StringVar stores the value of the minute selection
# Define the available minutes (00 to 60)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])  # Set the default selected minute to '00'

# Create an OptionMenu for selecting the minute, passing the available minutes
mins = OptionMenu(frame, minute, *minutes)  # Create an OptionMenu widget for selecting minutes
mins.pack(side=LEFT)  # Place the OptionMenu on the left side of the frame

# Create a StringVar to store the selected second value
second = StringVar(root)  # StringVar stores the value of the second selection
# Define the available seconds (00 to 60)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])  # Set the default selected second to '00'

# Create an OptionMenu for selecting the second, passing the available seconds
secs = OptionMenu(frame, second, *seconds)  # Create an OptionMenu widget for selecting seconds
secs.pack(side=LEFT)  # Place the OptionMenu on the left side of the frame

# Add a button to set the alarm, calling the Threading function when clicked
Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)  # Display the "Set Alarm" button and bind it to start the threading

# Start the Tkinter event loop to keep the window running and interactive
root.mainloop()  # Start the Tkinter event loop, making the GUI interactive and responsive
