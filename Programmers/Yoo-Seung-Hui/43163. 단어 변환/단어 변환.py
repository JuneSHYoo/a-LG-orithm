from collections import deque

def solution(begin, target, words):
    
    if target not in words :
        return 0 

    dq = deque()
    dq.append([begin, 0])
    
    while dq:
        b, count = dq.popleft()
        # print(b, count)
        if b == target :
                return count
                
        for w in words :
            if sum([b!=w for b,w in zip(b,w)]) == 1:
                dq.append([w,count +1])
                words.remove(w)
    return 0