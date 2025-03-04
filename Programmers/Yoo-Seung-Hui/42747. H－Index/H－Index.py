def solution(citations):

    # 논문 인용 횟수 배열 오름차순 정렬
    citations.sort()  
    answer = 0
    
    # hindex : len(citations) - i 
    for i in range(len(citations)):   
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            break
            
    return answer


