import tkinter as tk
from tkinter import *
from tkinter import ttk
import main
# data = [
#     {'Name': 'D:',
#      'Attribute': 'DIRECTORY',
#      'Date_Created': 0,
#      'Time_Created': 0,
#      'Size': 0,
#      'Children':
#          [
#              {'Name': 'SECOND.   ',
#               'Attribute': 'DIRECTORY',
#               'Date_Created': '29/3/2023',
#               'Time_Created': '10:22:19', 'Size': 0, 'Children':
#               [{'Name': 'docTest2.docx',
#                            'Attribute': 'ARCHIVE', 'Size': 0, 'Date_Created': '29/3/2023', 'Time_Created': '10:22:19'}]}, {'Name': 'TEST.TXT', 'Attribute': 'ARCHIVE', 'Size': 5, 'Date_Created': '29/3/2023', 'Time_Created': '10:22:19'}, {'Name': 'DOCUMENT.   ', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': [{'Name': 'thuvienhoclieu.com-Bo-de-thi-giua-Ki-2-Toan-8-nam-2022-co-dap-an.docx\x00', 'Attribute': 'ARCHIVE', 'Size': 613906, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': 'thuvienhoclieu.com-Trac-nghiem-on-tap-Toan-6-CTST-giua-HK2.docx\x00', 'Attribute': 'ARCHIVE', 'Size': 2125854, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}]}, {'Name': 'Dumb Mêm\x00', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': [{'Name': '280476110_136900915593740_5008353252623914579_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 76836, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '281038029_3487899421440442_5100370999465771142_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 59997, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '281286290_1192843454970428_7817779488501663921_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 81423, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '281328850_2104827453020413_4257538719060227133_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 132326, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '282792406_573885677463566_7690489439039068625_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 95544, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '283096233_1166475207255294_9122747780609148715_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 42403, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '283567486_1732898923710994_3192206505130348237_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 13645, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '283695325_1448784955571045_2227570152238139135_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 59130, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '284138962_417907986907016_6207887526400993776_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 31665, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '284173321_771908933974359_2026071460892497747_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 22575, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '284599867_549962790048817_1761629008859076941_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 54169, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '285230175_4497559997013205_6104544199087184749_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 7911, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '285500256_154304747133925_2431896949516430432_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 60370, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '285724573_133636039327727_3868110372095314538_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 33356, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '286401174_583057299879737_7396660998002401778_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 52104, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '286987187_5800138133334027_8189568189211242802_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 53641, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287289758_371954768251873_4649913961457664550_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 93683, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287295150_706673840640087_2915380713592139007_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 12535, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287320276_1241436683327953_6607701436940257692_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 221572, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287475525_320654583594760_1644998739994311907_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 25837, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287487088_136861862293294_6217522039874619812_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 91278, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '287758347_806186783680687_8386078947788057964_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 21977, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '288069646_3341471249506418_1115126369931697867_n.jpg', 'Attribute': 'ARCHIVE', 'Size': 72318, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '288463691_555286826273083_6205014063860903793_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 27149, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '289117092_734681407751469_2089071523564566131_n.jpg\x00', 'Attribute': 'ARCHIVE', 'Size': 24028, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': '788789_n.jpg\x00', 'Attribute': 'READ ONLY', 'Size': 1869116271, 'Date_Created': '0/8/1980', 'Time_Created': '0:8:0'}, {'Name': 'a7001000.030', 'Attribute': 'ARCHIVE,DIRECTORY,READ ONLY', 'Size': 808464484, 'Date_Created': '16/1/2008', 'Time_Created': '6:1:16'}, {'Name': '\x16\x1a\x1d%\x1f\x1a\x1b#.\x1c\x16\x16', 'Attribute': 'ARCHIVE', 'Size': 4280822056, 'Date_Created': '7/9/2000', 'Time_Created': '4:49:3'}, {'Name': '\x01\x01\x01\x00\x00\x00\x00\x00.\x00\x00\x00', 'Attribute': '', 'Size': 16843009, 'Date_Created': '4/8/1982', 'Time_Created': '0:24:2'}]}, {'Name': 'HINH ANH\x00', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': []}, {'Name': 'TESTING.   ', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': [{'Name': 'doc test.docx', 'Attribute': 'ARCHIVE', 'Size': 12738, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': 'Inside_testing\x00', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': [{'Name': 'Hello.txt\x00', 'Attribute': 'ARCHIVE', 'Size': 0, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': 'HEllo_Folder\x00', 'Attribute': 'DIRECTORY', 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14', 'Size': 0, 'Children': [{'Name': 'BRUH.TXT', 'Attribute': 'ARCHIVE', 'Size': 0, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}]}]}]}, {'Name': 'bo-de-thi-giua-hoc-ki-2-mon-toan-lop-7.pdf\x00', 'Attribute': 'ARCHIVE', 'Size': 393725, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': 'de-thi-giua-ki-2-toan-6-ctst.pdf\x00', 'Attribute': 'ARCHIVE', 'Size': 405441, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}, {'Name': 'Ref_BT_FAT1.pdf\x00', 'Attribute': 'ARCHIVE', 'Size': 457965, 'Date_Created': '29/3/2023', 'Time_Created': '23:36:14'}]}, {'Name': 'E:', 'Attribute': 'DIRECTORY', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:00', 'Size': 840, 'Children': [{'Name': 'de-thi-giua-ki-2-toan-6-ctst.pdf', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 392}, {'Name': 'DOCUMENT', 'Attribute': 'DIRECTORY', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 824, 'Children': [{'Name': 'thuvienhoclieu.com-Bo-de-thi-giua-Ki-2-Toan-8-nam-2022-co-dap-an.docx', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 464}, {'Name': 'thuvienhoclieu.com-Trac-nghiem-on-tap-Toan-6-CTST-giua-HK2.docx', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 448}]}, {'Name': '$RECYCLE.BIN', 'Attribute': 'DIRECTORY', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 536, 'Children': [{'Name': 'S-1-5-21-2553658766-3498898958-3403543597-1001', 'Attribute': 'DIRECTORY', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 960, 'Children': [{'Name': '$R9Q3OP4', 'Attribute': 'DIRECTORY', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 392, 'Children': ''}, {'Name': '$RR8TX0I.pdf', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '10:23:10', 'Size': 392}, {'Name': 'desktop.ini', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '10:29:16', 'Size': 432}, {'Name': '$I9Q3OP4', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '23:31:22', 'Size': 352}, {'Name': '$IR8TX0I.pdf', 'Attribute': 'ARCHIVE', 'Date_Created': '29/03/2023', 'Time_Created': '23:31:22', 'Size': 424}]}]}]}]
data = main.main()

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
                node_id = tree.insert(parent_node, 'end', text=''+node['Name'] , values=[
                        node['Attribute'], node['Date_Created'], node['Time_Created'], node['Size']])
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
                # if values:
                #     print('Name:', event.widget.item(node_id)['text'])
                #     print('Attribute:', values[0])
                #     print('Date Created:', values[1])
                #     print('Time Created:', values[2])
                #     print('Size:', values[3])



        # Create the content of the disk editor frame
        # label = tk.Label(self, text="Disk editor frame", font=("Arial", 24))
        # label.pack(pady=50)
        # Global area
        # Create the main window and TreeView widget
        # root = tk.Tk()
        # root.title('Directory Tree')
        # root.geometry('900x600')
        # root.maxsize(1980, 1024)
        # root.config(bg="#FFCC98")
        tree = ttk.Treeview(self, columns=['Attribute', 'Date_Created', 'Time_Created', 'Size'])

        left_frame = Frame(self, bd=0, width=200, height=400)
        # left_frame.grid(row=0, column=0, padx=10, pady=5)
        left_frame.pack(side="left", fill="both", padx=50,pady=60, expand=True)

        tree = ttk.Treeview(left_frame)
        tree.pack(side="left", fill="both", expand=True)

        # Add a scrollbar to the left frame
        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)


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
        # tree.pack(fill=tk.BOTH, expand=True)
        
        # Bind the click event to the TreeView widget
        # Bind the click event to the TreeView widget
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
