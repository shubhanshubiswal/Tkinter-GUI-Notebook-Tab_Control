# notebook -- contain two pages 
# page 1                                    # page2
# widgets                                   widgets 

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Notebook")
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
page4 = ttk.Frame(nb)
page5 = ttk.Frame(nb)
nb.add(page1, text='ONE')
nb.add(page2, text='TWO')
nb.add(page3, text='THREE')
nb.add(page4, text='FOUR')
nb.add(page5, text='FIVE')

# nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')

label1 = ttk.Label(page1, text='Page 1 label : ')
label1.grid(row=0, column=0)


label2 = ttk.Label(page2, text='Page 2 label : ')
label2.grid(row=0, column=0)


label3 = ttk.Label(page3, text='Page 3 label : ')
label3.grid(row=0, column=0)

label4 = ttk.Label(page4, text='Page 4 label : ')
label4.grid(row=0, column=0)


label5 = ttk.Label(page5, text='Page 5 label : ')
label5.grid(row=0, column=0)

entry1 = ttk.Entry(page1, width=26)
entry1.grid(row=0, column=1)

entry2 = ttk.Entry(page2, width=26)
entry2.grid(row=0, column=1)

entry3 = ttk.Entry(page3, width=26)
entry3.grid(row=0, column=1)

entry4 = ttk.Entry(page4, width=26)
entry4.grid(row=0, column=1)

entry5 = ttk.Entry(page5, width=26)
entry5.grid(row=0, column=1)

win.mainloop()