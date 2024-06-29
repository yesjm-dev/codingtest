def solution(numbers):
    answer = 0
    for i in range(0, 10, 1):
        if i not in numbers:
            print(i)
            answer += i
    return answer