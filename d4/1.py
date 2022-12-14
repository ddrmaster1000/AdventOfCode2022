# Some back and forth with ChatGPT but it finally got the right answer.

# Read the input file
with open('d4/input.txt', 'r') as input_file:
  input_data = input_file.read()

# Initialize a counter for the number of overlapping pairs
num_overlapping_pairs = 0

# Loop over all pairs of assignments
for assignment_pair in input_data.strip().split('\n'):
  # Split the pair into two assignments
  assignment1, assignment2 = assignment_pair.split(',')

  # Split each assignment into start and end points
  start1, end1 = map(int, assignment1.split('-'))
  start2, end2 = map(int, assignment2.split('-'))

  # Check if one of the assignments fully contains the other
  if (start1 <= start2 <= end1) and (start1 <= end2 <= end1) or (start2 <= start1 <= end2) and (start2 <= end1 <= end2):
    # If so, increment the counter
    num_overlapping_pairs += 1

# Print the number of overlapping pairs
print(num_overlapping_pairs)
