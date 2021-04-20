import re

def strippp(txt,arg=''):
    if arg =='':
        regex1 = re.compile(r'^(\s+)')
        mo = regex1.sub('', txt)
        regex2 = re.compile(r'(\s+)$')
        mo = regex2.sub('', mo)
        print(mo)
    else:
        regex1 = re.compile(arg)
        mo = regex1.sub('', txt)
        print(mo)

text = '        So, you can create the illusion of smooth motion        '
strippp(text, 'e')
strippp(text)
