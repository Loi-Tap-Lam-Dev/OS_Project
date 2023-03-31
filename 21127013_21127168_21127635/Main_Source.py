import tkinter as tk
from tkinter import *
from tkinter import ttk
import Read_Disk_Information

data = Read_Disk_Information.Get_InFo_From_All_Disk()

class MainMenuFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="#E7F6F2")
        self.pack(fill=tk.BOTH, expand=True)
        
        # Create the "Disk editor" label with big size
        label = tk.Label(self, text="DISK EDITOR", font=("Arial", 24), fg='#2C3333', bg='#A5C9CA',padx=20, pady=20, )
        label.pack(pady=50)
        
        # Create the "Start" button
        start_button = tk.Button(self, text="Start", font=("Arial", 18), fg='#2C3333', bg='#A5C9CA', command=self.start_button_clicked)
        start_button.pack(pady=20)
        
    def start_button_clicked(self):
        # Create a new instance of the DiskEditorFrame class and switch to it
        new_frame = DiskEditorFrame(self.master)
        self.pack_forget()
        new_frame.pack()
        
        
class DiskEditorFrame(tk.Frame):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.config(bg="#E7F6F2")
        self.pack(fill=tk.BOTH, expand=True)
        
        def load_tree(tree, parent_node, data):
            for node in data:
                Icon = ''
                if node['Type'] == 'FILE': Icon = '📄'
                if node['Type'] == 'FOLDER': Icon = '📁'
                if node['Type'] == 'FAT32' or node['Type'] == 'NTFS': Icon = '💽'
                
                node_id = tree.insert(parent_node, 'end', text = Icon + " " + node['Name'], values=[
                        node['Attribute'], node['Date_Created'], node['Time_Created'], node['Size'], node['Type']])
                if 'Children' in node:
                    load_tree(tree, node_id, node['Children'])
                    
        # Callback function to display file/folder information when a node is clicked
        def on_click(event):
            node_id = event.widget.focus()
            if node_id != '':
                values = event.widget.item(node_id)['values']
                # print(values)
                name_var.set(event.widget.item(node_id)['text'])
                attributes_var.set(values[0])
                date_var.set(values[1])
                time_var.set(values[2])
                size_var.set(values[3])
                type_var.set(values[4])
        #tree = ttk.Treeview(self, columns=['Attribute', 'Date_Created', 'Time_Created', 'Size'])

        left_frame = Frame(self, bd=0, width=200, height=400)
        # left_frame.grid(row=0, column=0, padx=10, pady=5)
        left_frame.pack(side="left", fill="both", padx=50,pady=60, expand=True)

        tree = ttk.Treeview(left_frame)
        tree.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the left frame
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # scrollbar_X = ttk.Scrollbar(left_frame, orient="horizontal", command=tree.xview)
        # scrollbar_X.pack(side="bottom", fill="x")
        # tree.configure(xscrollcommand=scrollbar_X.set)


        right_frame = Frame(self,bd=4, width=900, height=900,bg='#A5C9CA')

        right_frame.pack(side="left", fill="y", padx=0,pady=100, expand=True)

        name_label = Label(right_frame, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Name:", font=("Arial", 11))
        name_label.grid(row=0, column=0,sticky="w", padx=5, pady=8)
        name_var = StringVar()
        name_entry = Entry(right_frame, textvariable=name_var, bg='#A5C9CA', state="readonly", width=25, font=("Arial",11))
        name_entry.grid(row=0, column=1, sticky="w",padx=5, pady=8)

        attributes_label = Label(right_frame, bd=0, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Attributes:", font=("Arial", 11))
        attributes_label.grid(row=1, column=0, sticky="w")
        attributes_var = StringVar()
        attributes_entry = Entry(right_frame, bg='#A5C9CA', textvariable=attributes_var, state="readonly", width=25, font=("Arial",11))
        attributes_entry.grid(row=1, column=1, sticky="w", padx=5, pady=8)

        date_label = Label(right_frame, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Date Created:", font=("Arial", 11))
        date_label.grid(row=2, column=0, sticky="w")
        date_var = StringVar()
        date_entry = Entry(right_frame, bg='#A5C9CA', textvariable=date_var, state="readonly", width=25, font=("Arial",11))
        date_entry.grid(row=2, column=1, sticky="w", padx=5, pady=8)

        time_label = Label(right_frame, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Time Created:", font=("Arial", 11))
        time_label.grid(row=3, column=0, sticky="w")
        time_var = StringVar()
        time_entry = Entry(right_frame, bg='#A5C9CA', textvariable=time_var, state="readonly", width=25, font=("Arial",11))
        time_entry.grid(row=3, column=1, sticky="w", padx=5, pady=8)

        size_label = Label(right_frame, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Size:", font=("Arial", 11))
        size_label.grid(row=4, column=0, sticky="w")
        size_var = StringVar()
        size_entry = Entry(right_frame, bg='#A5C9CA', textvariable=size_var, state="readonly", width=25, font=("Arial",11))
        size_entry.grid(row=4, column=1, sticky="w", padx=5, pady=8)

        type_label = Label(right_frame, bg='#A5C9CA', padx=5, pady=8, fg='#2C3333', text="Type:", font=("Arial", 11))
        type_label.grid(row=5, column=0, sticky="w")
        type_var = StringVar()
        type_entry = Entry(right_frame, bg='#A5C9CA', textvariable=type_var, state="readonly", width=25, font=("Arial",11), fg='#2C3333')
        type_entry.grid(row=5, column=1, sticky="w", padx=5, pady=8)
        load_tree(tree, '', data)

        tree.bind('<ButtonRelease-1>', on_click)

        # Create the "Back" button
        back_button = tk.Button(self, text="Back to main menu", font=("Arial", 12), fg='#2C3333', bg='#A5C9CA', command=self.back_button_clicked)
        back_button.pack(pady=10)
        
    def back_button_clicked(self):
        # Switch back to the main menu frame
        new_frame = MainMenuFrame(self.master)
        self.pack_forget()
        new_frame.pack()
                

class MainApplication(tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        self.title("Main Menu")
        self.geometry("900x600")
        # self.config(bg="#FFCC98")
        # Create the main menu frame and register it with the master
        self.main_menu_frame = MainMenuFrame(self)

def main():
    
    app = MainApplication()
    app.mainloop()

main()
