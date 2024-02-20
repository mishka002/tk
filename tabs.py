#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFile
from tkinter import font as tkfont


def generate():
    selected_value = combo_box.get()
    nm = name.get()
    per = persent.get()
   

    print("ვის: ", nm, " რამდენი: ", per, " ტიპი: ", selected_value)

root = tk.Tk()
root.title('პრომო')
root.iconbitmap('imgs/qr-code.ico')
root.geometry('500x530')
ImageFile.LOAD_TRUNCATED_IMAGES = True

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

font_path = "fonts/bpg-no9-webfont.ttf" 
georgian_font = tkfont.Font(family=font_path, size=12)

myFont = ttk.Style()
myFont.configure("danger.Outline.TButton", font=(font_path, 10))

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

tab1 = ttk.Frame(my_notebook)
tab2 = ttk.Frame(my_notebook)

image_path = "imgs/qr-code.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Tab 1

text = "პრომო კოდის დამოწმება"
text_label = ttk.Label(tab1, text=text, font=georgian_font, padding=10)
text_label.pack(pady=10, anchor="center")

entry = ttk.Entry(tab1, width=20, font=georgian_font)
entry.pack()

b4 = ttk.Button(tab1, text='დამოწმება', style="danger.Outline.TButton", command=generate)
b4.pack(pady=20)

text2 = "-- ან --"
text_label2 = ttk.Label(tab1, text=text2, font=georgian_font, padding=10)
text_label2.pack(pady=10)

image_label = ttk.Label(tab1, image=photo)
image_label.pack(pady=10)

# Tab 1 End

# Tab 2

text = "პრომო"
my_label2 = ttk.Label(tab2, text=text, font=georgian_font, padding=10)
my_label2.pack(pady=10)

lf = ttk.LabelFrame(tab2, text=' ვის? ', padding=10)
lf.pack(pady=10)

name = ttk.Entry(lf, width=30, font=georgian_font)
name.pack()

lf = ttk.LabelFrame(tab2, text=' რამდენ % იანი ', padding=10)
lf.pack()

persent = ttk.Entry(lf, width=30, font=georgian_font)
persent.pack(pady=10)

options = ["ცივი სასმელები", "ცხელი სასმელები", "სასმელები * ", "საჭმელი", "დესერტები"]

lf = ttk.LabelFrame(tab2, text=' ტიპი ', padding=10)
lf.pack(pady=10)

combo_box = ttk.Combobox(lf, values=options, width=20, font=georgian_font)
combo_box.set("აირჩიე")
combo_box.bind("<<ComboboxSelected>>", lambda event: print("Selected:", combo_box.get()))
combo_box.pack(pady=10)

b4 = ttk.Button(tab2, text='გენერირება', style="danger.Outline.TButton", command=generate)
b4.pack(pady=20)

my_notebook.add(tab1, text='პრომოს შემოწმება')
my_notebook.add(tab2, text='პრომოს შექმნა')

root.mainloop()
