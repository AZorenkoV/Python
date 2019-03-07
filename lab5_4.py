"""def file_search(folder, filename) :
    path = "False"
    for x in folder :
        if type(x) == list :
            if file_search(x, filename) :
                path = folder[0] + "/" +  file_search(x, filename)
        if x == filename :
            return folder[0] + "/" + filename
        if filename in path :
            return path
    return bool(0)
"""
def file_search(folder, filename):
    path = str(folder[0]) + '/'
    if filename in folder[1:]:
        return path + filename
    else:
        for item in folder[1:]:
            if type(item) is list and len(item)> 1:
                src = file_search(item, filename)
                if src != False:
                    path = path + str(src)
                return path
        if path == path:
            return False
        else:
            return path

print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'find.me')
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
print file_search(['C:'], 'crack.exe')
