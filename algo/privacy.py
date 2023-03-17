def getAddMonth(d1, d2):
    # d1 약관동의 날짜 문자열
    # d2 유효 기간 문자열
    d2 = int(d2)
    date = d1.split('.')

    for i, x in enumerate(date):  # 숫자로 변환
        date[i] = int(x)

    Y = date[0]
    m = date[1]
    d = date[2]

    if m + d2 > 12:

        rest = m + d2
        y = 0

        while rest > 12:
            rest -= 12
            y += 1
        Y += y
        m = rest
    else:
        m += d2
    print(Y,m,d)
    return (Y, m, d)


def compareDate(today, pday):
    today = today.split('.')
    ty = int(today[0])
    tm = int(today[1])
    td = int(today[2])

    if ty > pday[0]:
        return -1
    elif ty == pday[0]:
        if tm > pday[1]:
            return -1
        elif tm == pday[1]:
            if td >= pday[2]:
                return -1
    return 1


def solution(today, terms, privacies):
    # today 오늘 날짜 문자열
    # terms 약관의 유효 기간을 담은 1차원 문자열 배열
    # privacies 수집된 갱ㄴ정보의 정보를 담은 1차원 문자열 배열

    # 딕셔너리로 변환
    answer = []
    due = {x.split()[0]: int(x.split()[1]) for x in terms}

    for e, i in enumerate(privacies):
        privacie = i.split()
        addMonth = due[privacie[1]]
        addResult = getAddMonth(privacie[0], addMonth)
        if compareDate(today, addResult) < 0:
            answer.append(e+1)
    answer.sort()

    return answer
today ="2022.05.19"
terms = ["A 6", "B 12", "C 3"]
pri = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today,terms,pri))