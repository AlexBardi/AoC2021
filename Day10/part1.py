file = open("input.txt")

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

pairings = {"(" : ")",
            "[" : "]",
            "{" : "}",
            "<" : ">"
}

scores = {")": 3,
          "]": 57,
          "}": 1197,
          ">": 25137
          }

totalError = 0
errC = 0

for line in file:
    stack = []
    for char in line:
        if any(char == openner for openner in openings):
            stack.append(char)
        elif any(char == closer for closer in closings):
            top = stack.pop()
            if pairings[top] != char:
                totalError += scores[char]
                errC += 1
                break

print(errC)
print(totalError)
