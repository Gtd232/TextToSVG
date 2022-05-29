
from os import mkdir
try:
    mkdir('/img')
except:
    pass
text = input("Enter text:")
color = input("Enter color: ")
list = list(text)
for i in list:
    with open('/img/' + i + '.svg', 'w', encoding='utf-8') as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1"><text x="0" y="0" fill="'+color+'">'+i+'</text></svg>')