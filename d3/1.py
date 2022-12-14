# Open the file and read the contents
with open('d3/input.txt') as f:
    contents = f.read()

# Initialize a variable to keep track of the sum of priorities
sum_of_priorities = 0

# Loop through each line in the file
for line in contents.split('\n'):
    # Split the line into two compartments
    comp1, comp2 = line[:len(line)//2], line[len(line)//2:]

    # Initialize a set to keep track of common items
    common_items = set()

    # Loop through each character in the first compartment
    for char in comp1:
        # If the character is also in the second compartment, add it to the set of common items
        if char in comp2:
            common_items.add(char)

    # If there is only one common item, add its priority to the sum of priorities
    for item in common_items:
        if str(item).isupper():
            sum_of_priorities += 26
        sum_of_priorities += ord(item.lower()) - 96

# Print the sum of priorities
print(sum_of_priorities)
