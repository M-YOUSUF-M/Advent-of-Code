safe = 0  # Global variable for counting safe reports

def is_safe(input_list):
    return (
        (all(input_list[i] > input_list[i + 1] for i in range(len(input_list) - 1)) or
         all(input_list[i] < input_list[i + 1] for i in range(len(input_list) - 1)))
        and all(1 <= abs(input_list[i] - input_list[i + 1]) <= 3 for i in range(len(input_list) - 1))
    )

with open('input.txt', 'r') as file:
    for line in file:
        input_list = list(map(int, line.strip().split()))
        
        if is_safe(input_list):
            safe += 1
            print("Safe List (No Removal Needed):", input_list)
            continue
        
        # Check if removing one level makes the list safe
        for i in range(len(input_list)):
            modified_list = input_list[:i] + input_list[i + 1:]  # Remove the ith level
            if is_safe(modified_list):
                safe += 1
                print(f"Safe List (Removed Level {input_list[i]}):", modified_list)
                break

print("Total Safe Reports:", safe)

