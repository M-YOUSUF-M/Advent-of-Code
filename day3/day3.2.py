import re

sum = 0
template = re.compile(r"do()")
template2 = re.compile(r'mul\((\d+),(\d+)\)')

with open('input.txt','r') as file:
    input_ = file.read()
    accept_list = input_.split("don't()")

for i in range(1,len(accept_list)):
    if(template.search(accept_list[i])):
        secondary_list = accept_list[i].split('do()')
        if(len(secondary_list) > 1):
            for item in secondary_list[1:]:
                final_list = template2.findall(item)
                print(final_list)
                for itr in final_list:
                    print(itr)
                    mul = int(itr[0]) * int(itr[1])
                    sum += mul

another_finat_list = template2.findall(accept_list[0])        

for item in another_finat_list:
    print(item)
    mul = int(item[0]) * int(item[1])
    sum += mul

print(sum)

