if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
# Extract all unique scores
scores = sorted({s[1] for s in student})

# Second lowest score
second_lowest = scores[1]

# Get all names with second lowest scores
result = [s[0] for s in student if s[1] == second_lowest]

# Sort names alphabetically
result.sort()

# Print each name on a new line
for name in result:
    print(name)