import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(value)
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(value)
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(value)
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = fahrenheit_to_kelvin(value)
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(value)
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(value)
        else:
            result = value

        result_label.config(text=str(round(result, 2)))

    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

from_var = tk.StringVar(root)
from_var.set("Celsius")

to_var = tk.StringVar(root)
to_var.set("Fahrenheit")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=10)
entry.grid(row=0, column=0)

from_dropdown = tk.OptionMenu(frame, from_var, "Celsius", "Fahrenheit", "Kelvin")
from_dropdown.grid(row=0, column=1)

to_dropdown = tk.OptionMenu(frame, to_var, "Celsius", "Fahrenheit", "Kelvin")
to_dropdown.grid(row=0, column=2)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(row=0, column=3)

result_label = tk.Label(frame, text="")
result_label.grid(row=1, columnspan=4)

root.mainloop()
