def check(survey_, choices_, result_dict):
    s_list = list(survey_)
    if choices_ == 4:
        pass
    elif choices_ <= 3:
        result_dict[s_list[0]] += 4 - choices_
    else:
        result_dict[s_list[1]] += choices_ - 4

def gernerate_answer(result_dict):
    answer = []
    if result_dict["R"] >= result_dict["T"]:
        answer.append("R")
    else:
        answer.append("T")

    if result_dict["C"] >= result_dict["F"]:
        answer.append("C")
    else:
        answer.append("F")

    if result_dict["J"] >= result_dict["M"]:
        answer.append("J")
    else:
        answer.append("M")

    if result_dict["A"] >= result_dict["N"]:
        answer.append("A")
    else:
        answer.append("N")
    return answer
def solution(survey, choices):
    type = {"R", "T", "C", "F", "J", "M", "A", "N"}
    result_dict = {x: 0 for x in type}
    for i in range(len(survey)):
        check(survey[i], choices[i], result_dict)
    ans = gernerate_answer(result_dict)
    answer = ''

    for i in ans:
        answer += i

    return answer
s = ["AN", "CF", "MJ", "RT", "NA"]
c = [5, 3, 2, 7, 5]
print(solution(s,c))