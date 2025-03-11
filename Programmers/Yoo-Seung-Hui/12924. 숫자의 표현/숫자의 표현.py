def solution(n):
    answer = 0
    
    for i in range(n):
        sum = 0
        # print(">> {}", i+1 , "번째")
        
        while 1:
            sum += (i+1)
            i += 1
            if sum == n :
                # print("추가")
                answer += 1
                break;
            elif sum > n :
                break;
            
    return answer