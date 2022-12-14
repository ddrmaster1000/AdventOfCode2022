# Wrote this one with some help of Amazon CodeWhisperer

# Open the file and read the contents
with open('d3/input.txt') as f:
    contents = f.readlines()

# Initialize a variable to keep track of the sum of priorities
sum_of_priorities = 0

elf_possie = []
# Loop through each line in the file
for i, elf in enumerate(contents, 1):
    elf = elf.strip("\n")
    # Split the line into two compartments
    if i % 3 == 0 and elf_possie:
        elf_possie.append(elf)
        common_letters = set()

        for string in elf_possie:
            for char in string:
                common_letters.add(char)

        steady_letters = common_letters.copy()
        # Some weak help from Amazon CodeWhisperer, including finishing this comment
        for string in elf_possie:
            for letter in steady_letters:
                if letter not in string:
                    try:
                        common_letters.remove(letter)
                    except KeyError:
                        continue

        item = list(common_letters)[0]
        if str(item).isupper():
            sum_of_priorities += 26
        sum_of_priorities += ord(item.lower()) - 96
        elf_possie = []
    else:
        elf_possie.append(elf)


# Print the sum of priorities
print(sum_of_priorities)
