file = open("input.txt")
import numpy as np


gsr = []
csr = []

for line in file:
    gsr.append([line[:-1],line[:-1]])        
    csr.append([line[:-1],line[:-1]])        


def calc(rating, popular):
    while len(rating) != 1:
        oneCount = 0
        zeroCount = 0
        for entry in rating:
            if entry[0][0] == "1":
                oneCount += 1
            else:
                zeroCount += 1
        if popular:
            if oneCount >= zeroCount:
                match = "1"
            else:
                match = "0" 
        else:
            if oneCount >= zeroCount:
                match = "0"
            else:
                match = "1"
        rating = [[x[0][1:],x[1]] for x in rating if x[0][0] == match]

    return int(rating[0][1],2) 
        
print(calc(gsr,True) * calc(csr, False))