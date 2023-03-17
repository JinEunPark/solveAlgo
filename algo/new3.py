def solution(k, score):
    answer = []
    h = []
    for i in score:
        if len(h) < k:
            h.append(i)
            answer.append(min(h))
        elif len(h) >= k:
            h.sort(reverse=True)
            if i <= h[-1]:
                answer.append(h[-1])
                h.sort(reverse=True)

                pass
            else:
                h.pop(-1)
                h.append(i)
                h.sort(reverse=True)
                answer.append(h[-1])
    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
