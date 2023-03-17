def solution(number, limit, power):
    # number 기사의 번호
    # limit 제한
    # 제한이 넘는 애들이 쓰는 무기의 파워
    answer = 0

    buf = []
    for i in range(1, number + 1):
        count = 0
        for e in range(1, int(i ** (1 / 2)) + 1):
            if i % e == 0:
                count += 1
                if e ** 2 != i:
                    count += 1
        buf.append(count)

    for i in buf:
        if limit <= i:
            answer += i
        else:
            answer += power

    return answer
n = 5
l = 3
p = 2
print(solution(n,l,p))