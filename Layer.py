import tkinter as tk
from tkinter import ttk


class FileExplorerTreePathGUI:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path

        self.treeview = ttk.Treeview(self.root)
        self.treeview.pack(side='left', fill='both', expand=True)

        self.scrollbar = ttk.Scrollbar(self.root)
        self.scrollbar.pack(side='right', fill='y')
        self.scrollbar.config(command=self.treeview.yview)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        self.insert_tree_nodes('', self.file_path)

    def insert_tree_nodes(self, parent, path):
        if not path:
            return

        for component in path:
            if isinstance(component, str):
                if not parent:
                    parent = ''
                self.treeview.insert(parent, 'end', text=component, open=True)
            elif isinstance(component, dict):
                for key, value in component.items():
                    node = self.treeview.insert(parent, 'end', text=key, open=True)
                    self.insert_tree_nodes(node, value)

def Display(file_path):
    root = tk.Tk()
    root.title('File Explorer Tree Path')
    root.geometry('800x600')
    
    # array = {'Hello': ['Hi', 'Bye']}
    # str = "Hi"
    # array[str] = {'Hi', 'Bye'}
    
    # file_path = [{
    #     'C': [ 
    #     {'Program Files': [
    #         'Internet Explorer',
    #         {'Microsoft Office': [
    #             'Excel.exe',
    #             'Word.exe',
    #             'PowerPoint.exe'
    #         ]}
    #     ]},
    #     {'Users': [
    #         {'John': [
    #             'Documents',
    #             'Downloads',
    #             {'Pictures': [
    #                 'Vacation',
    #                 'Family'
    #             ]}
    #         ]},
    #         {'Mary': [
    #             'Documents',
    #             {'Pictures': [
    #                 'Summer',
    #                 'Christmas'
    #             ]}
    #         ]}
    #     ]}
    #     ]
    # }]
    # file_path.append('D:')
    # print(array)
    
    FileExplorerTreePathGUI(root, file_path)

    root.mainloop()
    
# main()