import tkinter as tk
from tkinter import *
from tkinter import ttk

def load_tree(tree, parent_node, data):
    for node in data:
        '''text=node['Name']'''
        node_id = tree.insert(parent_node, 'end', text=''+node['Name'] , values=[
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
        # if values:
        #     print('Name:', event.widget.item(node_id)['text'])
        #     print('Attribute:', values[0])
        #     print('Date Created:', values[1])
        #     print('Time Created:', values[2])
        #     print('Size:', values[3])

# Global area
# Create the main window and TreeView widget
root = tk.Tk()
root.title('Directory Tree')
root.geometry('900x600')
root.maxsize(1980, 1024)
root.config(bg="#FFCC98")
# tree = ttk.Treeview(root, columns=['Attribute', 'Date_Created', 'Time_Created', 'Size'])

left_frame = Frame(root, bd=0, width=200, height=400,bg="#FFF7D9")
# left_frame.grid(row=0, column=0, padx=10, pady=5)
left_frame.pack(side="left", fill="both", padx=50,pady=60, expand=True)

tree = ttk.Treeview(left_frame)
tree.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the left frame
scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)


right_frame = Frame(root,bd=4, width=900, height=800,bg='#FFE6B6')

right_frame.pack(side="left", fill="y", padx=0,pady=150, expand=True)

name_label = Label(right_frame, bg='#FFE6B6', padx=5, pady=10, fg='#000181', text="Name:")
name_label.grid(row=0, column=0,sticky="w")
name_var = StringVar()
name_entry = Entry(right_frame, textvariable=name_var, bg='#FFE6B6', state="readonly", width=25)
name_entry.grid(row=0, column=1, sticky="w",padx=5, pady=8)

attributes_label = Label(right_frame, bd=0, bg='#FFE6B6', padx=5, pady=8, fg='#000181', text="Attributes:")
attributes_label.grid(row=1, column=0, sticky="w")
attributes_var = StringVar()
attributes_entry = Entry(right_frame, bg='#FFE6B6', textvariable=attributes_var, state="readonly", width=25)
attributes_entry.grid(row=1, column=1, sticky="w", padx=5, pady=8)

date_label = Label(right_frame, bg='#FFE6B6', padx=5, pady=8, fg='#000181', text="Date Created:")
date_label.grid(row=2, column=0, sticky="w")
date_var = StringVar()
date_entry = Entry(right_frame, bg='#FFE6B6', textvariable=date_var, state="readonly", width=25)
date_entry.grid(row=2, column=1, sticky="w", padx=5, pady=8)

time_label = Label(right_frame, bg='#FFE6B6', padx=5, pady=8, fg='#000181', text="Time Created:")
time_label.grid(row=3, column=0, sticky="w")
time_var = StringVar()
time_entry = Entry(right_frame, bg='#FFE6B6', textvariable=time_var, state="readonly", width=25)
time_entry.grid(row=3, column=1, sticky="w", padx=5, pady=8)

size_label = Label(right_frame, bg='#FFE6B6', padx=5, pady=8, fg='#000181', text="Size:")
size_label.grid(row=4, column=0, sticky="w")
size_var = StringVar()
size_entry = Entry(right_frame, bg='#FFE6B6', textvariable=size_var, state="readonly", width=25)
size_entry.grid(row=4, column=1, sticky="w", padx=5, pady=8)

type_label = Label(right_frame, bg='#FFE6B6', padx=5, pady=8, fg='#000181', text="Type:")
type_label.grid(row=5, column=0, sticky="w")
type_var = StringVar()
type_entry = Entry(right_frame, bg='#FFE6B6', textvariable=type_var, state="readonly", width=25)
type_entry.grid(row=5, column=1, sticky="w", padx=5, pady=8)


# Load directory tree data into the TreeView widget
def Display(data): 
    # Load directory tree data into the TreeView widget
    load_tree(tree, '', data)
    # tree.pack(fill=tk.BOTH, expand=True)
    
    # Bind the click event to the TreeView widget
    # Bind the click event to the TreeView widget
    tree.bind('<ButtonRelease-1>', on_click)
    
    # Run the main event loop
    root.mainloop()

