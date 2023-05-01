def solution(babbling):
    answer = 0

    cap = ["aya", "ye", "woo", "ma"]
    d_cap = ['ayaaya','yeye','woowoo','mama']
    b = []
    b2 = []

    for i in babbling:
        if i in cap:
            answer += 1
        else:
            b.append(i)

    for i in b:
        count = 0
        for e in d_cap:
            if e in i:
                count +=1
        if count == 0:
            b2.append(i)



    for i in range(len(b2)):
        j = 0
        while j < 16:
            for e in cap:
                if e in b2[i]:
                    b2[i] = b2[i].replace(e,'')
                    if len(b2[i]) == 0:
                        answer +=1
                        break
            j+=1
    return answer

c = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(c))