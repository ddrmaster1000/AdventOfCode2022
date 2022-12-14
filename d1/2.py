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

# Find the top three Elves with the most Calories
top_elves = sorted(elves, key=lambda x: x[0], reverse=True)[:3]

# Calculate the total Calories carried by the top three Elves
total_calories = sum([x[0] for x in top_elves])

# Print the result
print(f'The top three Elves carrying the most Calories have a total of {total_calories} Calories')
