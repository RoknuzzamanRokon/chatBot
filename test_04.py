import tkinter as tk
import openai

API_KEY = open("secret_key.txt", "r").read()
openai.api_key = API_KEY

BACKGROUND_COLOR = "#B1DDC6"


window = tk.Tk()
window.title("Roko chatBot")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Create a Frame for the Canvas
frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)

# Create a Canvas widget inside the Frame.
canvas = tk.Canvas(frame, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

# Create a Text widget with a scrollbar.
user_input_text = tk.Text(canvas, wrap=tk.WORD, width=80, height=25, state=tk.DISABLED)
user_input_text.grid(row=0, column=0, rowspan=2)

scrollbar = tk.Scrollbar(frame, command=user_input_text.yview)
scrollbar.grid(row=0, column=1, rowspan=2, sticky='ns')
user_input_text.config(yscrollcommand=scrollbar.set)


# Add label for story word.
words_label = tk.Label(window, text="How many words do you want in the story?", font=("Arial", 20, "bold"))
words_label.grid(row=1,column=3)

# Entry user word input.
words_input_entry = tk.Entry(window, font=("Arial", 14), width=50)
words_input_entry.grid(row=2,column=3)
window.mainloop()
