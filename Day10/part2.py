file = open("input.txt")

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}" ,">"]

scores = {")" : 3,
          "]" : 57,
          "}" : 1197,
          ">" : 25137
          }

totalError = 0

for line in file:
    stack = []
    for char in line:
        if any(char == openner for openner in openings):
            stack.append(char)
        if any(char == closer for closer in closings):
            top = stack.pop()
            if top != char:
                totalError += scores[char]
                break

print(totalError)
