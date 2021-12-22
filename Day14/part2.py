from collections import Counter

base, rules = [line for line in open("input.txt").read().split('\n\n')]
rules = dict([rule.split(' -> ') for rule in rules.strip().split('\n')])

letterCount = Counter(base[-1]) # last letter has no pair but is included in the count
cache = {}

def grow(pair, step, stop):
    if (pair, step) in cache:
        return cache[(pair, step)]
    else:
        if step < stop:
            left = pair[0] + rules[pair]
            right = rules[pair] + pair[1]
            leftCount = grow(left, step + 1, stop)
            rightCount = grow(right, step + 1, stop)
            cache[(pair, step)] = leftCount + rightCount
            return leftCount + rightCount
        else: 
            cache[(pair, step)] = Counter(pair[0])
            return Counter(pair[0])

for i in range(len(base) - 1):
    letterCount = letterCount + grow(base[i:i+2], 0, 40)
print(max(letterCount.values()) - min(letterCount.values()))

