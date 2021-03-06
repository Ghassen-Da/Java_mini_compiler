import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from turtle import bgcolor
from tkcode import CodeEditor
from tkinter import ttk
import os


fileAllPath = ""


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Java Files", "*.java"), ("Java Files", "*.*")]
    )
    if not filepath:
        return
    # txt_edit.delete(1.0, tk.END)
    # txt_edit.forget(tab_1)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        code_editor.content = text
        txt_edit.add(tab_1, text=filepath)
    global fileAllPath
    fileAllPath = filepath
    window.title(f"Mini java compiler - {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="java",
        filetypes=[(".java", "*.java"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = code_editor.content
        output_file.write(text)
    txt_edit.add(tab_1, text=filepath)
    global fileAllPath
    fileAllPath = filepath
    window.title(f"Mini java compiler - {filepath}")


def compileFile():
    # if there is no path, save a new file (save as)
    if(fileAllPath == ""):
        save_file()
    # if we're editing an existing file, save changes before compiling
    f = open(fileAllPath, "w")
    f.write(code_editor.content)
    f.close()
    
    file_to_compile = open(fileAllPath,"r")
    os.system("a.exe < "+file_to_compile.name +" 2> output.txt")
    output = open("output.txt","r")
    terminal.delete(1.0, tk.END)
    with open("output.txt", "r") as input_file:
        text = input_file.read()
        terminal.insert(tk.END, text)


window = tk.Tk()

window.geometry("800x600+250+50")

window.title("Compiler")
window.rowconfigure(0, minsize=450, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open File", command=open_file, bg="grey", fg="white")
btn_save = tk.Button(fr_buttons, text="Save", command=save_file, bg="grey", fg="white")
btn_compile = tk.Button(fr_buttons, text="Compile", command=compileFile, bg="grey", fg="white")

btn_open.grid(row=0, column=0, sticky="ew", ipadx=40, padx=5, pady=(21,5))
btn_save.grid(row=1, column=0, sticky="ew", padx=5,pady=5)
btn_compile.grid(row=2, column=0, sticky="ew", padx=5,pady=(300,5))

fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")
terminal = tk.Text(window)
# terminal.config(state='disabled')
# we add it to the grid
terminal.grid(row=1, column=1, sticky="nsew")
# ********



txt_edit = ttk.Notebook(window)
tab_1 = ttk.Frame(txt_edit)
txt_edit.add(tab_1, text='')
txt_edit.grid(row="0", column=1, sticky="nsew")
code_editor = CodeEditor(
    tab_1,
    width=600,
    height=20,
    language="java",
    font="Consolas",
    autofocus=True,
    blockcursor=True,
    insertofftime=0,
    padx=10,
    pady=10,  
)
code_editor.pack(fill="both", expand=True)

window.update()
window.mainloop()
