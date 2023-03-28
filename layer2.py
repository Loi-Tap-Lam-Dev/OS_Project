import os
import tkinter as tk
from tkinter import ttk

<<<<<<< Updated upstream:layer2.py
=======
        
>>>>>>> Stashed changes:Layer.py
class FileExplorerTreePathGUI:
    def __init__(self, root, file_path, file_attribute_path):
        self.root = root
        self.file_path = file_path
        self.file_attribute_path = file_attribute_path
        self.treeview = ttk.Treeview(self.root, columns=('name', 'attributes'))
        self.treeview.pack(side='left', fill='both', expand=True)

        self.scrollbar = ttk.Scrollbar(self.root)
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.treeview.yview)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        self.treeview.heading('#0', text='Path', anchor='w')
        self.treeview.heading('name', text='Name', anchor='w')
        self.treeview.heading('attributes', text='Attributes', anchor='w')

        self.treeview.bind('<ButtonRelease-1>', self.show_info)

        self.insert_tree_nodes('', self.file_path, self.file_attribute_path)

    def insert_tree_nodes(self, parent, path, attribute_path):
        if not path:
            return

        for component in path:
            if isinstance(component, str):
                if not parent:
                    parent = ''
                file_name = os.path.basename(component)
                print(file_name)
                file_attributes = os.path.splitext(component)[1]
                print(file_attributes)
                self.treeview.insert(parent, 'end', text=component, values=(file_name, file_attributes), open=True)
            elif isinstance(component, dict):
                for key, value in component.items():
                    node = self.treeview.insert(parent, 'end', text=key, open=True)
                    self.insert_tree_nodes(node, value, )

<<<<<<< Updated upstream:layer2.py
=======
    def show_info(self, event):
        item_id = self.treeview.selection()[0]
        file_path = self.treeview.item(item_id, 'text')
        file_name = os.path.basename(file_path)
        file_attributes = os.path.splitext(file_path)[1]
        self.treeview.item(item_id, values=(file_name, file_attributes))

>>>>>>> Stashed changes:Layer.py
if __name__ == '__main__':
    root = tk.Tk()
    root.title('File Explorer Tree Path')
    root.geometry('800x600')
<<<<<<< Updated upstream:layer2.py

    file_path = [
        'C:', 
=======
    
    file_path = [
>>>>>>> Stashed changes:Layer.py
        {'Program Files': [
            'Internet Explorer',
            {'Microsoft Office': [
                'Excel.exe',
                'Word.exe',
                'PowerPoint.exe'
            ]}
        ]},
        {'Users': [
            {'John': [
                'Documents',
                'Downloads',
                {'Pictures': [
                    'Vacation',
                    'Family'
                ]}
            ]},
            {'Mary': [
                'Documents',
                {'Pictures': [
                    'Summer',
                    'Christmas'
                ]}
            ]}
        ]}
    ]
<<<<<<< Updated upstream:layer2.py

    FileExplorerTreePathGUI(root, file_path)

    root.mainloop()
=======
    file_attribute_path = [
        {'Folder': [
            'Folder',
            {'Folder': [
                'File',
                'File',
                'File'
            ]}
        ]},
        {'Folder': [
            {'Folder': [
                'Folder',
                'Folder',
                {'Folder': [
                    'Folder',
                    'Folder'
                ]}
            ]},
            {'Folder': [
                'Folder',
                {'Folder': [
                    'Folder',
                    'Folder'
                ]}
            ]}
        ]}
    ]
    file_date_created_path = [
        {'1/4/2003': [
            '18/2/2002',
            {'20/7/2003': [
                '24/3/2003',
                '31/7/1973',
                '31/12/1967'
            ]}
        ]},
        {'1/4/2003': [
            {'18/2/2002': [
                '24/3/2003',
                '24/3/2003',
                {'24/3/2003': [
                    '24/3/2003',
                    '24/3/2003'
                ]}
            ]},
            {'18/2/2002': [
                '18/2/2002',
                {'18/2/2002': [
                    '18/2/2002',
                    '18/2/2002'
                ]}
            ]}
        ]}
    ]
    file_time_created_path = [
        {'12:00:00': [
            '12:00:00',
            {'12:00:00': [
                '12:00:00',
                '12:00:00',
                '12:00:00'
            ]}
        ]},
        {'12:00:00': [
            {'12:00:00': [
                '12:00:00',
                '12:00:00',
                {'12:00:00': [
                    '12:00:00',
                    '12:00:00'
                ]}
            ]},
            {'12:00:00': [
                '12:00:00',
                {'12:00:00': [
                    '12:00:00',
                    '12:00:00'
                ]}
            ]}
        ]}
    ]
    file_size_path = [
        {'10MB': [
            '5MB',
            {'5MB': [
                '2MB',
                '2MB',
                '1MB'
            ]}
        ]},
        {'5MB': [
            {'3MB': [
                '1MB',
                '1MB',
                {'1MB': [
                    '500KB',
                    '500KB'
                ]}
            ]},
            {'2MB': [
                '1MB',
                {'1MB': [
                    '500KB',
                    '500KB'
                ]}
            ]}
        ]}
    ]

    FileExplorerTreePathGUI(root, file_path, file_attribute_path)

    root.mainloop()
>>>>>>> Stashed changes:Layer.py
