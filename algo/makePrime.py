def solution(numbers):
    answer = 0
    numbers = list(numbers)

    def check(num):
        if num != 0 and num != 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    def pickNum(middle_string, visited, numbers):

        nonlocal answer

        if int(middle_string) not in visited:
            visited.append(int(middle_string))
            num = int(middle_string)

            if check(num):
                answer += 1

        for i in numbers:
            new = middle_string
            new = middle_string + i
            new_numbers = numbers[:]
            new_numbers.remove(i)
            if new not in visited and len(new_numbers) >= 0:
                pickNum(new, visited, new_numbers)

    visited = []

    for i in numbers:
        new_numbers = numbers[:]
        new_numbers.remove(i)
        pickNum(i, visited, new_numbers)

    return answer