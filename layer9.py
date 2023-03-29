import tkinter as tk
from tkinter import ttk

# Define the nested list of dictionaries representing the directory tree
file_system = [
    {
        'Name': 'root',
        'Attributes': {
            'read_only': True,
            'hidden': False
        },
        'Date_Created': '2022-01-01',
        'Time_Created': '10:00:00',
        'Size': 0,
        'Children': [
            {
                'Name': 'home',
                'Attributes': {
                    'read_only': False,
                    'hidden': False
                },
                'Date_Created': '2022-01-02',
                'Time_Created': '09:00:00',
                'Size': 0,
                'Children': [
                    {
                        'Name': 'user1',
                        'Attributes': {
                            'read_only': False,
                            'hidden': False
                        },
                        'Date_Created': '2022-01-03',
                        'Time_Created': '12:00:00',
                        'Size': 1000,
                        'Children': []
                    },
                    {
                        'Name': 'user2',
                        'Attributes': {
                            'read_only': False,
                            'hidden': False
                        },
                        'Date_Created': '2022-01-03',
                        'Time_Created': '11:00:00',
                        'Size': 500,
                        'Children': []
                    }
                ]
            },
            {
                'Name': 'etc',
                'Attributes': {
                    'read_only': False,
                    'hidden': False
                },
                'Date_Created': '2022-01-02',
                'Time_Created': '10:00:00',
                'Size': 200,
                'Children': [
                    {
                        'Name': 'config',
                        'Attributes': {
                            'read_only': True,
                            'hidden': False
                        },
                        'Date_Created': '2022-01-03',
                        'Time_Created': '09:00:00',
                        'Size': 100,
                        'Children': []
                    }
                ]
            }
        ]
    }
]

# Define a function to display the properties of a selected item
def display_properties(event):
    selected_item = tree.focus()
    if selected_item != "":
        item = tree.item(selected_item)
        values = item['values']
        name_var.set(values[0])
        attributes_var.set(values[1])
        date_var.set(values[2])
        time_var.set(values[3])
        size_var.set(values[4])

# Define the tkinter GUI
root = tk.Tk()
root.title("Directory Tree")
root.geometry('600x300')
# Define the left frame containing the directory tree
left_frame = ttk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)

tree = ttk.Treeview(left_frame)
tree.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the left frame
scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Define the right frame containing the properties
right_frame = ttk.Frame(root)
right_frame.pack(side="left", fill="both", expand=True)

name_label = ttk.Label(right_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_var = tk.StringVar()
name_entry = ttk.Entry(right_frame, textvariable=name_var, state="readonly",width=30)
name_entry.grid(row=0, column=1, sticky="w")

attributes_label = ttk.Label(right_frame, text="Attributes:")
attributes_label.grid(row=1, column=0, sticky="w")
attributes_var = tk.StringVar()
attributes_entry = ttk.Entry(right_frame, textvariable=attributes_var,  state="readonly",width=30)
attributes_entry.grid(row=1, column=1, sticky="w")

date_label = ttk.Label(right_frame, text="Date Created:")
date_label.grid(row=2, column=0, sticky="w")
date_var = tk.StringVar()
date_entry = ttk.Entry(right_frame, textvariable=date_var, state="readonly",width=30)
date_entry.grid(row=2, column=1, sticky="w")

time_label = ttk.Label(right_frame, text="Time Created:")
time_label.grid(row=3, column=0, sticky="w")
time_var = tk.StringVar()
time_entry = ttk.Entry(right_frame, textvariable=time_var, state="readonly",width=30)
time_entry.grid(row=3, column=1, sticky="w")

size_label = ttk.Label(right_frame, text="Size:")
size_label.grid(row=4, column=0, sticky="w")
size_var = tk.StringVar()
size_entry = ttk.Entry(right_frame, textvariable=size_var, state="readonly",width=30)
size_entry.grid(row=4, column=1, sticky="w")

# Define a function to recursively populate the directory tree
def populate_tree(parent, node):
    if node['Name'] != 'root':
        tree.insert(parent, 'end', text=node['Name'], values=(node['Name'], node['Attributes'], node['Date_Created'], node['Time_Created'], node['Size']))
    if len(node['Children']) > 0:
        for child in node['Children']:
            child_id = tree.insert(parent, 'end', text=child['Name'], values=(child['Name'], child['Attributes'], child['Date_Created'], child['Time_Created'], child['Size']), open=False)
            populate_tree(child_id, child)

# Populate the directory tree with the nested list of dictionaries
populate_tree('', file_system[0])

# Bind the function to display properties to the left frame
tree.bind("<<TreeviewSelect>>", display_properties)

root.mainloop()
