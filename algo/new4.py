def solution(lottos, win_nums):
    # lottos 내가 뽑은 숫자
    # win_nums 1등 숫자
    match_num = 0
    new_lottos = []
    zero = 0


    for i in range(len(lottos)):
        if lottos[i] != 0:
            new_lottos.append(lottos[i])

    zero = len(lottos) - len(new_lottos)

    for i in new_lottos:
        if i in win_nums:
            match_num += 1

    won_dict = {7-x : x for x in range(1,7)}
    won_dict[0] = 6
    answer = [won_dict[match_num+zero],won_dict[match_num]]


    return answer

