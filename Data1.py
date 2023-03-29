def Print_Directory_Tree_v3(Entry,i, str, depth = 0):
    
    path = []
    if depth > 6: return None
    
    #print(str + Entry.name, [i for i in Entry.attr if i != "NULL"],'\n')    
    if Entry.attr[3] == 'Directory' and Entry.attr[4] == 'NULL' and Entry.attr[5] == 'NULL' and Entry.attr[6] == 'NULL' and Entry.attr[7] == 'NULL':
        
        for x in Entry.ListEntry:
            str = ' ' * i 
            res = Print_Directory_Tree_v3(x, i + 5, str + '|' + '-' * 4, depth + 1)
            if res != '':
                path.append(res)
                
        dict_path = {}
        dict_path["Name"] = Entry.name
        
        str = ''
        for i in range(len(Entry.attr)): 
            if Entry.attr[i] != "NULL": str += Entry.attr[i] + ','
        
        dict_path["Attribute"] = str
        dict_path["Size"] = Entry.size
        dict_path["Date_Created"] = Entry.createDate
        dict_path["Time_Created"] = Entry.createTime
        dict_path["Size"] = Entry.size
        dict_path["Children"] = path
        
    elif Entry.attr[4] == 'Volume Label' or Entry.attr[5] == 'System File' or Entry.attr[6] == 'Hidden File':
            return ''
    else: 
        dict_path = {}
        dict_path["Name"] = Entry.name
        
        str = ''
        for i in range(len(Entry.attr)):
            if Entry.attr[i] != "NULL": str += Entry.attr[i] + ','
        
        dict_path["Attribute"] = str
        dict_path["Size"] = Entry.size
        dict_path["Date_Created"] = Entry.createDate
        dict_path["Time_Created"] = Entry.createTime
        dict_path["Size"] = Entry.size
        
        return dict_path
    
    return dict_path
