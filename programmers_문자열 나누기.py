def solution(s):
    answer = 0
    a0, a1, i = 1, 0, 0
    while True:
        try:
            i += 1
            if s[i] != s[0]:
                a1 += 1
            else:
                a0 += 1

            if a0 == a1:
                answer += 1
                a0, a1 = 1, 0
                s = s[i+1:]
                i = 0
                if len(s) == 0:
                    break
                else:
                    continue
        except:
            answer += 1
            break

    return answer