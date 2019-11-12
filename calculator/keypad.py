from calcFunctions import *

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantMap = {
    'pi': '3.141592',
    '빛의 이동 속도 (m/s)': '3E+8',
    '소리의 이동 속도 (m/s)': '340',
    '태양과의 평균 거리 (km)': '1.5E+8'
}

functionMap = {
    'factorial (!)': factorial,
    '-> binary': toBinary,
    'binary -> dec': toDec,
    'dec -> roman': decToRoman,
    'roman -> dec': romanToDec
}
