
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
        f.write('<svg version="1.1"><g transform="translate(-229.75,-164.01875)"><g data-paper-data="{&quot;isPaintingLayer&quot;:true}" fill="#000000" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="Sans Serif" font-weight="normal" font-size="40" text-anchor="start" style="mix-blend-mode: normal"><text transform="translate(230,185.76875) scale(0.5,0.5)" font-size="40" xml:space="preserve" fill="'+color+'" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-weight="normal" text-anchor="start" style="mix-blend-mode: normal"><tspan x="0" dy="0">'+i+'</tspan></text></g></g></svg>')