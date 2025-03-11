def solution(N, number):

    if N == number :
        return 1
    
    answer = -1
    dp = [set() for _ in range(8)]
    
    for i in range(8):   
        dp[i].add(int(str(N)*(i+1)))
        
        
    for i in range(8):
        print(">>", dp[i])
        for j in range(i):
            for d in dp[j]:
                for p in dp[i-j-1]:
                    dp[i].add(d+p)
                    dp[i].add(d-p)
                    dp[i].add(d*p)
                    if p != 0 :
                        dp[i].add(d//p)
                        
        if number in dp[i] :
            return i+1
                        
    return -1

