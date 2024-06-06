import string
def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    alphabet = list(string.ascii_lowercase)
    alphabet = [x for x in alphabet if x not in skip]
    for i in s:
        answer += alphabet[(alphabet.index(i) + index) % len(alphabet)]
    return answer