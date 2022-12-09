import sys
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from install import install
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Credentials, Portal
from crypto import Crypto
from cryptography.fernet import InvalidToken


@dataclass
class DTOCredentials:
    portal: str
    login: str


class AddPassword:
    def __init__(self, tab, db, credential_list, tabs, password):
        self.db = db
        self.credential_list = credential_list
        self.tabs = tabs
        self.crypto = Crypto(password)

        button = ttk.Button(tab, text='Add password')
        portal_label = ttk.Label(tab, text='Portal:')
        self.portal = ttk.Entry(tab)

        login_label = ttk.Label(tab, text='Login:')
        self.login = ttk.Entry(tab)

        password_label = ttk.Label(tab, text='Password:')
        self.password = ttk.Entry(tab, show='*')

        portal_label.grid(row=0, column=0, padx=5)
        self.portal.grid(row=0, column=1, pady=5)

        login_label.grid(row=1, column=0, padx=5)
        self.login.grid(row=1, column=1, pady=5)

        password_label.grid(row=2, column=0, padx=5)
        self.password.grid(row=2, column=1, pady=5)

        button.grid(row=3, column=0, columnspan=2)
        button.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        print('Click!!!')
        with Session(self.db) as session:
            portal = Portal(name=self.portal.get())
            cred = Credentials(
                login=self.login.get(),
                password=self.crypto.encrypt(self.password.get()),
                portal=portal
            )
            session.add_all([
                portal,
                cred
            ])

            session.commit()
            self.credential_list.fill_table_with_data()
            self.tabs.select(0)


class CredentialList:
    def __init__(self, tab, root_window, db, password, tabs, main_pass_tab):
        self.root_window = root_window
        self.tabs = tabs
        self.main_pass_tab = main_pass_tab
        self.tree = ttk.Treeview(
            tab,
            columns=('portal', 'login'),
            show='headings',
            height=10
        )
        self.crypto = Crypto(password)
        self.db = db
        self.fill_table_with_data()
        self.config_tree()
        self.tree.bind('<<TreeviewSelect>>', self.on_click)

    def on_click(self, event):
        item = self.tree.selection()[0]
        selection = self.tree.item(item, 'values')
        with Session(self.db) as session:
            credential = session.query(Credentials).filter(
                Portal.name == selection[0],
                Credentials.login == selection[1]
            ).one()

            try:
                decrypted = self.crypto.decrypt(credential.password)
            except InvalidToken:
                self.tree.pack_forget()
                self.tabs.add(self.main_pass_tab, text='input password')
                self.tabs.select(0)
                return 0

            self.root_window.clipboard_clear()
            self.root_window.clipboard_append(decrypted)

    def fill_table_with_data(self):
        with Session(self.db) as session:
            for credential in session.query(Credentials).all():
                credential = DTOCredentials(credential.portal.name, credential.login)
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


if __name__ == '__main__':
    engine = create_engine('sqlite:///database.db', future=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'install':
        install(engine)
        print('Tables has been created successfully')

    root = tk.Tk()
    root.title('Password Manager')
    root.geometry('500x300')


    def pass_on_click():
        tabs.hide(0)
        credential_list = CredentialList(cred_tab, root, engine, pass_entry.get(), tabs, main_pass_tab)
        AddPassword(add_cred_tab, engine, credential_list, tabs, pass_entry.get())


    tabs = ttk.Notebook(root)
    main_pass_tab = ttk.Frame(tabs)
    cred_tab = tk.Frame(tabs)
    add_cred_tab = tk.Frame(tabs)

    tabs.add(main_pass_tab, text='input password')
    tabs.add(cred_tab, text='Credentials')
    tabs.add(add_cred_tab, text='Add password')
    tabs.pack(expand=1, fill='both')

    pass_label = ttk.Label(main_pass_tab, text='Input password:')
    pass_entry = ttk.Entry(main_pass_tab, show='*')
    pass_button = ttk.Button(main_pass_tab, text='OK', command=pass_on_click)

    pass_label.pack(padx=5, pady=5)
    pass_entry.pack(padx=5, pady=5)
    pass_button.pack(padx=5, pady=5)

    root.mainloop()
