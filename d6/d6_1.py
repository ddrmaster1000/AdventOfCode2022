# Write the python code with as few characters as possible to solve the following problem, given an input file input.txt:

def find_marker(s):
    # Iterate over the characters in the string.
    for i in range(len(s)):
        # Check if the last four characters are all different.
        if len(set(s[i-3:i+1])) == 4:
        # Return the index of the last character in the marker.
            return i + 1

if __name__ == "__main__":
    print(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) # 7
    print(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz")) # 5
    print(find_marker("nppdvjthqldpwncqszvftbrmjlhg")) # 6
    print(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) # 10
    print(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) # 11

    with open("d6/input_1.txt") as f:
        s = f.read().strip()
        print(find_marker(s))
