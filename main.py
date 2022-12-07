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
        self.config_tree()

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

        for credential in credentials:
            self.tree.insert('', 'end', values=(credential.portal, credential.login))

        self.tree.pack()


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

    CredentialList(cred_tab)

    root.mainloop()
