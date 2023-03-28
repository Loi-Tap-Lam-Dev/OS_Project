        
# class FileExplorerTreePathGUI:
#     def __init__(self, root, file_path):
#         self.root = root
#         self.file_path = file_path

#         self.treeview = ttk.Treeview(self.root, columns=('name', 'attributes'))
#         self.treeview.pack(side='left', fill='both', expand=True)

#         self.scrollbar = ttk.Scrollbar(self.root)
#         self.scrollbar.pack(side='right', fill='y')
#         self.scrollbar.config(command=self.treeview.yview)
#         self.treeview.config(yscrollcommand=self.scrollbar.set)

#         self.treeview.heading('#0', text='Path', anchor='w')
#         self.treeview.heading('name', text='Name', anchor='w')
#         self.treeview.heading('attributes', text='Attributes', anchor='w')

#         self.treeview.bind('<ButtonRelease-1>', self.show_info)

#         self.insert_tree_nodes('', self.file_path)

#     def insert_tree_nodes(self, parent, path):
#         if not path:
#             return

#         for component in path:
#             if isinstance(component, str):
#                 if not parent:
#                     parent = ''
#                 file_name = os.path.basename(component)
#                 file_attributes = os.path.splitext(component)[1]
#                 self.treeview.insert(parent, 'end', text=component, values=(file_name, file_attributes), open=True)
#             elif isinstance(component, dict):
#                 for key, value in component.items():
#                     node = self.treeview.insert(parent, 'end', text=key, open=True)
#                     self.insert_tree_nodes(node, value)

#     def show_info(self, event):
#         item_id = self.treeview.selection()[0]
#         file_path = self.treeview.item(item_id, 'text')
#         file_name = os.path.basename(file_path)
#         file_attributes = os.path.splitext(file_path)[1]
#         self.treeview.item(item_id, values=(file_name, file_attributes))
