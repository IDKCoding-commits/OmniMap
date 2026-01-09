from PIL import Image, ImageTk
import requests
from io import BytesIO

def clear_input(text_box):
    text_box.set_value('')

def handle_submit(textarea):
    def on_submit():
        value = textarea.value
        value_string = str(value)
        stripped_value = str(value_string.strip())
        lower_value = str(stripped_value.lower())
        print(lower_value)
        if lower_value == "silksong":
            print("Due to the sheer size and complexity of Silksong, maps for that game are sorted by Act. To get maps for Silksong, simply search 'Silksong Act X'")
        return value, clear_input(textarea)
    return on_submit




