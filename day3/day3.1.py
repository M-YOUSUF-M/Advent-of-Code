import re

template = re.compile(r'mul\((\d+),(\d+)\)')
with open('input.txt','r') as file:
    input_ = file.read()
    accept_list = template.findall(input_)
sum:int = 0
for i in accept_list:
    mul = int(i[0]) * int(i[1])
    sum += mul

print(sum)