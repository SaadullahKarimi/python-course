import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timer completed!')

def countup(t):
    current_time = 0
    while current_time <= t:
        mins, secs = divmod(current_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        current_time += 1
    print('Timer completed!')

choice = input("Choose timer type (1 for CountDown, 2 for CountUp): ")

if choice == '1':
    t = int(input("Enter the time in seconds for CountDown: "))
    countdown(t)
elif choice == '2':
    t = int(input("Enter the time in seconds to count up to: "))
    countup(t)
else:
    print("Invalid choice!")
