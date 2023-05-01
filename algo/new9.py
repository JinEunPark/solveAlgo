def solution(ingredient):
    answer = 0
    ingredient_str = ''

    for i in ingredient:
        ingredient_str = ingredient_str + str(i)

    right = "1231"

    j = 0
    detect = 0
    while right in ingredient_str:
        if detect == 1:
            j = 0
            detect = 0

        bugger = ingredient_str[j:j + 4]
        if bugger == right:
            ingredient_str = ingredient_str[:j] + ingredient_str[j + 4:]
            answer += 1
            detect = 1
        else:
            j += 1

    return answer
i = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(i))
print(str(i))