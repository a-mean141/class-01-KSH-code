def factorial(number):
    answer = 1
    for i in range(1, number+1):
        answer *= i
    return answer


def toBinary(number):
    answer = ""
    while number > 0:
        r = number % 2
        answer += str(r)
        number = number // 2
    answer = answer[::-1]
    return answer

def toDec(number):
    numStr = str(number)
    answer = 0
    position = 1
    for i in range(len(numStr)):
        if numStr[-1-i] == '1':
            answer += position
        position *= 2
    return answer

def toRoman(number):
    numStr = str(number)
    answer = 0
    position = 1
    for i in range(len(numStr)):
        if numStr[-1-i] == '1':
            answer += position
        position *= 2
    return answer
