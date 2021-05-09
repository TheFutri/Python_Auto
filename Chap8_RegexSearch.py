#! python3

import os, re

def search(regex, txt):
    searchRegex = re.compile(regex, re.I)
    result = searchRegex.findall(txt)
    print(result)

whie True:
    dirs = input('absolute path\n')
    if os.path.exists(dirs) == True:
        print('This folder exists')
        break
user_search = input('Enter regular expression\n')

folder = os.listdir(dirs)

for file in folder:
    if file.endswith('.txt'):
        print(os.path.join(dirs, file))
        txtfile = open(os.path.join(dirs, file), 'r+')
        msg = txtfile.read()
        search(user_search, msg)
