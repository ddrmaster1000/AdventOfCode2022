# Chatgpt struggled with this one really hard. I wrote most of it but the main idea was written by chatgpt.

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
    # Split the line into opponent and solution
    opponent, solution = line.strip().split()

    # Check if the round should end in a draw
    if solution == "Y":
        # Choose the same shape as the opponent
        if opponent == "A":
            # Add the score for Rock
            total_score += 1
        elif opponent == "B":
            # Add the score for Paper
            total_score += 2
        elif opponent == "C":
            # Add the score for Scissors
            total_score += 3

        # Add the score for drawing
        total_score += 3

    # Check if the player should lose
    elif solution == "X":
        # Choose the shape that loses against the opponent
        if opponent == "A":
            # Add the score for scissors
            total_score += 3
        elif opponent == "B":
            # Add the score for Rock
            total_score += 1
        elif opponent == "C":
            # Add the score for Paper
            total_score += 2

        # Add the score for losing
        total_score += 0

        # Check if the player should win
    elif solution == "Z":
        # Choose the shape that win against the opponent
        if opponent == "A":
            # Add the score for paper
            total_score += 2
        elif opponent == "B":
            # Add the score for scissors
            total_score += 3
        elif opponent == "C":
            # Add the score for rock
            total_score += 1

        # Add the score for win
        total_score += 6

print(total_score)