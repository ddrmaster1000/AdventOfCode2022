# Open the input file
with open("d2/input.txt") as f:
    # Read the lines from the file
    lines = f.readlines()

# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.

# Initialize the total score to 0
total_score = 0

# Loop through each line in the input
for line in lines:
    # Split the line into opponent and player
    opponent, player = line.strip().split()

    # Check the shape of the player
    if player == "X":
        # Add the score for Rock
        total_score += 1
    elif player == "Y":
        # Add the score for Paper
        total_score += 2
    elif player == "Z":
        # Add the score for Scissors
        total_score += 3

    # Check if the player loses
    if (opponent == "A" and player == "Z") or (opponent == "B" and player == "X") or (opponent == "C" and player == "Y"):
        # Add the score for losing
        total_score += 0

    # Check if the player wins
    elif (opponent == "A" and player == "Y") or (opponent == "B" and player == "Z") or (opponent == "C" and player == "X"):
        # Add the score for winning
        total_score += 6

    # Otherwise, the round is a draw
    else:
        # Add the score for drawing
        total_score += 3

# Print the total score
print(total_score)