# Python code​​​​​​‌‌​​​‌​​​​‌​‌‌‌​​​​‌‌​​‌​ below
# Converts a string hexadecimal number (max = 3 characters) into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}



def hexToDec(hexNum):
    # Example Cases:
    # 2A -> (2*16)+(A*1)
    # CAB -> (C*256)+(A*16)+(B*1)
    # hexNum = xyz -> (x*256)+(y*16)+(z*1)
    

    if len(hexNum) == 1:
        if hexNum[0] not in hexNumbers:
            return None
        dec = (hexNumbers[hexNum[0]]*1)
        return dec

    elif len(num_str) == 2:
        if hexNum[0] not in hexNumbers:
            return None
        if hexNum[1] not in hexNumbers:
            return None
        dec = (hexNumbers[hexNum[0]]*16) + (hexNumbers[hexNum[1]]*1)
        return dec

    elif len(num_str) == 3:
        if hexNum[0] not in hexNumbers:
            return None
        if hexNum[1] not in hexNumbers:
            return None
        if hexNum[2] not in hexNumbers:
            return None
        dec = (hexNumbers[hexNum[0]]*256) + (hexNumbers[hexNum[1]]*16) + (hexNumbers[hexNum[2]]*1)
        return dec 


