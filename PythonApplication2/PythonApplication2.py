import tkinter as tk

def f_to_c():
    f = float(f_entry.get())
    c = (f - 32) * 5/9
    c_entry.delete(0, tk.END)
    c_entry.insert(0, f"{c:.1f}")

def c_to_f():
    c = float(c_entry.get())
    f = (f - 32) * 5/9
    f_entry.delete(0, tk.END)
    f_entry.insert(0, f"{f:.1f}")

window = tk.TK()
window.title("Temperature Converter")

# Labels (Row 0)
tk.Label(window,
         text="Fahrenheit").grid(row=0, column=0)
tk.Label(window,
         text="Celsius").grid(row=0, column=1)

# Entries (Row 1)
f_entry = tk.Entry(window)
f_entry.grid(row=1, column=0)
f_entry.insert(0, "32.0")

c_entry = tk.Entry(window)
c_entry.grid(row=1, column=1)
c_entry.insert(0, "0.0")

# Buttons (Row 2)
tk.Button(window, text=">>>>",
          command=f_to_c).grid(row=2, column=0)
tk.Button(window, text="<<<<",
          command=c_to_f).grid(row=2, column=1)

window.mainloop()