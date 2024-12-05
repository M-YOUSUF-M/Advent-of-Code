import re

template1 = re.compile(r'\d+\|\d+')
update_list = []
update_command = []
sum_ = 0

with open('input.txt','r') as file:
    file_txt = file.read().split("\n")
    for item in file_txt:
        if template1.findall(item):
            update_list.append(item)
        else:
            update_command.append(item)
print(update_command)
for secondaryitem in update_command[1:]:
    secondary_list = secondaryitem.split(',')         
    is_vaiolate_rulse = False

    for item in secondary_list[:]:
        index = secondary_list.index(item)
        for i in secondary_list[index + 1:]:
            if f'{item}|{i}' in update_list:
                print(f'{item}|{i}: ',update_list.index(f'{item}|{i}'))
                print(secondary_list)
            else:
                print('came to else: violate_rule')
                is_vaiolate_rulse = True
                break
        if is_vaiolate_rulse:
            print("came to if is_vaiolate_rules")
            break
    if not is_vaiolate_rulse:
        middle_index = len(secondary_list) // 2
        print(secondary_list[middle_index ])
        sum_ += int(secondary_list[middle_index ])
print(sum_)