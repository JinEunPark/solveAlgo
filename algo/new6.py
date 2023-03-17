def divie(s, answer):
    first = s[0]
    same = 0
    notsame = 0

    for i, e in enumerate(s):
        if e == first:
            same += 1
        else:
            notsame += 1

        if same == notsame and len(s) >= 2 and i != len(s)-1:
            answer =+ divie(s[i + 1:], answer)
            return answer + 1
    return answer


def solution(s):
    answer = 0
    return divie(s, answer)

s = "banana"
print(solution(s))