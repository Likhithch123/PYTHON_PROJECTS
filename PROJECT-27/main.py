import tkinter
FONT = ("Times New Roman", 18, "normal")

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=400, width=400)
window.config(padx=200, pady=200)

# Entry-1
entry_1 = tkinter.Entry(width=15)
entry_1.grid(row=0, column=1)

# Label-1
miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

# Label-2
is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(padx=10, pady=10)

# Label-3
result_label = tkinter.Label(text="0", font=FONT)
result_label.grid(row=1, column=1)
result_label.config(padx=10, pady=10)

# Label-4
km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)


def miles_to_km():
    miles = entry_1.get()
    result_label.config(text=f"{float(miles) * 1.60934}")


# Button
button = tkinter.Button(text="Calculate", font=FONT, command=miles_to_km)
button.grid(row=2, column=1)
window.mainloop()
