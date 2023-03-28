import tkinter as tk
from tkinter import ttk

# Sample directory tree data
data = [
  {
    "Name": "folder1",
    "Attribute": "directory",
    "Date_Created": "2022-01-01",
    "Time_Created": "10:00:00",
    "Size": 0,
    "Children": [
      {
        "Name": "subfolder1",
        "Attribute": "directory",
        "Date_Created": "2022-01-01",
        "Time_Created": "10:00:00",
        "Size": 0,
        "Children": [
          {
            "Name": "file1.txt",
            "Attribute": "file",
            "Date_Created": "2022-01-01",
            "Time_Created": "10:01:00",
            "Size": 1000
          },
          {
            "Name": "file2.txt",
            "Attribute": "file",
            "Date_Created": "2022-01-01",
            "Time_Created": "10:02:00",
            "Size": 2000
          }
        ]
      },
      {
        "Name": "subfolder2",
        "Attribute": "directory",
        "Date_Created": "2022-01-01",
        "Time_Created": "10:00:00",
        "Size": 0,
        "Children": [
          {
            "Name": "file3.txt",
            "Attribute": "file",
            "Date_Created": "2022-01-01",
            "Time_Created": "10:03:00",
            "Size": 3000
          },
          {
            "Name": "file4.txt",
            "Attribute": "file",
            "Date_Created": "2022-01-01",
            "Time_Created": "10:04:00",
            "Size": 4000
          }
        ]
      }
    ]
  }
]

# Recursive function to load directory tree data into the TreeView widget
def load_tree(tree, parent_node, data):
    for node in data:
        node_id = tree.insert(parent_node, 'end', text=node['Name'], values=[node['Attribute'], node['Date_Created'], node['Time_Created'], node['Size']])
        if 'Children' in node:
            load_tree(tree, node_id, node['Children'])

# Callback function to display file/folder information when a node is clicked
def on_click(event):
    node_id = event.widget.focus()
    if node_id:
        values = event.widget.item(node_id)['values']
        if values:
            print('Name:', event.widget.item(node_id)['text'])
            print('Attribute:', values[0])
            print('Date Created:', values[1])
            print('Time Created:', values[2])
            print('Size:', values[3])

# Create the main window and TreeView widget
root = tk.Tk()
root.title('Directory Tree')
tree = ttk.Treeview(root, columns=['Attribute', 'Date_Created', 'Time_Created', 'Size'])
tree.heading('#0', text='Name')
tree.heading('#1', text='Attribute')
tree.heading('#2', text='Date Created')
tree.heading('#3', text='Time Created')
tree.heading('#4', text='Size')

# Load directory tree data into the TreeView widget
load_tree(tree, '', data)
tree.pack(fill=tk.BOTH, expand=True)

# Bind the click event to the TreeView widget
# Bind the click event to the TreeView widget
tree.bind('<ButtonRelease-1>', on_click)

# Run the main event loop
root.mainloop()

