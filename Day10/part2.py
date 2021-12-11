file = open("input.txt")

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

pairings = {"(" : ")",
            "[" : "]",
            "{" : "}",
            "<" : ">"
}

scores = {")": 1,
          "]": 2,
          "}": 3,
          ">": 4
          }

errors = []

for line in file:
    incorrectLine = False
    stack = []
    for char in line:
        if any(char == openner for openner in openings):
            stack.append(char)
        elif any(char == closer for closer in closings):
            top = stack.pop()
            if pairings[top] != char:
                incorrectLine = True
                break
    if not incorrectLine:
        error = 0
        while len(stack) > 0:
            error *= 5
            error += scores[pairings[stack.pop()]]
        errors.append(error)

errors.sort()
print(errors[(len(errors) - 1) // 2])