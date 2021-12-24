inPacket = open("input.txt").read().strip()


# not useing bin(int(char, 16)) bc that causes lots of extra chars and unaligned bytes
hexToBin = {
    "0"  : "0000",
    "1"  : "0001",
    "2"  : "0010",
    "3"  : "0011",
    "4"  : "0100",
    "5"  : "0101",
    "6"  : "0110",
    "7"  : "0111",
    "8"  : "1000",
    "9"  : "1001",
    "A"  : "1010",
    "B"  : "1011",
    "C"  : "1100",
    "D"  : "1101",
    "E"  : "1110",
    "F"  : "1111"
}

def packetHexToBin(packet):
    packetBin = ""
    for char in packet:
        packetBin += hexToBin[char]
    return packetBin

def unpack(packet):
    version = int(packet[0:3], 2)
    typeid = int(packet[3:6], 2)

    if typeid == 4: # literal value
        idx = 6
        num = 0
        done = False
        while not done:
            if packet[idx] == '0':
                done = True
            num *= 16
            num += int(packet[idx+1:idx+5], 2)
            idx = idx+5
        return (idx, num)  # returning: (lengthOfPacket, result)

    else:  # operator 
        lengthTypeID = packet[6]
        if lengthTypeID == '0': # next 15 bits are a num that represents the total length in bits of sub packets
            bitLength = int(packet[7:22], 2)
            offset = 0
            result = -1
            while bitLength != offset:
                packetLen, packetContents = unpack(packet[22+offset:])
                offset += packetLen
                result = jumptable(typeid, result, packetContents)
            return (22+offset, result)

        else: # next 11 bits are a number that represents number of sub packets
            numPacketsLeft = int(packet[7:18], 2)
            offset = 0
            result = -1
            while numPacketsLeft > 0:
                packetLen, packetContents = unpack(packet[18+offset:])
                offset += packetLen
                result = jumptable(typeid, result, packetContents)
                numPacketsLeft -= 1
            return (18+offset, result)

def jumptable(op, prevVal, newVal):
    print("OP: ", op, " PV: ", prevVal, " NV: ", newVal)
    if op == 0:
        if prevVal == -1:
            return newVal
        else:
            return prevVal + newVal

    elif op == 1:
        if prevVal == -1:
            return newVal
        else:
            return prevVal * newVal

    elif op == 2:
        if prevVal == -1:
            return newVal
        else:
            return min(prevVal, newVal)

    elif op == 3:
        if prevVal == -1:
            return newVal
        else:
            return max(prevVal, newVal)

    elif op == 5:
        if prevVal == -1:
            return newVal
        else:
            if prevVal > newVal:
                return 1
            else:
                return 0

    elif op == 6:
        if prevVal == -1:
            return newVal
        else:
            if prevVal < newVal:
                return 1
            else:
                return 0

    elif op == 7:
        if prevVal == -1:
            return newVal
        else:
            if prevVal == newVal:
                return 1
            else:
                return 0
    print("AHHHH! WHY ARE YOU HERE?!")


print(unpack(packetHexToBin("EE00D40C823060")))
print(unpack(packetHexToBin(inPacket)))