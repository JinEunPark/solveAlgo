def solution(new_id):
    new_id = new_id.lower()
    new_id_ = ''
    new = ''

    for i in new_id:
        if i not in '~!@#$%^&*()=+[{]}:?,<>/':
            new_id_ = new_id_ + i

    for i in range(len(new_id_)):
        if i == len(new_id_) - 1:
            new = new + new_id_[i]
        else:
            if new_id_[i] == '.' and new_id_[i + 1] == '.':
                pass
            else:
                new = new + new_id_[i]

    if len(new) == 0:
        new = "a"

    if new[-1] == '.':
        new = new[:-1]
    if len(new) == 0:
        new = "a"

    if new[0] == '.':
        new = new[1:]

    if len(new) == 0:
        new = "a"

    if len(new) >= 16:
        new = new[:15]

    if new[-1] == '.':
        new = new[:-1]

    if len(new) <= 2:
        while len(new) < 3:
            new = new + new[0]

    return new

n = "=.="
print(solution(n))