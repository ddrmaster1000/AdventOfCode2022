# Open the file
with open('d6/input_1.txt', 'r') as f:
    # Read the file and store it in a string
    s = f.read()

# Loop through the string, starting at index 14
# s = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
for i in range(14, len(s)):
    # If the length of the set of the last 14 characters is 14, it means that
    # all 14 characters are distinct, so we have found a start-of-message marker
    if len(set(s[i-14:i])) == 14:
        # Print the index of the first character in the marker plus 1 and exit the loop
        print(i)
        break