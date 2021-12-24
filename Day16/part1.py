packet = open("input.txt").read().strip()

packetBin = ""

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

for char in packet:
    packetBin += hexToBin[char]

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
        return (idx, version)  # returning: (lengthOfPacket, version)

    else:  # operator 
        lengthTypeID = packet[6]
        if lengthTypeID == '0': # next 15 bits are a num that represents the total length in bits of sub packets
            bitLength = int(packet[7:22], 2)
            offset = 0
            versionSum = version
            while bitLength != offset:
                packetLen, packetVer = unpack(packet[22+offset:])
                offset += packetLen
                versionSum += packetVer
            return (22+offset, versionSum)

        else: # next 11 bits are a number that represents number of sub packets
            numPacketsLeft = int(packet[7:18], 2)
            offset = 0
            versionSum = version
            while numPacketsLeft > 0:
                packetLen, packetVer = unpack(packet[18+offset:])
                offset += packetLen
                versionSum += packetVer
                numPacketsLeft -= 1
            return (18+offset, versionSum)

# print(unpack("110100101111111000101000"))
# print(unpack("00111000000000000110111101000101001010010001001000000000"))
print(unpack(packetBin))
