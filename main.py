import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass


@dataclass
class DTOCredentials:
    portal: str
    login: str


if __name__ == '__main__':
    credentials = [
        DTOCredentials('o2.pl', 'duraj9@wp.pl'),
        DTOCredentials('facebook.pl', 'duraj4@o2.pl'),
        DTOCredentials('gmail.com', 'durajczykmichal@gmail.com')
    ]

    root = tk.Tk()
    root.title('Password Manager')

    tabs = ttk.Notebook(root)

    cred_tab = tk.Frame(tabs)
    add_cred_tab = tk.Frame(tabs)
    tabs.add(cred_tab, text='Credentials')
    tabs.add(add_cred_tab, text='Add password')

    tabs.pack(expand=1, fill='both')

    tree = ttk.Treeview(
        cred_tab,
        columns=('portal', 'login'),
        show='headings',
        height=10
    )
    tree.column(
        '#1',
        anchor=tk.CENTER,
        stretch=tk.NO,
        width=200
    )
    tree.heading('#1', text='portal')
    tree.column(
        '#2',
        anchor=tk.CENTER,
        stretch=tk.NO,
        width=200
    )
    tree.heading('login', text='login')

    for credential in credentials:
        tree.insert('', 'end', values=(credential.portal, credential.login))

    tree.pack()

    root.mainloop()
