import tkinter as tk
from tkinter import ttk
import json
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

DICTIONARY_FILE = os.path.join(os.path.abspath("."), "dictionary.json")
ARCHIVE_FILE = os.path.join(os.path.abspath("."), "archive.json")


def save_dictionary():
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_dictionary():
    try:
        with open(DICTIONARY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_archive():
    with open(ARCHIVE_FILE, 'w', encoding='utf-8') as file:
        json.dump(archive, file, ensure_ascii=False, indent=4)

def load_archive():
    try:
        with open(ARCHIVE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def add_word():
    eng = add_new_word.get().strip().capitalize()
    rus = add_translation.get().strip().capitalize()
    if eng and rus:
        data[eng] = rus
        save_dictionary()
        update_listbox()
        add_new_word.delete(0, tk.END)
        add_translation.delete(0, tk.END)

def delete_word():
    selected_word = listbox.curselection()
    if selected_word:
        eng = listbox.get(selected_word).split(" - ")[0]
        del data[eng]
        save_dictionary()
        update_listbox()

def archive_word():
    selected_word = listbox.curselection()
    if selected_word:
        eng = listbox.get(selected_word).split(" - ")[0]
        archive[eng] = data.pop(eng)
        save_dictionary()
        save_archive()
        update_listbox()
        update_archive_listbox()

def restore_word():
    selected_word = archive_listbox.curselection()
    if selected_word:
        eng = archive_listbox.get(selected_word).split(" - ")[0]
        data[eng] = archive.pop(eng)
        save_dictionary()
        save_archive()
        update_listbox()
        update_archive_listbox()

def del_arch_word():
    selected_word = archive_listbox.curselection()
    if selected_word:
        eng = archive_listbox.get(selected_word).split(" - ")[0]
        del archive[eng]
        save_archive()
        update_archive_listbox()


def update_listbox(search_query=""):
    listbox.delete(0, tk.END)
    for eng, rus in dict(sorted(data.items())).items():
        if search_query.lower() in eng.lower() or search_query.lower() in rus.lower():
            listbox.insert(tk.END, f"{eng} - {rus}")

def update_archive_listbox(search_query=""):
    archive_listbox.delete(0, tk.END)
    for eng, rus in dict(sorted(archive.items())).items():
        if search_query.lower() in eng.lower() or search_query.lower() in rus.lower():
            archive_listbox.insert(tk.END, f"{eng} - {rus}")

def on_search(event):
    search_query = search_var.get()
    update_listbox(search_query)

def on_archive_search(event):
    search_query = archive_search_var.get()
    update_archive_listbox(search_query)

window = tk.Tk()
window.title("My dictionary")
window.geometry('800x600')

data = load_dictionary()
archive = load_archive()

notebook = ttk.Notebook(window)
notebook.pack(fill=tk.BOTH, expand=True)

# Main dictionary tab
frame_main = ttk.Frame(notebook)
frame_main.pack(fill=tk.BOTH, expand=True)
notebook.add(frame_main, text="Dictionary")

#search
frame_search = tk.Frame(frame_main, padx=5, pady=5)
frame_search.pack(fill=tk.X, anchor=tk.NW)

search_label = tk.Label(frame_search, text="Search:")
search_label.pack(side=tk.LEFT, padx=5)

search_var = tk.StringVar()
search_entry = tk.Entry(frame_search, textvariable=search_var)
search_entry.pack(fill=tk.X, padx=5)
search_entry.bind("<KeyRelease>", on_search)

frame_center = ttk.Frame(frame_main)
frame_center.pack(fill=tk.Y, expand=True)

#main list
frame_list = ttk.Frame(frame_center)
frame_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, width=50)
listbox.pack(expand=True, fill=tk.Y)
scrollbar.config(command=listbox.yview)

update_listbox()

#translater
frame_translater = ttk.Frame(frame_center)
frame_translater.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

translater_label = tk.Label(frame_translater, text = "Translater:")
translater_label.pack()

ask_translation = tk.Entry(frame_translater)
ask_translation.pack()

button_translater = tk.Button(frame_translater, text="traslate")
button_translater.pack()

translate_res = tk.Text(frame_translater, height=10, width=50)
translate_res.pack()

#the lower part of the application.
frame_entry = tk.Frame(frame_main, padx=5, pady=5)
frame_entry.pack(anchor=tk.SW, fill=tk.X)

new_word_en_label = tk.Label(frame_entry, text="New english word:")
new_word_en_label.grid(row=0, column=0, padx=5, pady=5)
add_new_word = tk.Entry(frame_entry)
add_new_word.grid(row=1, column=0, padx=5, pady=5)

translation_word_label = tk.Label(frame_entry, text="Translation:")
translation_word_label.grid(row=0, column=1, padx=5, pady=5)
add_translation = tk.Entry(frame_entry)
add_translation.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame_entry, text="Add word", command=add_word)
add_button.grid(row=1, column=4, padx=5, pady=5)

delete_button = tk.Button(frame_entry, text="Delete selected word", command=delete_word)
delete_button.grid(row=2, column=4, padx=5, pady=5)

archive_button = tk.Button(frame_entry, text="Archive selected word", command=archive_word)
archive_button.grid(row=2, column=5, padx=5, pady=5)

# Archive tab
frame_archive = tk.Frame(notebook, padx=5, pady=5)
notebook.add(frame_archive, text="Archive")

frame_archive_search = tk.Frame(frame_archive, padx=5, pady=5)
frame_archive_search.pack(fill=tk.X)

archive_search_label = tk.Label(frame_archive_search, text="Search:")
archive_search_label.pack(side=tk.LEFT, padx=5)

archive_search_var = tk.StringVar()
archive_search_entry = tk.Entry(frame_archive_search, textvariable=archive_search_var)
archive_search_entry.pack(fill=tk.X, padx=5)
archive_search_entry.bind("<KeyRelease>", on_archive_search)

frame_archive_list = tk.Frame(frame_archive)
frame_archive_list.pack(fill=tk.BOTH, expand=True)

archive_scrollbar = tk.Scrollbar(frame_archive_list)
archive_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

archive_listbox = tk.Listbox(frame_archive_list, yscrollcommand=archive_scrollbar.set)
archive_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
archive_scrollbar.config(command=archive_listbox.yview)

update_archive_listbox()

restore_button = tk.Button(frame_archive, text="Restore selected word", command=restore_word)
restore_button.pack(pady=10)

del_arch_word_button = tk.Button(frame_archive, text="Delete selected word", command=del_arch_word)
del_arch_word_button.pack(pady=10)

window.mainloop()
