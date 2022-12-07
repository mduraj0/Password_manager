import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Password Manager')

    tabs = ttk.Notebook(root)

    cred_tab = tk.Frame(tabs)
    add_cred_tab = tk.Frame(tabs)
    tabs.add(cred_tab, text='Credentials')
    tabs.add(add_cred_tab, text='Add password')

    tabs.pack(expand=1, fill='both')

    tree = ttk.Treeview()

    root.mainloop()