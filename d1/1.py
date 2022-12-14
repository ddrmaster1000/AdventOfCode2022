# Write the solution in Python. The input is in the file "input.txt":
#

# Read the input data
with open('d1/input_1.txt') as f:
  data = f.read().strip().split('\n')

# Parse the data and calculate the total Calories for each Elf
elves = []
current_elf = []
for elf_data in data:
  if elf_data == '':
    elves.append((sum(current_elf), current_elf))
    current_elf = []
  else:
    current_elf.append(int(elf_data))

# Find the Elf with the most Calories
max_elf = max(elves, key=lambda x: x[0])

# Print the result
print(f'The Elf carrying the most Calories has a total of {max_elf[0]} Calories')