import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass


@dataclass
class DTOCredentials:
    portal: str
    login: str


class CredentialList:
    def __init__(self, tab):
        self.tree = ttk.Treeview(
            tab,
            columns=('portal', 'login'),
            show='headings',
            height=10
        )
        self.fill_table_with_data()
        self.config_tree()
        self.tree.bind('<<TreeviewSelect>>', self.on_click)

    def on_click(self, event):
        item = self.tree.selection()[0]
        selection = self.tree.item(item, 'values')
        print(selection)

    def fill_table_with_data(self):
        credentials = [
            DTOCredentials('o2.pl', 'duraj9@wp.pl'),
            DTOCredentials('facebook.pl', 'duraj4@o2.pl'),
            DTOCredentials('gmail.com', 'durajczykmichal@gmail.com')
        ]
        for credential in credentials:
            self.tree.insert('', 'end', values=(credential.portal, credential.login))

    def config_tree(self):
        self.tree.column(
            '#1',
            anchor=tk.CENTER,
            stretch=tk.NO,
            width=200
        )
        self.tree.heading('#1', text='portal')
        self.tree.column(
            '#2',
            anchor=tk.CENTER,
            stretch=tk.NO,
            width=200
        )
        self.tree.heading('login', text='login')
        self.tree.pack()


if __name__ == '__main__':\

    root = tk.Tk()
    root.title('Password Manager')

    tabs = ttk.Notebook(root)
    cred_tab = tk.Frame(tabs)

    add_cred_tab = tk.Frame(tabs)
    tabs.add(cred_tab, text='Credentials')
    tabs.add(add_cred_tab, text='Add password')

    tabs.pack(expand=1, fill='both')

    CredentialList(cred_tab)

    root.mainloop()
