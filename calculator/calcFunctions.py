def factorial(text):
    result = 1
    number = int(text)
    for i in range(1, number + 1):
        result *= i
    return result

def toBinary(text):
    result = ''
    number = int(text)
    while number > 0:
        r = number % 2
        result += str(r)
        number = number // 2
    result = result[::-1]
    return result

def toDec(text):
    result = 0
    position = 1
    for i in range(len(text)):
        if text[-1 - i] == '1':
            result += position
        position *= 2
    return result

def decToRoman(text):
    number = int(text)
    romanList = [('D', 500), ('CD', 400), ('C', 100), ('L', 50),
                 ('XL', 40), ('X', 10), ('V', 5), ('IV', 4), ('I', 1)]
    index = 0
    result = ''
    while number > 0:
        if number - romanList[index][1] >= 0:
            result += romanList[index][0]
            number -= romanList[index][1]
        else:
            index += 1
    return result

def romanToDec(text):
    romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(text)):
        if i == 0 or romanMap[text[i]] <= romanMap[text[i - 1]]:
            result += romanMap[text[i]]
        else:
            result += romanMap[text[i]] - 2 * romanMap[text[i - 1]]
    return result
