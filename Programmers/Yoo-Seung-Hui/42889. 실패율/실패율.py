def solution(N, stages):
    answer = {}

    for i in range(N):
        # answer[i+1] = stages.count(i+1) / len( [s for s in stages if s >= i+1])
        
        challenge = len( [s for s in stages if s >= i+1])
        if challenge == 0 :
            answer[i+1] = 0
        else: 
            answer[i+1] = stages.count(i+1) / challenge
    
    answerlst = list(dict(sorted(answer.items(), key= lambda x:x[1], reverse = True)).keys())
    
    return answerlst