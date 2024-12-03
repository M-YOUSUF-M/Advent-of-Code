left_list = []
right_list = []

with open('input.txt','r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
sum_ = 0;        
for num in left_list:
    similarity = num * right_list.count(num)
    sum_ += similarity
print(sum_)
