#Packages
from tkinter import *
import googletrans
import textblob
from tkinter import messagebox
from tkinter import ttk



#Main Window
root = Tk()
root.title("Translator")
root.geometry("880x300")

#Functions
def translate():
    translated_text.configure(state="normal")
    translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key
        
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to= to_language_key)

        translated_text.insert(1.0, words)
        translated_text.configure(state="disabled")

    except Exception as e:
        messagebox.showerror("Translator", e)


def clear():
    translated_text.configure(state="normal")
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)
    translated_text.configure(state="disabled")

languages = googletrans.LANGUAGES

language_list = list(languages.values())
print(language_list)


# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, padx=10, pady=20)


#Translate Button
translate_button = Button(root, text="Translate", font=("Helvetica", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, padx=10, pady=20)


#Combo boxes
original_combo = ttk.Combobox(root, state="readonly", width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, state="readonly", width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)


#Clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)


root.mainloop()