import tkinter
from tkinter import ttk
from deep_translator import GoogleTranslator
import pyperclip

class Temperature(object):
    def __init__(self):
        self.entry_for_temperature = None
        self.label_for_temperature = None


def main():
    # Data object to hold information needed for callbacks.
    temperature = Temperature()

    # Root window and Frame on it.
    root = tkinter.Tk()
    root.title("TRADUCTOR por Isaac T.")
    root.geometry("650x200")

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    # The Entry box, into which the user can enter a temperature.
    # We store it in the Temperature object so that we can later
    # get its contents.
    entry = ttk.Entry(frame, width=100)
    entry.grid()
    temperature.entry_for_temperature = entry

    # A Label which will display the temperature corresponding to the
    # temperature that the user enters in the Entry box.
    # We store the label in the Temperature object so that we can later
    # put the computed temperature on it.
    label = ttk.Label(frame, text='Ingresa el texto a traducir')
    label.grid()
    temperature.label_for_temperature = label

    # # Buttons that: get Entry value, compute and display temperature
    # button1 = ttk.Button(frame, text='Compute Fahrenheit from Celsius')
    # button1.grid()
    # button1['command'] = lambda: fahrenheit_from_celsius(temperature)

    button2 = ttk.Button(frame, text='Traducir')
    button2.grid()
    button2['command'] = lambda: celsius_from_fahrenheit(temperature)
    
    button3 = ttk.Button(frame, text='Copiar al portapapeles')
    button3.grid()
    #a=celsius_from_fahrenheit
    button3['command'] = lambda:  clipboard
    
    root.mainloop()
    




def celsius_from_fahrenheit(temperature):
    # Get the contents (as a STRING) from the Entry box.
    entry = temperature.entry_for_temperature
    contents_of_entry_box = entry.get()

    # Convert that STRING to a floating point NUMBER.
    # Use the number to compute the corresponding Celsius temperature.
    # fahrenheit = float(contents_of_entry_box)
    # celsius = (5 / 9) * (fahrenheit - 32)

    # Display the computed Celsius temperature in the Label
    # provided for it.
    # format_string = '{:0.2f} Fahrenheit is {:0.2f} Celsius'
    # answer = format_string.format(fahrenheit, celsius)
    translated = GoogleTranslator(source='es', target='english').translate(contents_of_entry_box)
    temperature.label_for_temperature['text'] = translated
    return clipboard(translated)

def clipboard(text_return):
    pyperclip.copy(text_return)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()