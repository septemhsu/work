import os
import re

f = open('access.log', 'r')
new_dict = {}

for line in f.readlines():
    ip= line[:line.find(' ')]
    line = line[line.find("HTTP"):]
    line = line[line.find(" ") + 1:]
    resp_code = line[:line.find(' ')]
    if  resp_code == '404':
        value = new_dict.get(ip, 0)
        if value == 0:
            new_dict[ip] = 1
        else:
            new_dict[ip] = new_dict[ip] + 1

items=new_dict.items() 
backitems=[[v[1],v[0]] for v in items] 
backitems.sort()
for element in backitems:
    print(str(element[0]) + ' ' + element[1])
    
