import tkinter as tk

def checkbox_action():
    if checkbox_var.get() == 1:
        label.config(text="Checkbox is checked")
    else:
        label.config(text="Checkbox is unchecked")

window = tk.Tk()
window.title("Checkbox Example")

# Create a Checkbutton widget
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(window, text=" ", variable=checkbox_var, command=checkbox_action)
checkbox.pack()

# Create a Label to display the status of the checkbox
label = tk.Label(window, text="Checkbox is unchecked")
label.pack()

window.mainloop()
