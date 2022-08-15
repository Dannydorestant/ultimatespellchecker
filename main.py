from tkinter import *
from spellchecker import SpellChecker

spell = SpellChecker()

window = Tk()
window.title("Ultimate Spell Checker")


class Gui(Tk):
    def __init__(self):
        # Labels
        self.text_label = Label(window, text="Insert Text:", font=('comic sans', 15))
        self.text_label.grid(row=0, column=0, padx=10, pady=10)

        self.result_label = Label(window, text="Suggested Spelling:", font=('comic sans', 15))
        self.result_label.grid(row=5, column=0, pady=10, columnspan=3)

        # User Input
        self.word_entry = Entry(window, width=50)
        self.word_entry.grid(row=2, column=0, pady=2, padx=5)

        # Buttons
        self.convert = Button(window, text='Check Spelling', width=25, command=self.check_spelling)
        self.convert.grid(row=3, column=0, pady=5)

        self.convert = Button(window, text='Clear Suggestions', width=25, command=self.clear_list)
        self.convert.grid(row=4, column=0, pady=5)

        # Listbox

        self.listbox1 = Listbox(window)
        self.listbox1.grid(row=6, column=0, pady=10)

    def clear_list(self):
        self.listbox1.delete(0, END)

    def check_spelling(self):
        sentence = self.word_entry.get().lower()
        words_list = sentence.split()

        for word in words_list:
            misspelled = spell.correction(word)
            self.listbox1.insert(END, misspelled)


gui = Gui()
window.mainloop()
