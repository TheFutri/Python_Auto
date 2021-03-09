#! python3
# Chap6_Project_bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text =  pyperclip.paste()

lines = text.split('\n')    #into list
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]  #adding to each one in the list '* '
text = '\n'.join(lines)         #adding end line to each position in the list
pyperclip.copy(text)
